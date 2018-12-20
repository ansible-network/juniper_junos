# Configure LLDP on the device

The `configure_lldp` function can be used to set LLDP on Juniper Junos devices.
This function is only supported over `network_cli` connection type and 
requires the `ansible_network_os` value set to `junos`.

## How to set LLDP on the device

To set LLDP on the device, simply include this function in the playbook
using either the `roles` directive or the `tasks` directive.  If no other
options are provided, then all of the available facts will be collected for 
the device.

Below is an example of how to use the `roles` directive to set LLDP on the
Juniper Junos device.

```
- hosts: junos

  roles:
  - name ansible-network.juniper_junos
    function: configure_lldp
  vars:
    lldp:
      - advertisement_interval: 60 
        hold_multiplier: 60
        interface: all
        lcni: 60
        management_address: 192.168.1.1
        pcmht: 4
        pcti: 1
        transmit_delay: 1
        disble_interface: ge-0/0/2
```

The above playbook will set the LLDP with holdtime, reinit, tlv-select, receive,
and transmit to particular interface under the `junos` top level key.  

### Implement using tasks

The `configure_lldp` function can also be implemented using the `tasks` directive
instead of the `roles` directive.  By using the `tasks` directive, you can
control when the fact collection is run. 

Below is an example of how to use the `configure_lldp` function with `tasks`.

```
- hosts: junos

  tasks:
    - name: set lldp to junos devices
      import_role:
        name: ansible-network.juniper_junos
        tasks_from: configure_lldp
      vars:
        lldp:
          - advertisement_interval: 60
            hold_multiplier: 60
            interface: all
            lcni: 60
            management_address: 192.168.1.1
            pcmht: 4
            pcti: 1
            transmit_delay: 1
            disble_interface: ge-0/0/2
```

## Adding new parsers

Over time new parsers can be added (or updated) to the role to add additional
or enhanced functionality.  To add or update parsers perform the following
steps:

* Add (or update) command parser located in `parse_templates/cli`

## Arguments

### advertisement_interval

LLDP advertisement_interval specifies the length of transmit interval for LLDP messages.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### hold_multiplier

LLDP hold_multiplier specifies timer interval for LLDP messages.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### interface

LLDP intefaces parameter sets interface configuration, valid input for the argument is
either `all` or the `interface-name`.

### lcni

This is LLDP lldp-configuration-notification-interval which specifies Time interval for
LLDP notification.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### management_address

This specifies LLDP management address.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### pcti

This is LLDP ptopo-configuration-trap-interval which specifies the interval for physical
topology configuration change trap.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### pcmht

This is LLDP ptopo-configuration-maximum-hold-time which specifies hold time for physical
topology connection entries.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### transmit_delay

This specifies transmit delay time interval for LLDP messages.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.
            
### disble_interface

If user needs to disable LLDP on any particular interface, then user has to specify
respective interface name under this argument and LLDP will bbe disabled on particular
interface.

### state

This sets the LLDP value to the Juniper Junos device and if the value of the state is changed
to `absent`, the role will go ahead and try to delete the condifured LLDP via the arguments
passed.

The default value is `present` which means even if the user doesn't pass the respective
argument, the role will go ahead and try to set the LLDP via the arguments passed to the 
Juniper Junos device.

## Notes

None
