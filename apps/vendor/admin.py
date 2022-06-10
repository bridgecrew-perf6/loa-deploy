from django.contrib import admin

from .models import Info
from .models import Vendor

admin.site.register(Vendor)

admin.site.register(Info)