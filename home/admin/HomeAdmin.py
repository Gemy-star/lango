from django.contrib import admin
from ..models import HomePage


class HomeAdmin(admin.ModelAdmin):
    pass


admin.site.register(HomePage, HomeAdmin)
