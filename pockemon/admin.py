from django.contrib import admin
from pockemon.models import User, Pockemon, Region, Capture
from .forms import PockemonForm


class CaptureInline(admin.TabularInline):
    model = Capture
    extra = 2


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_level']
    inlines = [CaptureInline]


class PockemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'po_name', 'po_level']
    form = PockemonForm
    inlines = [CaptureInline]


class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [CaptureInline]


#class CaptureAdmin(admin.ModelAdmin):
#    list_display = ['id', 'user', 'pockemon', 'region']

admin.site.register(User, UserAdmin)
admin.site.register(Pockemon, PockemonAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Capture)