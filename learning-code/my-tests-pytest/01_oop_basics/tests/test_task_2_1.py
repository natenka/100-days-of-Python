import pytest
from task_2_1 import CiscoSSH



def test_class_creation_attr_ssh(ssh_r1):
    '''Проверка создания класса и атрибута ssh '''
    assert getattr(ssh_r1, 'ssh', None) != None
    assert ssh_r1.ssh.check_enable_mode()
    assert ssh_r1.ssh.send_command('sh ip int br')


