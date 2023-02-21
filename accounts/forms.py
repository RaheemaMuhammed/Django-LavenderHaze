from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    

    class Meta:
        model=Account
        fields=['name','email','phone','password']

    
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
