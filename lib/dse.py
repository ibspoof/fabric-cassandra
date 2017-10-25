from fabric.api import *

dse_path = "/etc/dse/"
cass_path = dse_path + "cassandra/"
cass_log_path = "/var/log/cassandra/"
startup_defaults = "/etc/default/dse"


@task
def restart_datastax_agent():
    """
    Restart dse agent service
    :return:
    """
    sudo("service datastax-agent restart")


@task
def start_datastax_agent():
    """
    Start a datastax-agent
    :return:
    """
    sudo("service datastax-agent start")
