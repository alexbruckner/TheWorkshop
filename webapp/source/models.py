from django import forms
from django.db import models
from django.contrib import admin

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class UserForm(forms.ModelForm):
    class Meta:
        model = User

class UserAdmin(admin.ModelAdmin):
    form = UserForm

admin.site.register(User, UserAdmin)


class Source(models.Model):

    user = models.ForeignKey(User)
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


