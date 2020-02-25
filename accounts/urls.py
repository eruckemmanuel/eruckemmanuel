from django.conf.urls import url

from accounts.views import (GetAuthToken, CheckUsernameAvailability,
                           CreateAccount, VerifyPhoneNumber, ValidateVerificationCode)



urlpatterns = [
    url('^login/', GetAuthToken.as_view()),
    url('^check-username/', CheckUsernameAvailability.as_view()),
    url('^signup/', CreateAccount.as_view()),
    url('^verify-phone/', VerifyPhoneNumber.as_view()),
    url('^validate-verification-code/', ValidateVerificationCode.as_view()),
]