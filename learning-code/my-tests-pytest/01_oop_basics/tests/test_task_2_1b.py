import pytest
import clitable
from task_2_1b import CiscoSSH



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


def test_method_send_show_command(ssh_r1):
    netmiko_send_command = ssh_r1.ssh.send_command('sh ip int br')
    assert getattr(ssh_r1, 'send_show_command', None) != None
    assert netmiko_send_command == ssh_r1.send_show_command('sh ip int br')


def test_method_send_and_parse_show(ssh_r1):
    command = 'sh ip int br'
    command_out = ssh_r1.ssh.send_command(command)
    assert getattr(ssh_r1, 'send_and_parse_show', None) != None
    assert send_and_parse(command, command_out) == ssh_r1.send_and_parse_show(command)


