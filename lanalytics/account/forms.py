from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=128,
        widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationException(_(''))

        return password_confirm

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password', 'password_confirm', 'email', )
