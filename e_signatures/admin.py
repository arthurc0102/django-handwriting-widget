from django.contrib import admin

from handwriting.admin import HandwritingPadModelAdmin

from .models import Signatures


@admin.register(Signatures)
class SignatureAdmin(HandwritingPadModelAdmin):
    list_display = ('name', 'create_at')
