"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm


schema_view = get_schema_view(
   openapi.Info(
      title="QuestionTime API",
      default_version='v1',
      description="Questions and Answers API, with management of 'comments', 'users' and 'likes'",
      contact=openapi.Contact(email="erickvb12@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Register via browser
    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
         ), name="django_registration_register"),

    # Login via browser
    path("accounts/",
         include("django_registration.backends.one_step.urls")),

    # Login via browser
    path("accounts/",
         include("django.contrib.auth.urls")),

    #Docs
    url(r'^docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),

    url(r'^docs/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    # urls users app
    path("api/",
         include("users.api.urls")),

    # urls questions app
    path("api/",
         include("questions.api.urls")),

    # Login browsable API
    path("api-auth/",
         include("rest_framework.urls")),

    # Login via REST
    path("api/rest-auth/",
         include("rest_auth.urls")),

    # Registration via REST
    path("api/rest-auth/registration/",
         include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
