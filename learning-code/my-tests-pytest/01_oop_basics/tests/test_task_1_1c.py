import pytest
from task_1_1c import Topology
import warnings

stdout_incorrect_warning = '''
Сообщение отличается от указанного в задании.
Должно быть: {}
А выведено: {}
'''


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = Topology(topology_with_dupl_links)
    assert getattr(top_with_data, 'topology', None) != None


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method_delete_node(normalized_topology_example, capsys):
    '''Проверка наличия метода delete_node и его работы'''
    norm_top = Topology(normalized_topology_example)
    assert getattr(norm_top, 'delete_node', None) != None
    node = 'SW1'

    delete_node_result = norm_top.delete_node(node)
    assert delete_node_result == None, 'Метод delete_node не должен ничего возвращать'

    ports_with_node = [src for src, dst in norm_top.topology.items()
                       if node in src or node in dst]
    assert len(ports_with_node) == 0
    assert len(norm_top.topology) == 3

    #проверка удаления несуществующего устройства
    norm_top.delete_node(node)
    out, err = capsys.readouterr()
    node_msg = 'Такого устройства нет\n'
    if not out == node_msg:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(node_msg, out)))

