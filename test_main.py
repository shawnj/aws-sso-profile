import unittest
import os
import select_aws_profile
from unittest.mock import patch

class TestSelectAwsProfile(unittest.TestCase):
    def setUp(self):
        # Create a test config file if it doesn't exist
        self.test_config_path = os.path.join(os.path.expanduser('~'), '.aws/test_config')
        with open(self.test_config_path, 'w') as f:
            f.write('[profile test]\n')

    def test_main(self):
        config_path = "test_config"
        with patch('builtins.input', return_value='1'):
            select_aws_profile.main(config_path)
        with open(os.path.join(os.path.expanduser('~'), '.aws-env'), 'r') as f:
            self.assertEqual(f.read(), 'AWS_PROFILE="test"')

    def tearDown(self):
        os.remove(self.test_config_path)
        os.remove(os.path.join(os.path.expanduser('~'), '.aws-env'))

if __name__ == '__main__':
    unittest.main()