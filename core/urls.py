from django.urls import path
from .views import recaptcha_page, verify_recaptcha

urlpatterns = [
    path("recaptcha/", recaptcha_page, name="recaptcha"),
    path("verify/", verify_recaptcha, name="verify"),
]
