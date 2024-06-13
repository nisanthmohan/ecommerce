from django.urls import path
from store import views

urlpatterns=[
    path("home/",views.homeview.as_view(),name="home"),
    path("cat/<int:pk>",views.category_data.as_view(),name="cat_data"),
    path("pro/<int:pk>",views.product_data.as_view(),name="pro_data"),
    path("reg/",views.regview.as_view(),name="reg"),
    path("login/",views.loginview.as_view(),name="login"),
    path("logout/",views.logoutview.as_view(),name="logout"),
    path("cart/<int:pk>",views.cartview.as_view(),name="cart"),
    path("delete/<int:pk>",views.cart_deleteview.as_view(),name="del"),
    path("cartdata/",views.cart_dataview.as_view(),name="c_data"),
    path("order/<int:pk>",views.orderview.as_view(),name="ord"),
    path("orderlist/",views.orderlist.as_view(),name="ordlist"),
    path("delete/<int:pk>",views.orderlist.as_view(),name="ordlist"),
    path("search/",views.searchview.as_view(),name="srch")

]
