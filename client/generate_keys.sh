#!/bin/bash

openssl genrsa -out key.pem 2048
openssl rsa -in key.pem -pubout -outform PEM -pubout -out ../pe/public_key.pem
