from django.conf.urls import  url


from home.views import SaveMessage


urlpatterns = [
    url(r'^save-message/', SaveMessage.as_view()),
]