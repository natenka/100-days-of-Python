import pytest
import clitable
from task_2_1d import CiscoSSH


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
    commands_with_errors = sorted(['logging 0255.255.1', 'logging', 'i'])
    correct_commands = sorted(['logging buffered 20010', 'ip http server'])
    commands = commands_with_errors+correct_commands

    assert getattr(ssh_r1, 'send_cfg_commands', None) != None

    correct, failed = ssh_r1.send_cfg_commands(commands)
    assert sorted(correct.keys()) == correct_commands
    assert sorted(failed.keys()) == commands_with_errors


