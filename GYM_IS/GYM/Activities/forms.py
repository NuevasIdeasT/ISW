from django import forms


class Homeform( forms.Form):
    nombre:forms.CharField(required=False)