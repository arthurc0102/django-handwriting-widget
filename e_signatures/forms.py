from django import forms

from handwriting.forms import HandwritingPad

from .models import Signature


class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = '__all__'
        widgets = {
            'image': HandwritingPad(),
            'image_no_required': HandwritingPad(),
        }
