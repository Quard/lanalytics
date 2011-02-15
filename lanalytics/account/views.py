from django.conf import settings
from django.shortcuts import redirect
from annoying.decorators import render_to

from lanalytics.account.forms import RegistrationForm


@render_to('registration/registration.html')
def registration(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(settings.LOGIN_REDIRECT_URL)

    return {
        'form': form,
    }
