from django import forms
from app.models import *


class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}



class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']