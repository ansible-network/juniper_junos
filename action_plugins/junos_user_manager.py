# (c) 2018, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}
import re

from ansible.plugins.action import ActionBase


class UserManager:

    def __init__(self, new_users, user_config_data):
        self.__new_users = new_users
        self.__user_config_data = user_config_data

    def _parse_sshkey(self, cfg):
        match = re.search(r'ssh-(?:\S+) (.*)', cfg, re.M)
        if match:
            sshkey = match.group(1)[1:-1]
            return sshkey

    def _parse_role(self, cfg):
        match = re.search(r'class (\S+)', cfg, re.M)
        if match:
            role = match.group(1)
            return role

    def _parse_full_name(self, cfg):
        match = re.search(r'full-name (\S+)', cfg, re.M)
        if match:
            full_name = match.group(1)
            return full_name

    def generate_existing_users(self):
        match = re.findall(r'^set system login user (\S+)', self.__user_config_data, re.M)
        if not match:
            return []

        existing_users = []

        for user in set(match):
            regex = r' %s .+$' % user
            cfg = re.findall(regex, self.__user_config_data, re.M)
            cfg = '\n'.join(cfg)
            obj = {
                'name': user,
                'role': self._parse_role(cfg),
                'sshkey': self._parse_sshkey(cfg),
                'full_name': self._parse_full_name(cfg)
            }

            filtered = {k: v for k, v in obj.items() if v is not None}
            obj.clear()
            obj.update(filtered)

            existing_users.append(obj)

        return existing_users

    def filter_users(self):
        want = self.__new_users
        have = self.generate_existing_users()
        filtered_users = [x for x in want if x not in have]

        changed = True if len(filtered_users) > 0 else False

        return changed, filtered_users


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        try:
            new_users = self._task.args['new_users']
            user_config_data = self._task.args['user_config']
        except KeyError as exc:
            return {'failed': True, 'msg': 'missing required argument: %s' % exc}

        supported_roles = ['operator', 'read-only', 'super-user', 'unauthorized']

        for entry in new_users:
            if entry['role'] and entry['role'] not in supported_roles:
                return {'failed': True, 'msg': 'allowed roles are %s; got \'%s\'' % (supported_roles, entry['role'])}

        result['changed'], result['stdout'] = UserManager(new_users, user_config_data).filter_users()

        return result
