
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('movie_app.urls')),

]

urlpatterns += swagger