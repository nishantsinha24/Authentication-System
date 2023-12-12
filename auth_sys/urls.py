from django.contrib import admin
from django.urls import path, include
from account import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls'))
]
