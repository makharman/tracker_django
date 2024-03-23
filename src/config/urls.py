from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('account/', include('account.urls')),
    path('api/v1/', include('api.urls')),

]
