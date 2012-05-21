from django.db import models
from django import forms

#http://www.allbuttonspressed.com/projects/django-filetransfers
class UploadModel(models.Model):
#    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    file = models.FileField(upload_to='uploaded')

    def __str__(self):
        return str(self.file)

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
