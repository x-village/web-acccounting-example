import pytest

from app import app as _app
from app import db
from models import Record


@pytest.fixture
def app():
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_for_testing.db'
    db.drop_all()
    db.create_all()
    return _app


def test_add_record(client, accept_json):
    resp = client.post(
        '/record',
        headers=accept_json,
        data={
            'name': 'test_record',
            'cost': 100
        }
    )
    assert resp.status_code == 200
    assert resp.data.decode('utf-8') == 'Create Succeeded'

    test_record = Record.query.filter_by(name='test_record').first()
    assert test_record.name == 'test_record'
    assert test_record.cost == 100
