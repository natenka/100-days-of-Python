import pytest
from task_2_1a import CiscoSSH


def test_class_creation_attr_ssh(ssh_r1):
    '''Проверка создания класса, атрибута ssh и метода send_show_command'''
    assert getattr(ssh_r1, 'ssh', None) != None
    assert ssh_r1.ssh.check_enable_mode()


def test_method_send_show_command(ssh_r1):
    netmiko_send_command = ssh_r1.ssh.send_command('sh ip int br')
    assert getattr(ssh_r1, 'send_show_command', None) != None
    assert netmiko_send_command == ssh_r1.send_show_command('sh ip int br')

