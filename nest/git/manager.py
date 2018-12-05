from nest.git.gitlab_proxy import GitlabProxy


class CodesManager(object):
    def __init__(self, host, token):
        self.git_proxy = GitlabProxy(host, token)

    def get_group(self, name):
        groups = self.git_proxy.get_groups()
        for group in groups:
            if group.name == name:
                return group
        return None

    def get_or_create_group(self, name):
        group = self.get_group(name)
        if group:
            return group
        else:
            self.git_proxy.create_group(name)
        return self.get_group(name)

    def get_group_projects(self, group_name):
        group = self.get_group(group_name)
        return group.projects.list()

    def get_project(self, name, group_name):
        projects = self.get_group_projects(group_name)
        for project in projects:
            if project.name == name:
                return project
        return None

    def create_project(self, name, group_name):
        group_id = self.get_group(group_name).id
        self.git_proxy.create_project(name, group_id)

    def get_or_create_project(self, name, group_name):
        project = self.get_project(name, group_name)
        if project:
            return project
        self.create_project(name, group_name)
        return self.get_project(name, group_name)

    def get_ssh_key(self, title):
        keys = self.git_proxy.get_ssh_keys()
        for key in keys:
            if key.title == title:
                return key
        return None

    def get_or_create_sshkey(self, title, key):
        ssh_key = self.get_ssh_key(title)
        if ssh_key:
            return ssh_key
        self.git_proxy.upload_ssh_key(title, key)
        return self.get_ssh_key(title)

    def delete_ssh_key(self, title):
        key = self.get_ssh_key(title)
        self.git_proxy.delete_ssh_key(key.id)


