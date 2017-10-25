from fabric.api import *

@task
def firewall_add_rule(port):
    """
    Add port to firewalld

    :param port:
    :return:
    """
    sudo("firewall-cmd --zone=public --add-port=" + str(port) + "/tcp --permanent")


@task
def firewall_reload():
    """
    Reload firewall

    :return:
    """
    sudo("firewall-cmd --reload")



@task
def uname():
    """
    Run uname on selected hosts
    :return:
    """
    run("uname -a")


@task
def whoami():
    """
    Run whoami on selected hosts
    :return:
    """
    run("whoami")
