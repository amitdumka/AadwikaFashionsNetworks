"""
URL configuration for estore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings  # add this
from django.urls import include, path
from django.conf.urls.static import static 

 
try:
    from rest_framework.authtoken.views import obtain_auth_token
except:
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/jwt/", view=obtain_auth_token),
    
    #This is oauth2 part    
   # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
   # below there line need to be reviews
    path('api-auth/', include('rest_framework.urls')), # Need to check which one is working
    path('v2/', include('django_dyn_api.urls')),     # <-- NEW

]


# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append(path("api/", include("api.urls"))) # Need to check which one is working
    urlpatterns.append(path("login/jwt/", view=obtain_auth_token)) # Need to check which one is working
   
except:
    pass
# add this
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)