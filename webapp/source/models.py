from django import forms
from django.db import models
from django.contrib import admin

# Create your models here.

class Source(models.Model):

    user = models.CharField(max_length=50)
    source = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.source

class SourceForm(forms.ModelForm):
    source = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Source

class SourceAdmin(admin.ModelAdmin):
    form = SourceForm

admin.site.register(Source, SourceAdmin)
