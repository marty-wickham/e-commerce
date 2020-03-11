from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
# These are all views that are already provided by Django that will allow us
# to implement the password reset functionality
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # post reset redirect is gonna redirect to the password reset done view.
    url(r'^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name="password_reset"),
    url(r'^done/$', password_reset_done, name="password_reset_done"),
    # This URL is going to contain a token that will have to be  generated for
    # each specific user so we need to create a unique URL for each password
    # reset that's called, usually the URL that would be sent in an email.
    # We're going to use reverse lazy to redirect to the password reset complete view
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name="password_reset_confirm"),
    url(r'complete/$', password_reset_complete, name="password_reset_complete")
]
