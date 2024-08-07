from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/", include("comments.urls")),
    path("api/", include("projects.urls")),
    path("api/", include("task.urls")),
    path("api/token/", TokenObtainPairView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()