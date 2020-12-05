from django import forms
from .models import UserPicture
class ProfilePicForm(forms.ModelForm):
      class Meta:
            model = UserPicture
            fields=['picture']
