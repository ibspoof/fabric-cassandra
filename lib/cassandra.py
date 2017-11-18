from fabric.api import *
import time

dse_path = "/etc/dse/"
cass_path = dse_path + "cassandra/"
cass_log_path = "/var/log/cassandra/"
startup_defaults = "/etc/default/dse"

@task
def shutdown():
    """
    Shutdown a node with flush, drain then stop
    :return:
    """
    nodetool("flush")
    nodetool("drain")
    sudo("service dse stop")

@task
def start():
    """
    Start a node
    :return:
    """
    sudo("service dse start")


@task
def yaml_print(find):
    """
    Find a value via regex in the cassandra.yaml file
    :param find:
    :return:
    """
    file_path = cass_path + "cassandra.yaml"
    sudo("grep " + find + " " + file_path)


@task
def get_log_file(file="system.log", localpath="./"):
    """
    Download a file to local from hosts without collisions
    :param file:
    :param localpath:
    :return:
    """
    if localpath != "./" and localpath.lower().find("c:") < 0:
        local("mkdir -p " + localpath)
    get(cass_log_path + file, localpath + file + "." + env.host)


@task
def rolling_restart(sleep=5, start_sleep=10):
    """
    Rolling restart of nodes w/ sleep time
    :param sleep: default check
    :param start_sleep: 5
    """
    enable_warn()

    sudo(get_nodetool_cmd_str("flush"))
    sudo(get_nodetool_cmd_str("drain"))
    sudo("service dse stop")
    sudo("service dse start")

    print "Sleeping for %d seconds to allow DSE to start" % start_sleep
    time.sleep(start_sleep)

    while sudo(get_nodetool_cmd_str("status")).find("Failed to connect") < 0:
        print "WARN: Unable to connect to JMX, sleeping for %d seconds" % sleep
        time.sleep(sleep)

    while sudo(get_nodetool_cmd_str("status")).find("UN  " + env.host) < 0:
        print "WARN: nodetool host %s is not UN, sleeping for %d seconds" % (env.host, sleep)
        time.sleep(sleep)

    print "Node %s is up." % env.host
    disable_warn()


@task
def nodetool(cmd):
    """
    Run nodetool command
    :param cmd:
    :return:
    """
    sudo(get_nodetool_cmd_str(cmd))


def get_nodetool_cmd_str(command):
    # return "nodetool -u %s -pwf /etc/dse/cassandra/jmxremote.password %s" % (env.user, command)
    return "nodetool %s" % command


##
# below are private commands and should only be used by commands above
##

def yaml_sed(replace, replace_with):
    file_path = cass_path + "cassandra.yaml"
    sudo(get_sed_file_cmd(replace, replace_with, file_path))


def jmv_opts_sed(replace, replace_with):
    file_path = cass_path + "jvm.options"
    sudo(get_sed_file_cmd(replace, replace_with, file_path))


def env_sed(replace, replace_with):
    file_path = cass_path + "cassandra-env.sh"
    sudo(get_sed_file_cmd(replace, replace_with, file_path))


def dse_sed(replace, replace_with):
    file_path = dse_path + "dse.yaml"
    sudo(get_sed_file_cmd(replace, replace_with, file_path))


def spark_env_sed(replace, replace_with):
    file_path = dse_path + "spark/spark-env.sh"
    sudo(get_sed_file_cmd(replace, replace_with, file_path))


def defaults_sed(replace, replace_with):
    sudo(get_sed_file_cmd(replace, replace_with, startup_defaults))


def enable_warn():
    env.warn_only = True


def disable_warn():
    env.warn_only = False


def get_sed_file_cmd(replace_str, replace_with, file_path):
    replace_str = replace_str.replace('"', r'\"')
    replace_str = replace_str.replace('/', '\/')
    replace_with = replace_with.replace('"', r'\"')
    replace_with = replace_with.replace('/', '\/')
    replace_with = replace_with.replace('\\', '\\\\')

    return "sed -i --follow-symlinks -e \"s/" + replace_str + "/" + replace_with + "/g\" " + file_path
