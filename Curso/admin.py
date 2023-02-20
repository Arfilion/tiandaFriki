from django.contrib import admin
from .models import cartas, videoJuegos, Peliculas, miniaturas
# Register your models here.
admin.site.register(videoJuegos)
admin.site.register(miniaturas)
admin.site.register(cartas)
admin.site.register(Peliculas)