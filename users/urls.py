from django.urls import path

from users.views import SignUpApiView, VerifyCodeApiView

urlpatterns = [
    path('signup/', SignUpApiView.as_view()),
    path('verify-code/', VerifyCodeApiView.as_view()),
]
