from django.contrib import admin

# Register your models here.
from guest_app.models import Event,Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','start_time','id']
    search_fields = ['name']
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name','phone','email','sign','create_time','event']
    search_fields = ['real_name']
    list_filter = ['sign']


admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)