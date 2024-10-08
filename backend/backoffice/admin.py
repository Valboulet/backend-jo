from datetime import datetime
from django.contrib import admin
from .models import User, Customer, UserTicket, Cart, Ticket, Offer, Event, Sport, Location

# Customize admin interface
admin.site.site_header = "JO Paris 2024 - Admin"
admin.site.site_title = "JO Paris 2024 - Admin"
admin.site.index_title = "Bienvenue dans votre espace d'administration"


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "number_of_seats", "discount")
    ordering = ("number_of_seats",)


@admin.register(UserTicket)
class UserTicketAdmin(admin.ModelAdmin):
    list_display = ("user", "ticket")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "date_of_birth", "isAChild", "country")
    ordering = ("lastname", "country")

    def isAChild(self, obj) -> str:
        age = datetime.now().year - obj.date_of_birth.year

        if(age <= 12):
            return "Oui"
        else:
            return "Non"
        
    isAChild.short_description = "Tarif Enfant"


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ("name", "pictogram")
    ordering = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    ordering = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("sport", "location", "start_date", "price")
    ordering = ("start_date",)
    list_filter = ("location", "sport")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "email")
    ordering = ("lastname",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("event", "offer", "cart")


class CartInline(admin.TabularInline):
    model = Ticket
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_validation_date", "user")
    inlines = (CartInline,)
