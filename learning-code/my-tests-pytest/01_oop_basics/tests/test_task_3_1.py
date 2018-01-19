import pytest
from task_3_1 import CiscoSSH
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


def test_method__del__(ssh_r1, capsys):
    assert getattr(ssh_r1, '__del__', None) != None
    del ssh_r1
    out, err = capsys.readouterr()
    disconnect_msg = 'Соединение разорвано\n'
    if not out == disconnect_msg:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(disconnect_msg, out)))

