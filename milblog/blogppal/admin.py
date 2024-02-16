from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo_post", "slug", "autor", "publicado", "status"]
    list_filter = ["status", "creado", "publicado", "autor"]
    search_fields = ["titulo_post", "cuerpo_post"]
    prepopulated_fields = {"slug": ("titulo_post",)}
    raw_id_fields = ["autor"]
    date_hierarchy = "publicado"
    ordering = ["status", "publicado"]
