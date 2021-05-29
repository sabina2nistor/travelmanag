from django.contrib import admin
from mainapp.models import Travel,Destination

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    pass


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass


