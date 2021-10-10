from django.contrib import admin

# Register your models here.
from .models import Post , Category
from import_export.admin import ImportExportModelAdmin


admin.site.register(Category)
@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass



# admin.site.register(Post)
