from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class ChangePasswordForm(forms.ModelForm):
    current_password = forms.CharField(max_length=128,
        widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=128,
        widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=128,
        widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data['new_password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError(_('Password should match'))

        return password_confirm

    def clean_current_password(self):
        password = self.cleaned_data['current_password']
        try:
            social_auth = self.instance.social_auth.all()[0]
            if self.instance.password == '!' and social_auth.provider != '':
                # We can skip password check if auth provider available
                return password
            raise IndexError("Checking password if it's already filled")
        except IndexError:
            if not self.instance.check_password(password):
                raise forms.ValidationError(\
                        _('Please, enter valid current password'))
        return password

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        try:
            social_auth = self.instance.social_auth.all()[0]
            if self.instance.password == '!' and social_auth.provider != '':
                self.fields['current_password'].widget = forms.HiddenInput()
                self.fields['current_password'].required = False

        except IndexError:
            pass
        
    def save(self, commit=True):
        user = super(ChangePasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data['new_password'])
        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ('current_password', 'new_password', 'password_confirm',)
