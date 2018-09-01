from django.contrib import admin
from .models import Ticket, Location


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'violation', 'plate_number', 'location', 'user', 'get_city']


admin.site.register(Ticket)
