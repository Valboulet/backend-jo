import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from .utils import convertToParisTZ


class Offer(models.Model):
    """
    The Offer table containing all offers items
    """
    id_offer = models.SmallAutoField(primary_key=True, null=False)
    offer_name = models.CharField(max_length=10, null=False, verbose_name="Nom de l'offre")
    number_of_seats = models.SmallIntegerField(null=False, verbose_name="Nombre de places",
                                               validators=[MinValueValidator(1), 
                                                           MaxValueValidator(10)])
    discount = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name="Réduction", validators=[MinValueValidator(0)])

    class Meta:
        verbose_name ="Offre"
        verbose_name_plural ="Offres"

    def __str__(self) -> str:
        return f'{self.offer_name}'


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Vous devez spécifier une adresse e-mail valide")
        

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)



class Spectator(models.Model):
    id_spectator = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=False, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Nom")
    date_of_birth = models.DateField(null=False, verbose_name="Date de naissance")
    country = models.CharField(max_length=75, null=False, verbose_name="Pays")

    class Meta:
        verbose_name ="Spectateur"
        verbose_name_plural ="Spectateurs"

    def __str__(self) -> str: 
        return f'{self.last_name} {self.first_name}'
    


class User(AbstractBaseUser, PermissionsMixin):
    """
    The User table contains customers
    """
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=100, null=False, verbose_name="E-mail")
    first_name = models.CharField(max_length=50, null=False, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Nom")
    auth_key = models.UUIDField(default=uuid.uuid4, verbose_name="Clé d'authentification")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now, null=False, verbose_name='Date de création')
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    class Meta:
        verbose_name ="Client"
        verbose_name_plural ="Clients"



class Cart(models.Model):
    """
    The Cart table contains tickets
    """
    id_cart = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_validation_date = models.DateTimeField(null=False, auto_now_add=True, verbose_name="Date d'achat")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="Client")

    class Meta:
        verbose_name ="Commande"
        verbose_name_plural ="Commandes"

    def __str__(self) -> str:
        date_purchase = convertToParisTZ(self.cart_validation_date).strftime("%d/%m/%Y | %H:%M:%S")
        return f'{self.user} | {date_purchase}'    
    


class Sport(models.Model):
    id_sport = models.SmallAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=30, null=False, verbose_name="Sport")
    pictogram = models.ImageField(upload_to='uploads/sports', verbose_name='Image')

    class Meta:
        verbose_name ="Sport"
        verbose_name_plural ="Sports"

    def __str__(self) -> str:
        return f'{self.name}'

    def pictogram_url(self):
        """
        This function returns the pictogram URL concatenated with the website URL in settings.base.py
        """
        return f'{settings.WEBSITE_URL}{self.pictogram.url}'
    

class Location(models.Model):
    id_location = models.SmallAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False, verbose_name="Lieu")
    image = models.ImageField(upload_to='uploads/locations', verbose_name='Image')

    class Meta:
        verbose_name ="Lieu"
        verbose_name_plural ="Lieux"

    def __str__(self) -> str:
        return f'{self.name}'
    
    def image_url(self):
        """
        This function returns the image URL concatenated with the website URL in settings.base.py
        """
        return f'{settings.WEBSITE_URL}{self.image.url}'




class Event(models.Model):
    id_event = models.SmallAutoField(primary_key=True, null=False)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False, verbose_name="Sport")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, verbose_name="Lieu")
    start_date = models.DateTimeField(null=False, verbose_name="Date de début")
    end_date = models.DateTimeField(null=False, verbose_name="Date de fin")
    description = models.CharField(max_length=250, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, verbose_name="Tarif", validators=[MinValueValidator(0)])
                    
    class Meta:
        verbose_name ="Évènement"
        verbose_name_plural ="Évènements"

    def __str__(self) -> str:
        date_start = convertToParisTZ(self.start_date).strftime("%d/%m/%Y | %H:%M")
        date_end = convertToParisTZ(self.end_date).strftime("%H:%M")
        return f'{(self.sport)} | {date_start} - {date_end}'
    

    """
    Theses functions return the start and end formated to show in API
    """
    def date_start(self):
        return f'{convertToParisTZ(self.start_date).strftime("%d/%m/%Y | %H:%M")}'

    def date_end(self):
        return f'{convertToParisTZ(self.end_date).strftime("%H:%M")}'
    


class Ticket(models.Model):
    id_ticket = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False, verbose_name="Commande")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, verbose_name="Épreuve")
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=False, verbose_name="Offre")
    buying_key = models.UUIDField(default=uuid.uuid4, verbose_name="Clé d'achat")

    class Meta:
        verbose_name ="Ticket"
        verbose_name_plural ="Tickets"

    def __str__(self) -> str:
        return f'{self.cart} | {self.event}'



class SpectatorTicket(models.Model):
    """
    The SpectatorTicket table is an association table between Spectator and Ticket
    """
    id_spectator_ticket = models.SmallAutoField(primary_key=True, null=False)
    spectator = models.ForeignKey(Spectator, on_delete=models.CASCADE, null=False, verbose_name="Utilisateur")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null =False, verbose_name="Ticket")

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['spectator', 'ticket'], name='unique_spectator_ticket')
        ]
        verbose_name ="Spectateur | Ticket"
        verbose_name_plural ="Spectateurs | Tickets"

    def __str__(self) -> str:
        return f'{self.ticket}'
