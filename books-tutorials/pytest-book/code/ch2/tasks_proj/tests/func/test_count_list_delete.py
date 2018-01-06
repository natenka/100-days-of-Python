import pytest
import tasks
from tasks import Task


tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))


def test_count_func():
    """Test tasks.count"""
    for t in tasks_to_try:
        tasks.add(t)
    assert tasks.count() == len(tasks_to_try)


def test_list_tasks():
    ids = [tasks.add(t) for t in tasks_to_try]
    list_of_tasks = [tasks.get(tid) for tid in ids]
    assert tasks.list_tasks() == list_of_tasks


def test_delete_task():
    ids = [tasks.add(t) for t in tasks_to_try]
    first_id, *rest = ids
    tasks.delete(first_id)

    all_ids = [t.id for t in tasks.list_tasks()]
    #assert tasks.get(first_id) == None get не работает на удаленном Task
    assert tasks.count() == len(rest)
    assert first_id not in all_ids


def test_delete_all_tasks():
    ids = [tasks.add(t) for t in tasks_to_try]
    tasks.delete_all()
    get_all_tasks = tasks.list_tasks()
    assert len(get_all_tasks) == 0


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

