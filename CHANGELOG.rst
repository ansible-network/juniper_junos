=============================
Ansible Network juniper_junos
=============================

.. _Ansible Network juniper_junos_v2.7.2:

v2.7.2
======

.. _Ansible Network juniper_junos_v2.7.2_Major Changes:

Major Changes
-------------

- Added alarm parsers for get_facts `juniper_junos#34 <https://github.com/ansible-network/juniper_junos/pull/34>`_.

- Added ospf parsers for get_facts `juniper_junos#35 <https://github.com/ansible-network/juniper_junos/pull/35>`_.


.. _Ansible Network juniper_junos_v2.7.2_New Functions:

New Functions
-------------

- Add lldp configure function `juniper_junos#27 <https://github.com/ansible-network/juniper_junos/pull/27>`_.


.. _Ansible Network juniper_junos_v2.7.1:

v2.7.1
======

.. _Ansible Network juniper_junos_v2.7.1_New Functions:

New Functions
-------------

- Add support for get_facts function `juniper_junos#24 <https://github.com/ansible-network/juniper_junos/pull/24>`_

- Add support for configure_system_properties function `juniper_junos#23 <https://github.com/ansible-network/juniper_junos/pull/23>`_

- Add support for configure_vlan function `juniper_junos#22 <https://github.com/ansible-network/juniper_junos/pull/22>`_


.. _Ansible Network juniper_junos_v2.7.0:

v2.7.0
======

.. _Ansible Network juniper_junos_v2.7.0_New Functions:

New Functions
-------------

- Add support for edit function `juniper_junos#16 <https://github.com/ansible-network/juniper_junos/pull/16>`_


.. _Ansible Network juniper_junos_v2.7.0_Bugfixes:

Bugfixes
--------

- Fix fails when ansible_connection == netconf `juniper_junos#15 <https://github.com/ansible-network/juniper_junos/pull/15>`_


.. _Ansible Network juniper_junos_v2.6.1:

v2.6.1
======

.. _Ansible Network juniper_junos_v2.6.1_Major Changes:

Major Changes
-------------

- Added configure_user function `juniper_junos#8 <https://github.com/ansible-network/juniper_junos/pull/8>`_.


.. _Ansible Network juniper_junos_v2.6.1_Minor Changes:

Minor Changes
-------------

- Only set testenv:linters to python3 `juniper_junos#12 <https://github.com/ansible-network/juniper_junos/pull/12>`_.

- Add support for tox `juniper_junos#11 <https://github.com/ansible-network/juniper_junos/pull/11>`_.


.. _Ansible Network juniper_junos_v2.6.1_Bugfixes:

Bugfixes
--------

- Fix config manager spec option `juniper_junos#6 <https://github.com/ansible-network/juniper_junos/pull/6>`_.

- Fix zuul CI hooks `juniper_junos#5 <https://github.com/ansible-network/juniper_junos/pull/6>`_.


.. _Ansible Network juniper_junos_v2.6.0:

v2.6.0
======

.. _Ansible Network juniper_junos_v2.6.0_Major Changes:

Major Changes
-------------

- Initial release of the ``juniper_junos`` Ansible role.

- This role provides functions to perform automation activities on Juniper JUNOS devices.


.. _Ansible Network juniper_junos_v2.6.0_New Functions:

New Functions
-------------

- NEW ``config_manager/load`` function provides a means to load or replace configuration text onto a target device running Juniper JUNOS.

- NEW ``config_manager/save`` function saves the current active (running) configuration to the startup configuration.

