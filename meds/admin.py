from django.contrib import admin

from .models import Perscription, Log


@admin.register(Perscription)
class PerscriptionAdmin(admin.ModelAdmin):
    """Perscription admin."""

    model = Perscription
    list_display = ("name", "dosage", "interval", "created_at", "updated_at")


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """Log admin."""

    model = Log
    list_display = ("perscription", "taken", "created_at", "updated_at")
