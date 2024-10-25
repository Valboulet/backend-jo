import base64
from io import BytesIO

import qrcode
from django.contrib import admin
from django.utils.html import mark_safe

from .models import (
    Cart,
    Event,
    Location,
    Offer,
    Spectator,
    SpectatorTicket,
    Sport,
    Ticket,
    User,
)

# Customizing the admin interface
admin.site.site_header = "JO Paris 2024 - Admin"
admin.site.site_title = "JO Paris 2024 - Admin"
admin.site.index_title = "Welcome to the Admin Dashboard"


# Admin configuration for various models
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """Admin interface for managing event offers."""
    list_display = ("offer_name", "number_of_seats", "discount")
    ordering = ("number_of_seats",)


@admin.register(Spectator)
class SpectatorAdmin(admin.ModelAdmin):
    """Admin interface for managing spectators."""
    list_display = ("last_name", "first_name", "date_of_birth", "country")
    ordering = ("last_name", "country")


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    """Admin interface for managing sports."""
    list_display = ("name", "pictogram")
    ordering = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Admin interface for managing locations."""
    list_display = ("name", "image")
    ordering = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin interface for managing events."""
    list_display = ("sport", "location", "start_date", "price")
    ordering = ("start_date",)
    list_filter = ("location", "sport")


class TicketInline(admin.TabularInline):
    """Inline admin interface for managing tickets within a cart."""
    model = Ticket
    extra = 0
    readonly_fields = ('event', 'offer',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    

class CartInline(admin.TabularInline):
    """Inline admin interface for managing carts."""
    model = Cart
    extra = 0
    readonly_fields = ('cart_validation_date',)
    can_delete = False
    inlines = [TicketInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for managing users."""
    list_display = ('email', 'first_name', 'last_name', 'auth_key')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """Admin interface for managing tickets."""
    list_display = ("event", "offer", "cart", "buying_key", "qr_code_display")

    def qr_code_display(self, obj):
        # Retrieves the user associated with the ticket's cart
        user = obj.cart.user

        # Checks that the auth_key and buying_key are available
        if not user.auth_key or not obj.buying_key:
            return "Keys missing"

        # Concatenates auth_key and buying_key to create the QR code content
        combined_key = f"{user.auth_key}-{obj.buying_key}"

        # Generates the QR code for the combined key
        qr = qrcode.make(combined_key)
        buffered = BytesIO()
        qr.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # Returns the base64-encoded image for display in the admin interface
        return mark_safe(f'<img src="data:image/png;base64,{img_str}" width="100" height="100" />')

    qr_code_display.short_description = 'QR Code'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Admin interface for managing carts."""
    list_display = ("cart_validation_date", "user")
    inlines = [TicketInline]




