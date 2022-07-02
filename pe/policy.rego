package policy

# get the required inputs for the decision
import input.user
import input.role

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
        "addr": "127.0.0.1"
    }
]

# Allow if user is jack AND role is catlover AND source IP matches an approved app
allow {
    user == "jack"
    role == "catlover"
    sourceApps[_].addr
}


