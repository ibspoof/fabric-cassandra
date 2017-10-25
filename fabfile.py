from fabric.api import *
from lib import *

west_hosts = ['10.10.10.1']
east_hosts = ['10.10.11.1']
test_host = west_hosts[0]

# put user used to connect with here or override in command usage
env.user = "user"

# enable use of a pem file by uncommenting below
# env.key_filename = '/path/to/keyfile.pem'

# If you already have all the SSH connection parameters in your ~/.ssh/config file uncomment below
# env.use_ssh_config = True



@task
def hosts(dc):
    """
    Set hosts to run commands on
    :param dc:
    :return:
    """
    if dc == "test":
        env.hosts = test_host
    if dc == "west":
        env.hosts = west_hosts
    if dc == "east":
        env.hosts = east_hosts
    if dc == "all":
        env.hosts = west_hosts + east_hosts

    print "Hosts: " + ', '.join(env.hosts)


def enable_warn():
    env.warn_only = True


def disable_warn():
    env.warn_only = False
