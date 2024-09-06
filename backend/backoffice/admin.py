from django.contrib import admin

from backoffice.models import User, Customer, UserOffer, Cart, Ticket, Offer, Event


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "number_of_seats", "discount")
    ordering = ("number_of_seats",)


@admin.register(UserOffer)
class UserOfferAdmin(admin.ModelAdmin):
    list_display = ("user", "offer", "is_a_child", "child_discount")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "date_of_birth", "country")
    ordering = ("lastname", "country")


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
