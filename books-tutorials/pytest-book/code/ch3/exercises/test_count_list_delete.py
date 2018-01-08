import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_for_same_user():
    return (Task('sleep', 'brian', done=True),
            Task('wake', 'brian'),
            Task('breathe', 'brian', True),
            Task('exercise', 'brian', False))


@pytest.fixture()
def db_with_4_tasks(tasks_db, tasks_for_same_user):
    for t in tasks_for_same_user:
        tasks.add(t)


@pytest.fixture()
def db_with_4_tasks_id_returned(tasks_db, tasks_for_same_user):
    id_task_mapping = {}
    for t in tasks_for_same_user:
        tid = tasks.add(t)
        id_task_mapping[tid] = t
    yield id_task_mapping
    tasks.delete_all()


@pytest.fixture(autouse=True, scope='module')
def initialized_db_session(tmpdir_factory):
    """Connect to db before testing, disconnect after."""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(initialized_db_session):
    """An empty tasks db."""
    tasks.delete_all()


def test_count_func(tasks_db, db_with_4_tasks):
    """Test tasks.count"""
    assert tasks.count() == 4


def test_list_tasks(db_with_4_tasks_id_returned):
    ids = db_with_4_tasks_id_returned.keys()
    list_of_tasks = [tasks.get(tid) for tid in ids]
    assert tasks.list_tasks() == list_of_tasks


def test_delete_task(db_with_4_tasks_id_returned):
    ids = db_with_4_tasks_id_returned.keys()
    first_id, *rest = ids
    tasks.delete(first_id)

    all_ids = [t.id for t in tasks.list_tasks()]
    assert tasks.count() == len(rest)
    assert first_id not in all_ids


def test_delete_all_tasks(db_with_4_tasks):
    tasks.delete_all()
    get_all_tasks = tasks.list_tasks()
    assert len(get_all_tasks) == 0


