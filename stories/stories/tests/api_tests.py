import pytest
from rest_framework.test import RequestsClient

def test_api_list_stories():
    factory = RequestsClient()
    response = factory.get('/list-stories/')

    assert response.status_code == 200

def test_api_add_story():
    factory = RequestsClient()
    response = factory.get('/add-story/')

    assert response.status_code == 200

@pytest.mark.skip()
def test_api_get_story():
    # arrange
    # add mock story in database
    factory = RequestsClient()

    # act
    response = factory.get('/story/?story_id=1')

    # assert
    assert response.status_code == 200