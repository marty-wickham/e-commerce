from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    # Give the URL a name of logout so in the href when we said url 'logout'
    # then it will map directly to the URL that has the name of logout.
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url(r'^user_profile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
