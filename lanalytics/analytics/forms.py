from django import forms

from lanalytics.analytics.models import Analytic


class AnalyticForm(forms.ModelForm):

    class Meta:
        model = Analytic
