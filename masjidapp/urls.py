from django.urls import path
from . import views


urlpatterns = [
    path('countrry',views.CountrylistAPIView.as_view(),name='countrry'),
    path('state',views.StatelistAPIView.as_view(),name='state'),
    path('district',views.DistrictlistAPIView.as_view(),name='district'),
    path('masjidregister',views.MasjidRegisterAPIView.as_view(),name='masjidregister'),
    path('alldata',views.AllDataAPIView.as_view(),name='alldata'),
    path('masjiddata',views.MasjidlistAPIView.as_view(),name='masjiddata'),
    
]