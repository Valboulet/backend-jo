from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Spectator, User, SpectatorTicket, Cart, Ticket, Offer, Event, Sport, Location

# Personnalisation de l'interface d'administration
admin.site.site_header = "JO Paris 2024 - Admin"
admin.site.site_title = "JO Paris 2024 - Admin"
admin.site.index_title = "Bienvenue dans votre espace d'administration"


# Configuration de l'administration pour les modèles
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "number_of_seats", "discount")
    ordering = ("number_of_seats",)


@admin.register(Spectator)
class SpectatorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "country")
    ordering = ("last_name", "country")


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


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 0
    readonly_fields = ('buying_key', 'event', 'offer')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False  # Désactiver la possibilité d'ajouter des tickets depuis l'inline

    def has_change_permission(self, request, obj=None):
        return False  # Désactiver la possibilité de modifier les tickets depuis l'inline


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0
    readonly_fields = ('cart_validation_date',)
    can_delete = False
    inlines = [TicketInline]

    def tickets_list(self, obj):
        # Liste tous les tickets associés à la commande avec leurs clés d'achat
        tickets = Ticket.objects.filter(cart=obj)
        if tickets.exists():
            ticket_details = [
                format_html('<li>{} - Clé: {}</li>', ticket.event, ticket.buying_key)
                for ticket in tickets
            ]
            return format_html("<ul>{}</ul>", format_html("".join(ticket_details)))
        else:
            return "Pas de tickets"

    tickets_list.short_description = "Tickets associés"


# Administration du modèle User avec les commandes visibles et cliquables
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', "auth_key")

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("event", "offer", "cart", "buying_key")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_validation_date", "user")
    inlines = [TicketInline]  # Affichage des Tickets associés dans la Cart


@admin.register(SpectatorTicket)
class SpectatorTicketAdmin(admin.ModelAdmin):
    list_display = ('spectator', 'ticket', 'auth_key_display', 'buying_key_display')

    def auth_key_display(self, obj):
        # Vérifier si le Spectator a un User pour accéder à l'auth_key
        return obj.spectator.user.auth_key if hasattr(obj.spectator, 'user') else "N/A"

    def buying_key_display(self, obj):
        return obj.ticket.buying_key

    auth_key_display.short_description = 'Clé d\'authentification'
    buying_key_display.short_description = 'Clé d\'achat'
