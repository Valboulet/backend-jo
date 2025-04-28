import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
admin.site.index_title = "Bienvenue dans l'espace d'administration des JO de Paris 2024"


# Admin configuration for various models
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """Admin interface for managing event offers."""
    list_display = ("offer_name", "number_of_seats", "discount")
    ordering = ("number_of_seats",)

    def chosen_count_chart(self, obj=None):
        """Génère un graphique montrant le nombre de fois que chaque offre a été choisie dans l'ensemble des tickets."""
        # Obtenir toutes les offres
        offers = Offer.objects.all()

        # Compter le nombre de fois que chaque offre est choisie
        offer_names = []
        offer_counts = []
        for offer in offers:
            offer_names.append(offer.offer_name)
            offer_counts.append(Ticket.objects.filter(offer=offer).count())

        # Créer un graphique avec toutes les offres
        fig, ax = plt.subplots(figsize=(8, 5))  # Ajuster la taille pour afficher toutes les barres
        ax.bar(offer_names, offer_counts, color='skyblue')
        ax.set_title("Nombre de tickets choisis par offre")
        ax.set_ylabel("Nombre de tickets")

        # Convertir le graphique en image PNG
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_data = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        # Afficher l'image dans l'interface admin
        return mark_safe(f'<img src="data:image/png;base64,{img_data}" width="600" />')

    chosen_count_chart.short_description = "Graphique global des choix"

    # Ajouter le graphique dans les actions de l'admin
    readonly_fields = ("chosen_count_chart",)


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




