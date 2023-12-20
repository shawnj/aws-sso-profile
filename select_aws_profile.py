import os
import sys

def let_user_pick(options):
    print("AWS PROFILES: ")

    for i in range(1, len(options) + 1):
        print("{}) {}".format(i, options[i - 1]))

    while True:
        i = input("Enter number: ")
        if i.isdigit() and 0 < int(i) <= len(options):
            return int(i) - 1
        else:
            print("Invalid input. Please enter a number between 1 and {}.".format(len(options)))

def main(config_path):
    # Get the AWS CLI SSO profiles from the '.aws/config' file
    path = os.path.join(os.path.expanduser('~'), '.aws/{config_path}'.format(config_path=config_path))
    configList = []
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if "[" in line.strip() and "sso" not in line.strip():
                newLine = line.replace("\n", "").replace("[profile ", "").replace("]", "")
                configList.append(newLine)
    
    res = let_user_pick(configList)

    # Creates a file ~/.aws-env to hold the current AWS_PROFILE
    with open(os.path.join(os.path.expanduser('~'), '.aws-env'), 'w') as f:
        f.write(f'AWS_PROFILE="{configList[res]}"')

if __name__ == "__main__":
    config_path = "config"
    main(config_path)
