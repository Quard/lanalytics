from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to

from lanalytics.account.forms import RegistrationForm, ProfileForm, \
                                     ChangePasswordForm
from lanalytics.statistic.models import Site
from lanalytics.statistic.forms import SiteForm


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


@login_required
def logout(request):
    from django.contrib.auth import logout
    logout(request)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@render_to('account/profile.html')
def profile(request):
    form = ProfileForm(instance=request.user, prefix="profile")
    chpwd_form = ChangePasswordForm(instance=request.user)

    if request.method == 'POST':
        if 'change_profile' in request.POST:
            form = ProfileForm(request.POST, \
                           instance=request.user, prefix="profile")

            if form.is_valid():
                form.save()
                return redirect('profile')

        if 'change_password' in request.POST:
            chpwd_form = ChangePasswordForm(request.POST, \
                                            instance=request.user)
            if chpwd_form.is_valid():
                chpwd_form.save()
                return redirect('profile')

    return {
        'chpwd_form': chpwd_form,
        'form': form,
        'current_menu': 'profile',
    }


@login_required
@render_to('account/my_sites.html')
def my_sites(request):
    return {
        'current_menu': 'my-sites',
    }


@login_required
@render_to('account/edit_site.html')
def edit_site(request, pk=None):
    site = None
    if pk:
        site = get_object_or_404(Site, pk=pk)

    form = SiteForm(instance=site)
    if request.method == 'POST':
        post = request.POST.copy()
        post['owner'] = request.user.pk
        post['key'] = '-'
        form = SiteForm(post, instance=site)
        if form.is_valid():
            form.save()

            return redirect(reverse('my_sites'))
        else:
            print form.errors
    
    
    return {
        'form': form,
        'site': site,
        'current_menu': 'add-site',
    }


@login_required
def delete_site(request, pk=None):
    site = get_object_or_404(Site, pk=pk)
    site.delete()

    return redirect(reverse('my_sites'))
