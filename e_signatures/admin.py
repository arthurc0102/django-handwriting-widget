from django.contrib import admin

from .models import Signatures


@admin.register(Signatures)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
