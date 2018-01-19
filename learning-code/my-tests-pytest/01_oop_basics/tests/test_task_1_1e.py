import pytest
from task_1_1e import Topology


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = Topology(topology_with_dupl_links)
    assert getattr(top_with_data, 'topology', None) != None


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method__add__(normalized_topology_example):
    '''Проверка наличия метода __add__ и его работы'''
    top1 = Topology(normalized_topology_example)
    assert getattr(top1, '__add__', None) != None

    top2 = Topology({('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                     ('R1', 'Eth0/6'): ('R9', 'Eth0/0')})
    top3 = top1 + top2
    assert isinstance(top3, Topology), 'Метод __add__ должен возвращать новый экземпляр класса Topology'
    assert len(top3.topology) == 8

