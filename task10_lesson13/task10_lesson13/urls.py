from django.contrib import admin
from django.urls import path
from task10_lesson13.views import first
from second_app.views import second

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', view=first),
    path('second/', view=second),
]
