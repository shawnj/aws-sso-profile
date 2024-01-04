#!/bin/bash

export AWS_PROFILE=
target_dir=$1
python3 $target_dir/select_aws_profile.py
export $(cat ~/.aws-env | xargs)
echo AWS_PROFILE=$AWS_PROFILE