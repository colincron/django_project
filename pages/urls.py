from django.urls import path
#from .views import view_function
from .views import HomePageView, AboutMePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # path('', view_function, name="home"),
    path('', HomePageView.as_view(), name="home"),
    path('aboutme', AboutMePageView.as_view(), name="aboutme"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)