from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView
from .views import ProfileAPIView, ConfirmEmailView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    # 유효한 이메일이 유저에게 전달
    re_path(
        r"^account-confirm-email/$",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    # 유저가 클릭한 이메일(=링크) 확인
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("", include("dj_rest_auth.registration.urls")),
    path("profile/", ProfileAPIView.as_view()),
]
