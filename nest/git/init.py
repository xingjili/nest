from nest.git.manager import CodesManager


class Access(object):
    def __init__(self, token, host):
        self.token = token
        self.host = host


ACCESS = Access(
    token='BNa-yecKjyy9tjazMvA6',
    host='119.255.249.10')


class SshKey(object):
    def __init__(self, title, pub_key):
        self.title = title
        self.pub_key = pub_key


class DireContext(object):
    def __init__(self, group, projects, title, ssh_keys):
        self.group = group
        self.projects = projects
        self.title = title
        self.ssh_keys = ssh_keys


DIRE_CTXT = DireContext(
    group='dire',
    projects=['steam', 'germ', 'boot', 'kolla-ansible', 'kubespray'],
    ssh_keys=[
        SshKey(
            title='boot',
            pub_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNkgne/UjqIk/agZbRi0b+SN5oWXlSWWKTjXc1wgPFfBPbO/aMbpuasMSWIVQu9etw2ed4vtMoAIQUgxKNcFaofjHbpoYRjJreV2hH6Exd+wegA/fvhm5IVku1KwJWPVmVPeGvfHbNEx/wYwc8XssUeHvuwUiRXPcwXCgx1Z5RaPRwqIaQD9Ojv9UybmYjkaIT0q5jAqC0xKrLquvCa5qiceRBYe7VH8TKH1E/wPc2hn87blGVY7OS4dIwSUow0wevVTcoOV7CHqQaw9sjo+ZKpwcj7Ij9L3eRjkbu6oPvJIbothGVOvtpvkVE9UV1nPfBoARdK9c4HOFv0uBllNmj kolla@ubuntu'
        )
    ]
)


def init_dire(access=ACCESS, ctxt=DIRE_CTXT):
    manager = CodesManager(access.host, access.token)
    manager.get_or_create_group(ctxt.group)
    for project in ctxt.projects:
        manager.get_or_create_project(project, ctxt.group)
    for ssh_key in ctxt.ssh_keys:
        manager.get_or_create_sshkey(ssh_key.title, ssh_key.pub_key)



