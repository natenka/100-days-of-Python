import pytest
import clitable
from task_2_1c import CiscoSSH


def send_and_parse(command, command_output,
                   index_file='index', templates='templates'):
    attributes = {'Command': command,
                  'Vendor': 'cisco_ios'}
    cli_table = clitable.CliTable(index_file, templates)
    cli_table.ParseCmd(command_output, attributes)
    return [dict(zip(cli_table.header, row)) for row in cli_table]


def test_class_creation_attr_ssh(ssh_r1):
    '''Проверка создания класса, атрибута ssh и метода send_show_command'''
    assert getattr(ssh_r1, 'ssh', None) != None
    assert ssh_r1.ssh.check_enable_mode()


def test_method_send_cfg_commands(ssh_r1):
    cfg_command = 'logging 10.1.1.1'
    netmiko_send_cfg_set = ssh_r1.ssh.send_config_set(cfg_command)
    assert getattr(ssh_r1, 'send_cfg_commands', None) != None
    assert netmiko_send_cfg_set == ssh_r1.send_cfg_commands(cfg_command)


