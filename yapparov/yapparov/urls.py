from type import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path("cre/",views.cre),
    path('admin/', admin.site.urls),

]
