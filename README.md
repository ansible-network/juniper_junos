# juniper_junos

This Ansible Network role provides a set of network functions that are designed
to work with Juniper JUNOS network devices.  The functions included in this role
include gathering facts from JUNOS devices, performing declarative configuration
tasks and handling various operational tasks on the device.

## Requirements

* Ansible 2.6 or later
* Ansible Network Engine Role 2.6.2 or later

## Functions

This section provides a list of the available functions that are including
in this role.  Any of the provided functions can be implemented in Ansible
playbooks to perform automation activities on Juniper JUNOS devices.

Please see the documentation link for each function for details on how to use
the function in an Ansible playbook.

* load [[source]](https://github.com/ansible-network/juniper_junos/blob/devel/tasks/config_manager/load.yaml) [[docs]](https://github.com/ansible-network/juniper_junos/blob/devel/docs/config_manager/load.md)
* save [[source]](https://github.com/ansible-network/juniper_junos/blob/devel/tasks/config_manager/save.yaml) [[docs]](https://github.com/ansible-network/juniper_junoss/blob/devel/docs/config_manager/save.md)
* get_facts [[source]](https://github.com/ansible-network/juniper_junos/blob/devel/tasks/get_facts.yaml) [[docs]](https://github.com/ansible-network/juniper_junos/blob/devel/docs/get_facts.md)
* configure_netconf [[source]](https://github.com/ansible-network/juniper_junos/blob/devel/tasks/configure_netconf.yaml) [[docs]](https://github.com/ansible-network/juniper_junos/blob/devel/docs/configure_netconf.md)

## License

GPLv3

## Author Information

Ansible Network Community (ansible-network)
