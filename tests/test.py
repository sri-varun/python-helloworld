# test_sample.py
import pytest
from index import highlow
import json

@pytest.fixture()
def app():
    app = highlow()
    

@pytest.fixture()
def client(app):
    return app


def test_highlow(client):
    headers = {
        'Content-Type':  'application/json',
        'Accept':  'application/json'
    }
    data1 = {'value':100}
    url = '/highlow'
    response = client.post(url, data=json.dumps(data1),headers=headers)



