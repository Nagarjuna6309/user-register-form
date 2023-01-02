from django import forms

from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'email':'valid email enter'}
class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']