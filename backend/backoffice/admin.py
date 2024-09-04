from django.contrib import admin

from backoffice.models import User, Customer, UserOffer, Cart, Ticket, Offer, Event

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "number_of_seats", "discount")

@admin.register(UserOffer)
class UserOfferAdmin(admin.ModelAdmin):
    list_display = ("user", "offer", "is_a_child", "child_discount")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "date_of_birth", "country")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_validation_date", "user")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("sport_name", "location", "start_date", "price")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "email")
    # readonly_fields = ("password_display",)

    # def password_display(self, obj):
    #     # Retourner des astérisques pour masquer le mot de passe
    #     return '************'

    # password_display.short_description = 'Mot de passe'

    # # Spécifier les champs à afficher dans le formulaire d'édition
    # fields = ('lastname', 'firstname', 'email', 'phone', 'auth_token', 'password_display')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("event", "offer", "cart")

