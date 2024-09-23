import pytest
from backoffice.models import Offer

"""
This file tests a CRUD on offers objects by creating false datas (check pytest.fixture)
"""

# Fixture to create a dummy offer before the tests
@pytest.fixture
def dummy_offer(db):
    return Offer.objects.create(
        offer_name='Dummy',
        number_of_seats=5,
        discount=0.20
    )

# Test for creating a new offer
def test_create_offer(db):
    nbr_of_offers_before_add = Offer.objects.count()

    # Create a new offer
    new_offer = Offer.objects.create(
        offer_name='Groupe',
        number_of_seats=5,
        discount=0.20
    )

    nbr_of_offers_after_add = Offer.objects.count()

    # Assert that the number of offers has increased by 1
    assert nbr_of_offers_after_add == nbr_of_offers_before_add + 1

# Test for updating an existing offer
def test_update_offer(db, dummy_offer):
    # Verify that the dummy offer has the correct initial name
    assert dummy_offer.offer_name == 'Dummy'

    # Update the offer name
    dummy_offer.offer_name = 'Groupe'
    dummy_offer.save()

    # Retrieve the updated object to verify the change
    updated_offer = Offer.objects.get(pk=dummy_offer.pk)
    assert updated_offer.offer_name == 'Groupe'

# Test for deleting an offer
def test_delete_offer(db, dummy_offer):
    nbr_of_offers_before_delete = Offer.objects.count()

    # Delete the dummy offer
    dummy_offer.delete()

    nbr_of_offers_after_delete = Offer.objects.count()

    # Assert that the number of offers has decreased by 1
    assert nbr_of_offers_after_delete == nbr_of_offers_before_delete - 1