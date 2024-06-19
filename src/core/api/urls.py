from django.urls import path

from core.api import views as core_views

app_name = "core"

urlpatterns = [
    path("user/", core_views.UserListCreateView.as_view(), name="user"),
    path("template/", core_views.TemplateListCreateView.as_view(), name="template"),
    path("email/", core_views.EmailListCreateView.as_view(), name="email"),
]
