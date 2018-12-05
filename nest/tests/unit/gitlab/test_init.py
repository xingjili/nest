from unittest import TestCase
from nest.git import init

TOKEN = 'BNa-yecKjyy9tjazMvA6'
HOST = '119.255.249.10'
GROUP = 'dire'
PROJECTS = ['steam', 'germ', 'boot', 'kolla-ansible', 'kubespray']
TITLE = 'boot'
SSH_KEY = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNkgne/UjqIk/agZbRi0b+SN5oWXlSWWKTjXc1wgPFfBPbO/aMbpuasMSWIVQu9etw2ed4vtMoAIQUgxKNcFaofjHbpoYRjJreV2hH6Exd+wegA/fvhm5IVku1KwJWPVmVPeGvfHbNEx/wYwc8XssUeHvuwUiRXPcwXCgx1Z5RaPRwqIaQD9Ojv9UybmYjkaIT0q5jAqC0xKrLquvCa5qiceRBYe7VH8TKH1E/wPc2hn87blGVY7OS4dIwSUow0wevVTcoOV7CHqQaw9sjo+ZKpwcj7Ij9L3eRjkbu6oPvJIbothGVOvtpvkVE9UV1nPfBoARdK9c4HOFv0uBllNmj kolla@ubuntu'


class TestInit(TestCase):
    def test_init(self):
        init.init_dire()
