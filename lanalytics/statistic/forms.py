import uuid

from random import choice
from hashlib import sha1

from django import forms
from django.utils.translation import ugettext_lazy as _

from lanalytics.statistic.models import Site


class SiteUpdateForm(forms.ModelForm):
    key = forms.CharField(widget=forms.TextInput(\
                        attrs={'readonly': 'readonly', 'class': 'readonly'}))
    class Meta:
        model = Site
        fields = ('name', 'url',)


class SiteAddForm(forms.ModelForm):
    def clean_url(self):
        url = self.cleaned_data['url']
        pref1 = 'http://'
        pref2 = 'https://'

        # auto add http:// prefix if not specified
        if url[0:len(pref1)] != pref1 and url[0:len(pref2)] != pref2:
            return "%s%s" % (pref1, url)
        return url

    def clean_key(self):
        #key_str = '[%s] %s %s' % (
        #    self.cleaned_data['owner'].email,
        #    self.cleaned_data['name'],
        #    self.cleaned_data['url'],
        #)

        key = uuid.uuid4()
        max_shakes = 4
        shakes = 0
        while Site.objects.filter(key=key):
            if shakes > max_shakes:
                raise forms.ValidationError(\
                _("Can't generate unique site key. Please, try again later."))
            key = uuid.uuid4()
            shakes += 1

        return key

    class Meta:
        model = Site
        widgets = {
        'key': forms.HiddenInput(),
        }
        fields = ('name', 'url', 'key')
