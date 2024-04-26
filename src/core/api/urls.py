from core.api import views as core_views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('email/', core_views.CreateNewEmailView.as_view(), name="send_message"),
]
