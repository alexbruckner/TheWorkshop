from django.contrib import admin
from upload.models import UploadModel

class UploadModelAdmin(admin.ModelAdmin):
    fields = ('file',)

admin.site.register(UploadModel, UploadModelAdmin)