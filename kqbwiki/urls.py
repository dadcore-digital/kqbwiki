from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include('django_nyt.urls')),
    path('', include('wiki.urls'))
]
