from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CategoryView

app_name = "santechnic"
urlpatterns = [
   path('', views.CategoryView.as_view(), name='category'),
   path('<category_name>/', views.ProductsView.as_view(), name='products'),
   path('about_us', views.about_us, name='about_us'),
   path('contacts', views.contacts, name='contacts'),
]
