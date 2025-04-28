from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
# import stripe
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import redirect

# import os
# from dotenv import load_dotenv

# load_dotenv()

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer



# stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

# class StripeCheckoutView(APIView):
#     def post(self, request):
#         try:
#             checkout_session = stripe.checkout.Session.create(
#                 line_items=[
#                     {
#                         'price': 'prod_REETHEouAvhjfI',
#                         'quantity': 1,
#                     },
#                 ],
#                 mode='payment',
#                 success_url=os.environ.get("FRONT_SITE_URL") + '/payment/success?success=true&session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=os.environ.get("FRONT_SITE_URL") + '/payment/canceled?canceled=true',
#             )

#             return redirect(checkout_session.url)
#         except:
#             return