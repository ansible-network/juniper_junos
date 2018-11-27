# Configure System properties on the device

The `configure_system_properties` function can be used to set system properties on 
Juniper Junos devices.  This function is only supported over `network_cli` connection
type and requires the `ansible_network_os` value set to `junos`.

## How to set System properties on the device

To set System properties on the device, simply include this function in the playbook
using either the `roles` directive or the `tasks` directive.  If no other
options are provided, then all of the available facts will be collected for the
device.

Below is an example of how to use the `roles` directive to set system properties
on the Juniper Junos device.

```
- hosts: junos

  roles:
  - name ansible-network.juniper_junos
    function: configure_system_properties
  vars:
    system_properties:
      - hostname: test-
        domain_name: hostname.com
        name_server: 192.168.1.1
        vrf_routing_instance: test
        vrf_interface: ge-0/0/2
        vrf_route_distinguisher: 10.58.255.1:37
        vrf_target: target:10.58.255.1:37
        vrf_import_policy:
        vrf_export_policy:
        vrf_table_label: static
        vrf_table_static_value: 24
```

The above playbook will set the hostname, domain-name and the name-server values to
the host under the `junos` top level key.  

### Implement using tasks

The `configure_system_properties` function can also be implemented using the `tasks` 
directive instead of the `roles` directive.  By using the `tasks` directive, you can
control when the fact collection is run. 

Below is an example of how to use the `configure_system_properties` function with `tasks`.

```
- hosts: junos

  tasks:
    - name: set system properties to junos devices
      import_role:
        name: ansible-network.juniper_junos
        tasks_from: configure_system_properties
      vars:
        system_properties:
          - hostname: test-vyos
            domain_name: hostname.com
            name_server: 192.168.1.1
            vrf_routing_instance: test
            vrf_interface: ge-0/0/2
            vrf_route_distinguisher: 10.58.255.1:37
            vrf_target: target:10.58.255.1:37
            vrf_import_policy:
            vrf_export_policy:
            vrf_table_label: static
            vrf_table_static_value: 24
```

## Adding new parsers

Over time new parsers can be added (or updated) to the role to add additional
or enhanced functionality.  To add or update parsers perform the following
steps:

* Add (or update) command parser located in `parse_templates/cli`

## Arguments

### hostname

This will set the System host name for the VyOS device.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### domain_name

This will set the System domain name for the Juniper Junos device.

The default value is `omit` which means even if the user doesn't pass the respective 
value the role will continue to run without any failure.

### name_server

This will set the Domain Name Server (DNS) for the Juniper Junos device.

The default value is `omit` which means even if the user doesn't pass the respective 
value the role will continue to run without any failure.

### vrf_routing_instance

This will set the Routing instance name for the Juniper Junos device.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_interface

This will set the Interface name for routing instance for the Juniper Junos device.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_route_distinguisher

This will set the Route distinguisher for instance for the Juniper Junos device.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_target

This will set the VRF target community configuration for the Juniper Junos device.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_import_policy

This will set the Import policy for VRF instance RIBs.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_export_policy

This will set the Export policy for VRF instance RIBs

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_table_label

This will set and advertise a single VPN label for all routes in the VRF

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### vrf_table_static_value

This will set VRF static label value that will be used. Range(16..1048575).

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### state

This will set the hostname, domain-name and name-server value to the VyOS device and if
the value of the state is changed to `absent`, role will go ahead and try to delete the
hostname, domain-name and name-server passed via the arguments.

The default value is `present` which means even if the user doesn't pass the respective
argument, the role will go ahead and try to set the hostname, domain-name and name-server 
via the arguments passed to the Juniper Junos device.

## Notes

None
