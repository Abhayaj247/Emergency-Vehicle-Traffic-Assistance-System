from django.conf.urls import url, include
from . import views
from .views import home2,save_patient,emergency_detection
from django.urls import path

urlpatterns = [
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^accounts/status/$', views.UserStatusView.as_view(), name="status"),
    path('home2/', home2, name='home2'),
    path('save_patient/', save_patient, name='save_patient'),
    path('emergency_detection/',emergency_detection,name='emergency_detection')
]
