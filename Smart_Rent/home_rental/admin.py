from django.contrib import admin
from .models import AddRentalHome, UserInformation


class AddRentalHomeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'city', 'state', 'rent')
    search_fields = ('first_name', 'last_name', 'city')
    prepopulated_fields = {"slug": ("first_name", "last_name")}


admin.site.register(AddRentalHome)


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    pass
