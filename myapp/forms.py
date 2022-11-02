from  django import forms

from myapp.models import Profile

class Registration(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ['username', 'id_user', 'profileImg']
        
        
