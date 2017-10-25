## Fabric.py Cassandra Examples

Example of using Fabric with Cassandra cluster to manage certain configurations

> Fabric is a Python (2.5-2.7) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

### Requirements
Install Fabric (http://www.fabfile.org/) and Python (v2.6+)

### Setup
Check fabfile.py for configuration of hosts and environment settings.

### Usage
Listing all commands:
```bash
fab --list
```

Running Cassandra's nodetool command against multiple hosts
```bash
fab hosts:west nodetool:info
```

### More Info

See http://docs.fabfile.org/en/1.14/ for documentation of Fabric and usage.