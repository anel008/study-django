from django import forms 
from  .models import Product


class Modeform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','disc','img']
