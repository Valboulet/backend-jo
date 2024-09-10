from django.test import TestCase
from .models import Offer

class OfferTestCase(TestCase):

    DUMMY_OFFER_NAME = 'Dummy'

    # Create a setup with false datas to run tests (compare, etc)
    def setUp(self):
        self.offerTestElement = Offer()
        self.offerTestElement.offer_name = self.DUMMY_OFFER_NAME
        self.offerTestElement.number_of_seats = 5
        self.offerTestElement.discount = 0.20
        self.offerTestElement.save()


    def test_create_offer(self):

        nbr_of_offers_before_add = Offer.objects.count()
        # See how many offers exist in the DB

        new_offer = Offer()
        # Add an object (Offer) in the DB
        new_offer.offer_name = 'Groupe'
        new_offer.number_of_seats = 5
        new_offer.discount = 0.20
        new_offer.save()

        # Make sure the number of objects has been incremented by 1
        nbr_of_offers_after_add = Offer.objects.count()
        self.assertTrue(nbr_of_offers_after_add == nbr_of_offers_before_add +1)


    def test_update_offer(self):

        # Check if the dummy offer name and the offer name are the same
        self.assertEqual(self.offerTestElement.offer_name, self.DUMMY_OFFER_NAME)

        self.offerTestElement.offer_name = 'Groupe'
        self.offerTestElement.save()

        # Create a temp variable to contain the object to compare
        tempOfferElement = Offer.objects.get(pk=self.offerTestElement.pk)

        self.assertEqual(tempOfferElement.offer_name, 'Groupe')


    def test_delete_offer(self):

        # Check if the number of offers has been decremented by 1
        nbr_of_offers_before_delete = Offer.objects.count()
        self.offerTestElement.delete()
        nbr_of_offers_after_delete = Offer.objects.count()
        self.assertTrue(nbr_of_offers_after_delete == nbr_of_offers_before_delete - 1)

