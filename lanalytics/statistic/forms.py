from random import choice
from hashlib import sha1
from django import forms

from lanalytics.statistic.models import Site


class SiteForm(forms.ModelForm):

    def clean_key(self):
        key_str = '[%s] %s %s' % (
            self.cleaned_data['owner'].email,
            self.cleaned_data['name'],
            self.cleaned_data['url'],
        )

        key = sha1(key_str).hexdigest()
        while Site.objects.filter(key=key):
            key_str += choice('!@#$%^&**()_+1234567890-=')
            key = sha1(key_str).hexdigest()

        return key

    class Meta:
        model = Site
