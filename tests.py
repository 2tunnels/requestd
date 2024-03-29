from aiohttp.test_utils import TestClient

from requestd import create_application


async def test_get_request(aiohttp_client):
    client: TestClient = await aiohttp_client(create_application())
    response = await client.get('/api/users?order_by=date_created')

    assert response.status == 200
    assert await response.json() == {
        'method': 'GET',
        'version': [1, 1],
        'host': f'{client.server.host}:{client.server.port}',
        'path': '/api/users',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': f'{client.server.host}:{client.server.port}',
            'User-Agent': 'Python/3.8 aiohttp/3.6.2',
        },
        'query': {
            'order_by': 'date_created',
        },
        'body': None,
        'post': None,
        'json': None,
    }


async def test_post_request(aiohttp_client):
    client: TestClient = await aiohttp_client(create_application())
    response = await client.post('/api/users', data={
        'username': 'john',
        'password': 'qwerty',
    })

    assert response.status == 200
    assert await response.json() == {
        'method': 'POST',
        'version': [1, 1],
        'host': f'{client.server.host}:{client.server.port}',
        'path': '/api/users',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '29',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': f'{client.server.host}:{client.server.port}',
            'User-Agent': 'Python/3.8 aiohttp/3.6.2',
        },
        'query': None,
        'body': 'username=john&password=qwerty',
        'post': {
            'username': 'john',
            'password': 'qwerty',
        },
        'json': None,
    }


async def test_json_put_request(aiohttp_client):
    client: TestClient = await aiohttp_client(create_application())
    response = await client.put('/api/users/1', json={
        'username': 'bill',
    }, headers={
        'X-Api-Key': 'secret',
    })

    assert response.status == 200
    assert await response.json() == {
        'method': 'PUT',
        'version': [1, 1],
        'host': f'{client.server.host}:{client.server.port}',
        'path': '/api/users/1',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '20',
            'Content-Type': 'application/json',
            'Host': f'{client.server.host}:{client.server.port}',
            'User-Agent': 'Python/3.8 aiohttp/3.6.2',
            'X-Api-Key': 'secret'
        },
        'query': None,
        'body': '{"username": "bill"}',
        'post': None,
        'json': {
            'username': 'bill',
        },
    }
