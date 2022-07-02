#!/bin/bash

# Run OPA using rego policy
docker run -v $PWD:/example -p 8181:8181 openpolicyagent/opa:edge-static run --server example/policy.rego
