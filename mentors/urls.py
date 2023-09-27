from django.urls import path

from mentors.views import UstozCreateListApiView, UstozRetrieveUpdateDeleteApiView, MijozCreateListApiView, \
    MijozRetrieveUpdateDeleteApiView

urlpatterns = [
    path('ustoz/create_list/', UstozCreateListApiView.as_view()),
    path('ustoz/retrieve-update-delete/<int:pk>/', UstozRetrieveUpdateDeleteApiView.as_view()),
    path('mijoz/create_list/', MijozCreateListApiView.as_view()),
    path('mijoz/retrieve-update-delete/<int:pk>/', MijozRetrieveUpdateDeleteApiView.as_view()),
]
