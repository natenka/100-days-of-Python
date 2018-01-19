import pytest
from task_3_1a import CiscoSSH
import warnings

stdout_incorrect_warning = '''
Сообщение отличается от указанного в задании.
Должно быть: {}
А выведено: {}
'''


def test_class_creation_attr_ssh(ssh_r1):
    '''Проверка создания класса, атрибута ssh и метода send_show_command'''
    assert getattr(ssh_r1, 'ssh', None) != None
    assert ssh_r1.ssh.check_enable_mode()


def test_method__str__(ssh_r1, capsys):
    assert getattr(ssh_r1, '__str__', None) != None
    print(ssh_r1)
    out, err = capsys.readouterr()
    str_repr = 'CiscoSSH connection to 192.168.100.1\n'
    if not out == str_repr:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(str_repr, out)))

