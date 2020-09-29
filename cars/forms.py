from django import forms
from cars.models import Make,Cars

class MakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'        
