from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Contest, Team, Participant, HandleInvoice

# Register your models here.
class ParticipantAdmin(UserAdmin):
	model = Participant
	list_display = ('team', 'name', 'medal', 'codeforces_handle')
	search_fields = ('name','codeforces_handle',)
	readonly_fields = ()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ()

admin.site.register(Contest)
admin.site.register(Team)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(HandleInvoice)
