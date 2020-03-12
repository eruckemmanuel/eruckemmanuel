from django.conf.urls import url

from accounts.views import (GetAuthToken, CreateAccount)



urlpatterns = [
    url('^login/', GetAuthToken.as_view()),
    url('^signup/', CreateAccount.as_view()),
]
