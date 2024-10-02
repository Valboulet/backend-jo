import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from backoffice.models import Sport


@pytest.fixture
def api_client():
    """Provides an instance of the API client for making HTTP requests in tests."""
    return APIClient()


@pytest.fixture
def create_sport(db):
    """Fixture to create a sample Sport instance in the database with a pictogram image."""
    pictogram_file = SimpleUploadedFile("test_pictogram.jpg", b"file_content", content_type="image/jpeg")
    return Sport.objects.create(name="Football", pictogram=pictogram_file)


@pytest.mark.django_db
def test_sports_list(api_client, create_sport):
    """Test the sports_list view with one sport."""
    url = reverse('api_sports_list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert 'data' in response.json()
    assert len(response.json()['data']) == 1
    assert response.json()['data'][0]['name'] == create_sport.name
    assert response.json()['data'][0]['pictogram']


@pytest.mark.django_db
def test_sports_list_empty(api_client):
    """Test the sports_list view with no sports in the database."""
    url = reverse('api_sports_list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert 'data' in response.json()
    assert len(response.json()['data']) == 0


@pytest.mark.django_db
def test_sports_list_multiple(api_client):
    """Test the sports_list view with multiple sports."""
    # Create multiple sport instances
    pictogram_file1 = SimpleUploadedFile("test_pictogram1.jpg", b"file_content1", content_type="image/jpeg")
    pictogram_file2 = SimpleUploadedFile("test_pictogram2.jpg", b"file_content2", content_type="image/jpeg")

    sport1 = Sport.objects.create(name="Football", pictogram=pictogram_file1)
    sport2 = Sport.objects.create(name="Basketball", pictogram=pictogram_file2)

    url = reverse('api_sports_list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert 'data' in response.json()
    assert len(response.json()['data']) == 2
    assert response.json()['data'][0]['name'] == sport1.name
    assert response.json()['data'][1]['name'] == sport2.name
    assert response.json()['data'][0]['pictogram']
    assert response.json()['data'][1]['pictogram']
