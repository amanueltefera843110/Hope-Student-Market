
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home, name="home"),
   path('about/', views.about,name="about"),
   path('search/', views.search,name="search"),
   path('login/', views.login_user,name="login"),
   path('logout/', views.logout_user,name="logout"),
   path('register/', views.register_user, name="register"),
   path('update_password/', views.update_password, name="update_password"),
   path('update_user/', views.update_user, name="update_user"),
   path('update_info/', views.update_info, name="update_info"),
   path('product/<int:pk>', views.product, name="product"),
   path('category/<str:foo>', views.category, name="category"),
   path('category_summary/', views.category_summary, name="category_summary"),

   
   path('add_product/', views.add_product, name='add_product'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


