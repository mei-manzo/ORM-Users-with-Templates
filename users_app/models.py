from django.db import models


class Users(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email_address = models.TextField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class AddForm(forms.Form):
#     first_name =  forms.CharField(label='first_name', max_length=255)
#     last_name = forms.CharField(label='last_name', max_length=255)
#     email_address = forms.CharField(label='email', max_length=255)
#     age = forms.CharField(label='age', max_length=3)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)