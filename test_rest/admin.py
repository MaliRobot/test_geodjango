from django.contrib import admin

from .models import User_geos
from .models import Geos
from .models import Geom
from .models import User

# Register your models here.
admin.site.register(User_geos)
admin.site.register(Geos)
admin.site.register(Geom)
admin.site.register(User)