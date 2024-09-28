import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from backoffice.models import Sport


@pytest.fixture
def api_client():
    """
    Provides an instance of the API client for making HTTP requests in tests.
    This client simulates a web browser, allowing for interaction with the API endpoints.
    """
    return APIClient()


@pytest.fixture
def create_sport(db):
    """
    Fixture to create a sample Sport instance in the database with a pictogram image.
    This instance will be available for tests requiring a Sport object.
    """
    # Create a simulated pictogram image file
    pictogram_file = SimpleUploadedFile("test_pictogram.jpg", b"file_content", content_type="image/jpeg")
    return Sport.objects.create(name="Football", pictogram=pictogram_file)


@pytest.mark.django_db
def test_sports_list(api_client, create_sport):
    """
    Test the sports_list view.
    
    This test verifies that the sports_list API endpoint returns a 200 OK status code,
    includes a 'data' key in the response, and that the response contains the correct
    number of sports along with their names and pictograms.
    """
    url = reverse('api_sports_list')
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert 'data' in response.json()
    assert len(response.json()['data']) == 1 
    assert response.json()['data'][0]['name'] == create_sport.name
    assert response.json()['data'][0]['pictogram']

