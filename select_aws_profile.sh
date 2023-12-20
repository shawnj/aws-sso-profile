#!/bin/bash

export AWS_PROFILE=
python3 select_aws_profile.py
export $(cat ~/.aws-env | xargs)
echo AWS_PROFILE=$AWS_PROFILE