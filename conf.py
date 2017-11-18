from fabric.api import *

# put user used to connect with here or override in command usage
env.user = "user"

# enable use of a password by uncommenting below
# env.password = ""

# enable use of a pem file by uncommenting below
# env.key_filename = '/path/to/keyfile.pem'

# If you already have all the SSH connection parameters in your ~/.ssh/config file uncomment below
# env.use_ssh_config = True


clusters = {
    'my_cluster': {
        'dc1': {
            'rack1': ['10.10.10.1'],
            'rack2': ['10.10.10.2'],
            'rack3': ['10.10.10.3']
        },
        'dc2': {
            'rack1': ['10.10.11.1'],
            'rack2': ['10.10.11.2'],
            'rack3': ['10.10.11.3']
        }
    }
}

# test host to run verification tests
test_host = [clusters['my_cluster']['dc1']['rack1'][0]]
