#!/bin/bash

openssl genrsa -out key.pem 2048
openssl rsa -in key.pem -pubout -outform PEM -pubout -out ../server/public_key.pem

# Generate certificate
# https://www.digicert.com/kb/ssl-support/openssl-quick-reference-guide.htm
openssl req -new -key key.pem -out cert.csr -subj "/C=AU/ST=WA/L=Perth/O=Catlovers Inc./OU=IT/CN=catlovers.meow"
openssl x509 -signkey key.pem -in cert.csr -req -days 365 -out ../pe/cert.crt

# Generate docker .env file with certifiate, doesn't work currently
#echo -n "PROD_CERTIFICATE=" > ../pe/env.vars
#sed 'H;1h;$!d;x;y/\n/!/' ../pe/cert.crt | sed 's/!/\\n/g' >> ../pe/env.vars

# Feel bad for doing this lol
echo "package policy

cert = \`$(cat ../pe/cert.crt)\`" > ../pe/cert.var
cat ../pe/cert.var ../pe/policy_base.rego > ../pe/policy.rego
