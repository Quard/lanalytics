from django import forms

from lanalytics.analytics.models import Analytic


class AnalyticForm(forms.ModelForm):

    def clean_referrer(self):
        site = self.cleaned_data['site']
        referrer = self.cleaned_data['referrer']
        if site.host in referrer:
            return ''

        return referrer

    class Meta:
        model = Analytic
