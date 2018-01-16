import pytest


@pytest.fixture()
def topology_with_dupl_links():
    topology = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
    return topology


@pytest.fixture()
def normalized_topology_example():
    normalized_topology = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                           ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                           ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                           ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                           ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                           ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    return normalized_topology

