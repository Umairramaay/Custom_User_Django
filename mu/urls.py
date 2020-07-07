from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('accounts/', include('users.urls')),
    # path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]