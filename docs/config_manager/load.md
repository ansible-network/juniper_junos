# Load configuration into device

The `config_manager/load` function provides a means to load either a
configuration text onto a target device running Juniper JUNOS. The `config_manager/load`
function provides configuration values that  allow the source configuration to either
be merged with the current active  configuration (default) or to replace the current active
configuration on the device.

## How to load a configuration

Loading a configuration onto a target device is fairly simple and
straightforward.  By default, the `config_manager/load` function will merge the
contents of the provided configuration file with the configuration running on
the target device.

Below is an example of how to call the `config_manager/load` function.

```
- hosts: junos

  roles:
    - name: ansible-network.juniper_junos
      function: config_manager/load
      config_manager_text: "{{ lookup('file', 'junos.cfg') }}"
```

The example playbook above will simple load the contents of `junos.cfg` onto the
target network devices.

### How to load and replace a configuration

The `config_manager/load` function also provides support for replacing the current
configuration on a device.

In order to replace the configuration, the function as before but adds the
value `replace: yes` to the playbook to indicate that the configuration should
be replaced with the configuration value set in `config_manager_text`.

Note: Take caution when doing configuration replace that you do not
inadvertently replace your access to the device.

```
- hosts: junos

  roles:
    - name: ansible-network.juniper_junos
      function: config_manager/load
      config_manager_text: "{{ lookup('file', 'junos.cfg') }}"
      config_manager_replace: yes
```

## Arguments

### config_manager_text

This value accepts the text form of the configuration to be loaded on to the
remote device. This is a required value.

The default value is `null`

### config_manager_replace

This value enables or disables the configuration replace feature of the
function. In order to use `junos_config_replace` the target device must
support config replace function.

The default value is `False`

### junos_config_remove_temp_files

Configures the function to remove or not remove the temp files created when
preparing to load the configuration file. There are two locations for temp
files, one on the Ansible controller and one on the device. This argument
accepts a boolean value.

The default value is `True`
