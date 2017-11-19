from fabric.api import *
from lib import *
from conf import *

@task
def hosts(cluster, data_center, rack="all"):
    """
    Set hosts to run commands on based on cluster name, dc, and rack
    :param cluster:
    :param data_center:
    :param rack:
    :return:
    """
    if cluster == "test":
        env.hosts = test_host

    if cluster not in clusters:
        print "ERROR: Cluster %s not in cluster list in conf.py" % cluster
        exit(1)

    if data_center not in clusters[cluster]:
        print "ERROR: Datacenter %s not in cluster %s in conf.py" % (data_center, cluster)
        exit(1)

    if rack is not "all":
        if rack not in clusters[cluster][data_center]:
            print "ERROR: Rack %s not in cluster %s datacenter %s in conf.py" % (rack, data_center, cluster)
            exit(1)
        else:
            env.hosts = clusters[cluster][data_center][rack]
    else:
        for r in clusters[cluster][data_center]:
            env.hosts += clusters[cluster][data_center][r]

    print "Hosts: " + ', '.join(env.hosts)


def enable_warn():
    env.warn_only = True


def disable_warn():
    env.warn_only = False
