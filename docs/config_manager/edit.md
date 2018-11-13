#  Tasks to run against a target device

The `config_manager/edit` function provides a means to run independent task that can
either perform configuration changes onto a target device running Juniper JUNOS.

## How to run independent task

Running a task that performs some action onto a target device is fairly simple and
straightforward.  By default, the `config_manager/edit` function will take a list of file path
(absolute or relative) that are included as run time and executed against a target device.

Below is an example of how to call the `config_manager/edit` function.

```
- hosts: junos

  roles:
    - name: ansible-network.juniper_junos
      function: config_manager/edit
      config_manager_includes:
        -  "{{ role_path }}/includes/bgp/{{ bgp_state | default('present') }}.yaml"
```

The example playbook above will simple load the tasks that manages configuration of BGP on
target network devices.
Note: The tasks that are included at runtime can be written by user as per the required functionality.


## Arguments

### config_manager_includes

Provides a list of configuration task that are include at runtime. The individual value in the
list is a path to the task file that should be executed. This is a required value for edit function.

The default value is `null`
