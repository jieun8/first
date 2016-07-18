from django.contrib import admin
from pockemon.models import User, Pockemon
from .forms import PockemonForm


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_level']


class PockemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'po_name', 'po_level', 'catched_by', 'lnglat', 'catched_when']
    form = PockemonForm


admin.site.register(User, UserAdmin)
admin.site.register(Pockemon, PockemonAdmin)