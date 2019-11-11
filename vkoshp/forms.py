from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Participant


class AddParticipantHandleForm(forms.Form):
    participant = forms.ModelChoiceField(
        queryset=Participant.objects.all(), label="Участник"
    )

    handle = forms.CharField(label="Хендл")

    def clean_participant(self):
        participant = self.cleaned_data["participant"]
        if not participant:
            raise ValidationError(_("Invalid participant"))

        return participant

    def clean_handle(self):
        handle = self.cleaned_data["handle"]

        return handle


class UrlForm(forms.Form):
    url = forms.CharField(label="URL")


class FileForm(forms.Form):
    file = forms.FileField()
