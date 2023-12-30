from django import forms
from django.core.exceptions import ValidationError

from .models import ClientUserModel

class ClientCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = ClientUserModel
        fields = ['email', 'mobile']
        labels = {
            'email': 'Էլեկտրոնային փոստի հասցե', # 'Էլ.փոստի հասցե',  
            'mobile': 'Բջջային հեռախոսահամար, որով կազմակերպիչները կարող են կապվել ձեզ հետ'
        }

    password1 = forms.CharField(label="Գաղտնաբառ", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Գաղտնաբառի հաստատում", widget=forms.PasswordInput,
        empty_value="Կրկնեք ձեր գաղտնաբառը"
    )

    def __init__(self, *args, **kwargs):
        super(ClientCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-2'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Գաղտնաբառերը չեն համընկնում")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
