import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class Offer(models.Model):
    id_offer = models.SmallAutoField(primary_key=True, null=False)
    offer_name = models.CharField(max_length=10, null=False)
    number_of_seats = models.SmallIntegerField(null=False,
                                               validators=[MinValueValidator(1), 
                                                           MaxValueValidator(10)])
    discount = models.DecimalField(max_digits=4, decimal_places=2, null=False, validators=[MinValueValidator(0)])
                                

    def __str__(self) -> str:
        return f'{self.offer_name}'
    

class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=False)
    country = models.CharField(max_length=75, null=False)

    def __str__(self) -> str: 
        return f'{self.lastname} {self.firstname}'
    

class Customer(User):
    email = models.EmailField(unique=True, max_length=100, null=False)
    password = models.CharField(max_length=50, null=False)
    phone = PhoneNumberField()
    auth_token = models.CharField(unique=True, max_length=250, null=False)

    def __str__(self) -> str:
        return f'{self.email}'


class Cart(models.Model):
    id_cart = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_validation_date = models.DateTimeField(null=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return f'{self.cart_validation_date}'
    

class UserOffer(models.Model):
    id_user_offer = models.SmallAutoField(primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null =False)
    is_a_child = models.BooleanField(default=False)
    child_discount = models.DecimalField(max_digits=4, decimal_places=2, null=False, validators=[MinValueValidator(0)])

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['user', 'offer'], name='unique_user_offer')
        ]


class Event(models.Model):
    id_event = models.SmallAutoField(primary_key=True, null=False)
    sport_name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=50, null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    description = models.CharField(max_length=250, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, validators=[MinValueValidator(0)])                       

    def __str__(self) -> str:
        return f'{self.sport_name}'
    
    
class Ticket(models.Model):
    id_ticket = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buying_token = models.CharField(unique=True, max_length=250, null=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return f'{self.id_ticket}'

