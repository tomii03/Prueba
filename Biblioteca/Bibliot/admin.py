from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    fieldset = (('Datos',{'fields ' :('nombre', 'ejemplares')}), ('Contacto', {'fields': ('telefono' , 'direccion')}))

@admin.register(Libro)
class LibroAdmin (admin.ModelAdmin):
    list_display = ['titulo' , 'editorial']

@admin.register(Ejemplar)
class EjemplarAdmin (admin.ModelAdmin):
    list_display = ['libro', 'localiz']
    list_display_links = ('localiz', 'libro')
    search_fields = ['libro_titulo']

class LibroInline(admin.TabularInline):
    model = Libro
    fields = ['titulo' , 'editorial' , 'paginas']

@admin.register(Autor)
class AutorAdmin (admin.ModelAdmin):
    list_display = ['nombre']
    list_display_links = ('nombre',)
    search_fields = ['nombre']
    inlines = [LibroInline]