import pytest
from app import app

@pytest.fixture
def client():
  with app.test.client() as client:
    return client



def test_string(client):
  response = client.get('/page',query_string={'name': 'DHRUV'})
  assert "Hey" == "Hey"


def test_string1():
  assert "Hey" == "Hey"


def test_string2():
  assert "Hey" == "Hey"
