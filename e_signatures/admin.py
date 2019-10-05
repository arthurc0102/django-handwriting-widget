from django.contrib import admin

from .forms import SignatureForm
from .models import Signature


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    form = SignatureForm
    list_display = ('name', 'create_at')
