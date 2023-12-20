# AWS SSO Profile Selector

Loads all AWS SSO Profiles and allows you to select the desired one to load.

Once you have completed the initial setup of [AWS SSO](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html), you will have a `~/.aws/config` file that looks something like this:
    
```ini

[profile prod]
sso_account_id = 123456789012
sso_role_name = MyRoleProd
sso_session = my-sso
region = us-east-1
output = json

[profile dev]
sso_account_id = 123456789013
sso_role_name = MyRoleDev
sso_session = my-sso
region = us-east-1
output = json

[sso-session my-sso]
sso_region = us-east-1
sso_start_url = https://my-sso-portal.awsapps.com/start
```

## Usage

```bash
# Ensure the script is executable
chmod +x /<script_directory>/aws-sso-profile.sh

# Create an alias to run the script
alias aws-sso-profile="source /<script_directory>/aws-sso-profile/select-aws-profile.sh"

# Or run the script directly
source /<script_directory>/aws-sso-profile/select-aws-profile.sh

# Run the script with the alias
aws-sso-profile
```

## Example Output

```bash
AWS PROFILES: 
1) prod
2) dev
Enter number: 2
AWS_PROFILE=dev
```
