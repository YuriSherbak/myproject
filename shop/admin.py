from django.contrib import admin
from .models import Condition, Category, Thing

# Register your models here.
admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(Thing)
