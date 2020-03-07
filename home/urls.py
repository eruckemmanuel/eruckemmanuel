from django.conf.urls import  url


from home.views import SaveMessage, GetMessages


urlpatterns = [
    url(r'^message/', SaveMessage.as_view()),
    url(r'^get-messages/', GetMessages.as_view()),
]