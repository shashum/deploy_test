from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    nickname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "nickname", "password")
    
    def save(self, commit=True):
        user = super(CreateUserForm,self).save(commit=False)
        user.nickname = self.cleaned_data["nickname"]
        
        if commit:
            user.save()
        return user
