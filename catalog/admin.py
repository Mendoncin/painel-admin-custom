from django.contrib import admin
from catalog.models import LiteraryFormat, Book, Author
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ["title", "price", "format"]
  list_filter = ["format"]
  search_fields = ["title"]

@admin.register(Author)
class AuthorAdmin(UserAdmin):
  list_display = UserAdmin.list_display + ("psedonimo", )
  fieldsets = UserAdmin.fieldsets + (("Informações Adicionais", {"fields": ("psedonimo", )}), )
  add_fieldsets = UserAdmin.add_fieldsets + (("Informações Adicionais", {"fields": ("psedonimo", "first_name", "last_name" )}), )

admin.site.register(LiteraryFormat)
