from django.contrib import admin

from .models import Contest, Team, Participant, HandleInvoice

# Register your models here.

admin.site.register(Contest)
admin.site.register(Team)
admin.site.register(Participant)
admin.site.register(HandleInvoice)
