# OPA Test

## Model
This first example is closest to a resource portal-based deployment, except for simplicity, the gateway and resource are on the same server.
![](img/2022-07-02-18-05-30.png)

## Setup
1. Generate keys, certificates and policy file from client/ folder: `bash generate_keys.sh`*

\* Note: to remove all the created files, run `bash cleanup.sh`.

## Starting
1. Start OPA: `bash start-opa.sh`
2. Start application server from the server/ folder: `flask run`

## Requesting Resources

### URL Parameters
The resource can be accessed by passing the correct user and role as URL params:
http://localhost:5000/?user=jack&role=catlover  

### Cookie
Pass the parameters in a cookie header to get access to the resource.  
This test can be done via web browser or curl command.
```
curl -L --cookie "user=jack;role=catlover" localhost:5000
```
  
### JWT
Provide a JWT in the Auth header when requesting the page to access the resource.
1. Generate the JWT by running `bash generate_jwt` in the client/ folder.  
eg:
```bash
% ./generate_jwt.sh
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiamFjayIsInJvbGUiOiJjYXRsb3ZlciJ9.cYHFWKEEJV7KEQCPYwcA-Yk58S-EwFEbjw-jbFTDZY34ynHd4g02gq25-W1KlMp2e62AkNuAzDIK7QU-R73fBSPYMKM1pugTIoMBFOpQED24APZPYnvw9faqoxAydhFrkCKRc9Hj7MZopdk2mP9M094i6UVXsO4uCwcbKkPO_7_LW_E5bWxoN7qHYB-58Q9uZNTYuk6KdXuhusUJQ2aLHIupJOGtpCK5m2-RyvCK0UClrIuWsCFvOFZBHEkVDfAcM0YuLQLKbxbxDvH5moiUr3GyMbJrCer1luXzC2Fqm0n6g1dIoG18yC4buHQePYyC4u4310N4BaTFg_-D1LVcPw

Curl command:
curl -L -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiamFjayIsInJvbGUiOiJjYXRsb3ZlciJ9.cYHFWKEEJV7KEQCPYwcA-Yk58S-EwFEbjw-jbFTDZY34ynHd4g02gq25-W1KlMp2e62AkNuAzDIK7QU-R73fBSPYMKM1pugTIoMBFOpQED24APZPYnvw9faqoxAydhFrkCKRc9Hj7MZopdk2mP9M094i6UVXsO4uCwcbKkPO_7_LW_E5bWxoN7qHYB-58Q9uZNTYuk6KdXuhusUJQ2aLHIupJOGtpCK5m2-RyvCK0UClrIuWsCFvOFZBHEkVDfAcM0YuLQLKbxbxDvH5moiUr3GyMbJrCer1luXzC2Fqm0n6g1dIoG18yC4buHQePYyC4u4310N4BaTFg_-D1LVcPw" localhost:5000
```

2. Include this header in a request to access the resource.
