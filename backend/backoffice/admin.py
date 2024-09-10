from datetime import datetime
from django.contrib import admin
from .models import User, Customer, UserOffer, Cart, Ticket, Offer, Event

# Customize admin interface
admin.site.site_header = "JO Paris 2024 - Admin"
admin.site.site_title = "JO Paris 2024 - Admin"
admin.site.index_title = "Bienvenue dans votre espace d'administration"


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "number_of_seats", "discount")
    ordering = ("number_of_seats",)


@admin.register(UserOffer)
class UserOfferAdmin(admin.ModelAdmin):
    list_display = ("user", "offer", "child_discount")


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


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("sport_name", "location", "start_date", "price")
    ordering = ("start_date",)
    list_filter = ("location", "sport_name")


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
