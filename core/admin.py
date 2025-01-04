from django.contrib import admin
from .models import ServerConfig, GeoBlock
# Register your models here.
admin.site.register(ServerConfig)
admin.site.register(GeoBlock)