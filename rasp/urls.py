from . import views
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Student Management API",
        default_version='v1',
        description="Document for API",
        terms_of_service="https://www.pbl5.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('capture/', views.PictureAPIView.as_view()),
    path('doc',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
