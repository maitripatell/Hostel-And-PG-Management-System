from django import forms 
from .models import *
  
class addData(forms.ModelForm): 
  
    class Meta: 
        model = Residence 
        fields = ['residence_name', 'residence_address', 'residence_city', 'residence_state', 'residence_pincode', 'description', 'rent', 'image']