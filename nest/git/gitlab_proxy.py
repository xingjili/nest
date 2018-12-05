import gitlab


class GitlabProxy(object):
    def __init__(self, host, token):
        self._gitlab = gitlab.Gitlab('http://{host}'.format(host=host),
                                     private_token=token)
        self._gitlab.auth()

    def get_groups(self):
        return self._gitlab.groups.list()

    # create group
    def create_group(self, group_name):
        self._gitlab.groups.create({'name': group_name,
                                    'path': group_name})

    def get_projects(self, group_id):
        return self._gitlab.projects.list(group_id=group_id)

    # creat projects
    def create_project(self, name, group_id):
        self._gitlab.projects.create({'name': name,
                                      'namespace_id': group_id})

    # add user ssh key
    def upload_ssh_key(self, title, key):
        return self._gitlab.user.keys.create({'title': title, 'key': key})

    def get_ssh_keys(self):
        return self._gitlab.user.keys.list()

    def delete_ssh_key(self, id):
        return self._gitlab.user.keys.delete(id)
