from django.conf.urls import  url


from home.views import ContactMessage


urlpatterns = [
    url(r'^message/', ContactMessage.as_view()),
]