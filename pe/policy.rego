package policy

# get the required inputs for the decision
import input.user
import input.role

# fail close, no leniency
default allow := false

# allow if username AND role match
allow {
    user == "jack"
    role == "authorised"
}
