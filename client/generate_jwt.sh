#!/bin/bash

# header
# {"alg":"RS256","typ":"JWT"}
header="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9"

# name, role can be supplied
if [ $# -lt 2 ]
  then
    # echo "No arguments supplied, assigning compliant defaults"
    user="jack"
    role="catlover"
  else
    user=$1
    role=$2
fi

content=$header.$(echo -n "{\"user\":\"$user\",\"role\":\"$role\"}" | base64 | sed s/\+/-/ | sed -E s/=+$//)

# sign combined header and payload
jwt=$content.$(echo -n $content | openssl dgst -sha256 -binary -sign key.pem | openssl enc -base64 | tr -d '\n=' | tr -- '+/' '-_')
echo $jwt
echo
echo "Curl command:"
echo "curl -L -H \"Authorization: Bearer $jwt\" localhost:5000"

