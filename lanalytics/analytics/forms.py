from django import forms

from lanalytics.analytics.models import Analytic


class AnalyticForm(forms.ModelForm):
    # TODO: check site by key
    # TODO: check REFERRER etc.

    class Meta:
        model = Analytic
