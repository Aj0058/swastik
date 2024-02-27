from django.urls import path
from . import views
urlpatterns = [
    path('home', views.Home, name="home"),
    path('collections', views.collections, name='collections'),
    path("collections/<str:slug>",views.collectionsview,name="collectionsview"),
    path("collections/<str:cate_slug>/<str:prod_slug>",views.productview,name="productview"),
    path("register/",views.Ragister,name="register"),
    path("Login/",views.Login,name="Login"),
    path('logout/',views.Logout, name='Logout')





]

