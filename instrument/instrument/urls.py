from django.contrib import admin
from django.urls import path
from instrument import views
from .views import ImageDetectAPI, InstrumentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/instrument/', InstrumentList.as_view(), name='instrument_list'),
    path('api/detect/', ImageDetectAPI.as_view(), name='image-detect-api'),
]

