import pytest

from api import create_app, db as _db


@pytest.fixture(scope='module')
def app(request):

    app = create_app('Testing')

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)

    return app


@pytest.fixture(scope='module')
def db(app, request):

    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)

    return _db


@pytest.fixture(scope='function')
def session(db, request):

    connection = db.engine.connect()
    transaction = connection.begin()

    options = {'bind': connection, 'binds': {}}
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)

    return session


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()
