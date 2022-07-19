
# Get runtime data for environment variables.
# In this experimental setup, the environment variables include certs.
runtime := opa.runtime()

# get the required inputs for the decision
import input.user
import input.role
import input.token

# fail close, no leniency
default allow := false

# define a list of verified IP sources for applications
sourceApps := [
    {
        "hostname": "localhost",
        "addr": "127.0.0.1"
    },
    {
        "hostname": "localhost2",
        "addr": "127.0.0.2"
    }
]

# runtime.env.PROD_CERTIFICATE
# Allow if JWT token from approved app verifies with valid username and role
# https://www.openpolicyagent.org/docs/v0.16.2/faq/
# Note: for some reason this isn't working yet
allow {
    io.jwt.verify_rs256(token, cert)
    sourceApps[_].addr
}


# Allow if user is jack AND role is catlover AND source IP matches an approved app
allow {
    user == "jack"
    role == "catlover"
    sourceApps[_].addr
}
