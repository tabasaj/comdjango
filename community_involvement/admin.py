from django.contrib import admin
from .models import image


class images(admin.ModelAdmin):
    model = image
    list_display = ('description', 'time', 'image')

admin.site.register(image, images)

# Register your models here.
