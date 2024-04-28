from django.contrib import admin
from .models import UserProfile
from .models import Event
from .models import Venue
from .models import Categorie
from .models import Role
from .models import EventApplication
from .models import Department
# Register your models here.

admin.site.register(Venue)
admin.site.register(Categorie)
admin.site.register(Role)
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(EventApplication)
admin.site.register(Department)


