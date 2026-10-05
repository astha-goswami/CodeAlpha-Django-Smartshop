"""
URL configuration for SmartShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smartshopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('products',views.products),
    path('addtocart',views.addtocart),
    path('dashboard',views.dashboard,name='dashboard'),
    
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
   
    #USER
    path('user/viewproduct/',views.user_viewproduct,name='user_viewproduct'),
    path('user/viewcategory/',views.user_viewcategory,name='user_category'),
   
    path('user/addproduct/',views.user_addProduct,name='user_addProduct'),
    path('user/viewproduct/',views.user_viewProduct,name='user_viewProduct'),
    path('user/editproduct/<int:uid>/',views.user_editProduct,name='user_editProduct'),
    path('user/deleteproduct/<int:uid>/',views.user_deleteProduct,name='user_deleteProduct'),
   
    path('user/addorder/',views.user_addOrder,name='user_addOrder'),
    path('user/vieworder/',views.user_viewOrder,name='user_viewOrder'),
    path('user/editorder/<int:oid>/',views.user_editOrder,name='user_editOrder'),
    path('user/deleteorder/<int:oid>/',views.user_deleteOrder,name='user_deleteOrder'),   

    path('user/addpayment/',views.user_addPayment,name='user_addPayment'),
    path('user/viewpayment/',views.user_viewPayment,name='user_viewPayment'),
    path('user/editpayment/<int:paymentid>/',views.user_editPayment,name='user_editPayment'),
    path('user/deletepayment/<int:paymentid>/',views.user_deletePayment,name='user_deletePayment'),   
    

   
   
    #ADMIN
    path('smartshop_admin/addcategory/',views.admin_addCategory,name='admin_addCategory'),
    path('smartshop_admin/viewcategory/',views.admin_viewCategory,name='admin_viewCategory'),
    path('smartshop_admin/editcategory/<int:cid>/',views.admin_editCategory,name='admin_editCategory'),
    path('smartshop_admin/deletecategory/<int:cid>/',views.admin_deleteCategory,name='admin_deleteCategory'),
   
    path('smartshop_admin/adduser/',views.admin_addUser,name='admin_addUser'),
    path('smartshop_admin/viewuser/',views.admin_viewUser,name='admin_viewUser'),
    path('smartshop_admin/edituser/<int:uid>/',views.admin_editUser,name='admin_editUser'),
    path('smartshop_admin/deleteuser/<int:uid>/',views.admin_deleteUser,name='admin_deleteUser'),
   
    path('smartshop_admin/addproduct/',views.admin_addProduct,name='admin_addProduct'),
    path('smartshop_admin/viewproduct/',views.admin_viewProduct,name='admin_viewProduct'),
    path('smartshop_admin/editproduct/<int:pid>/',views.admin_editProduct,name='admin_editProduct'),
    path('smartshop_admin/deleteproduct/<int:pid>/',views.admin_deleteProduct,name='admin_deleteProduct'),
   
   
   
       #JOIN OPERATIONS
    path('smartshop_admin/viewcategoryproduct/',views.admin_viewCategoryProduct,name='admin_viewCategoryProduct'),
    path('smartshop_admin/viewproductorder/',views.admin_viewProductOrder,name='admin_viewProductOrder'),
    path('smartshop_admin/viewuserproduct/',views.admin_viewUserProduct,name='admin_viewUserProduct'),
    path('smartshop_admin/viewuserorder/',views.admin_viewUserOrder,name='admin_viewUserOrder'),
    path('smartshop_admin/viewuserpayment/',views.admin_viewUserPayment,name='admin_viewUserPayment'),
    path('smartshop_admin/viewuserorderpayment/',views.admin_viewUserOrderPayment,name='admin_viewUserOrderPayment'),
]
