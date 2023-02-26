from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('login_request/',views.login_request,name='login_request'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),

    path('test/',views.test,name='test'),

#*********USER START HERE ***********

    path('create_user/',views.create_user,name='create_user'),
    path('user_regi/',views.user_regi,name='user_regi'),
    path('view_all_users/',views.view_all_users,name='view_all_users'),
    path('del_user/<id>',views.del_user,name='del_user'),
    path('user_update/<id>',views.user_update,name='user_update'),

#*********USER END HERE ***********

    #****** item creation start here *********

    path('item_creation_page/',views.item_creation_page,name='item_creation_page'),
    path('item_creation/',views.item_creation,name='item_creation'),
    path('view_all_items/',views.view_all_items,name='view_all_items'),
    path('del_items/<id>',views.del_items,name='del_items'),
    path('update_item/<id>',views.update_item,name='update_item'),
    path('update_item_page/<id>',views.update_item_page,name='update_item_page'),

    #****** item creation end here *********

###********* CATEGORY CREATION END HERE *************

    path('create_category/',views.create_category,name='create_category'),
    path('category_regi/',views.category_regi,name='category_regi'),
    path('view_all_catergory/',views.view_all_catergory,name='view_all_catergory'),
    path('catergory_delete/<id>',views.catergory_delete,name='catergory_delete'),
    path('update_category/<id>',views.update_category,name='update_category'),

###********* CATEGORY CREATION END HERE *************

###********* DEPARTMENT CREATION END HERE *************

    path('create_department/',views.create_department,name='create_department'),
    path('department_regi/',views.department_regi,name='department_regi'),
    path('view_all_department/', views.view_all_department, name='view_all_department'),
    path('department_delete/<id>', views.department_delete, name='department_delete'),
    path('department_update/<id>', views.department_update, name='department_update'),

###********* DEPARTMENT CREATION END HERE *************
###********* UOM CREATION START HERE *************

    path('create_uom/',views.create_uom,name='create_uom'),
    path('uom_regi/', views.uom_regi, name='uom_regi'),
    path('view_all_uom/', views.view_all_uom, name='view_all_uom'),
    path('uom_delete/<id>', views.uom_delete, name='uom_delete'),
    path('uom_update/<id>', views.uom_update, name='uom_update'),

###********* UOM CREATION END HERE *************

###********* BRANCH CREATION END HERE *************

    path('branch_creation_page/',views.branch_creation_page,name='branch_creation_page'),
    path('branch_cration/',views.branch_cration,name='branch_cration'),
    path('view_all_branch/',views.view_all_branch,name='view_all_branch'),
    path('branch_update/<id>',views.branch_update,name='branch_update'),
    path('consolidated_order/',views.consolidated_order,name='consolidated_order'),
    path('consolidated_order2/',views.consolidated_order2,name='consolidated_order2'),


###********* BRANCH CREATION END HERE *************

###******************************************************** ALL REPORTS  START HERE *************

###********* REPORTS ORDER START HERE *************

    path('department_wise/',views.department_wise,name='department_wise'),
    path('department_wises/', views.department_wises, name='department_wises'),

###********* REPORTS ORDER END HERE *************
###********* REPORTS PRODUCTION START HERE *************

    path('production_home/',views.production_home,name='production_home'),
    path('total_order/',views.total_order,name='total_order'),
    path('pro_department_wises/', views.pro_department_wises, name='pro_department_wises'),

###********* REPORTS PRODUCTION END HERE *************
###********* REPORTS DESPATCH START HERE *************

    path('des_br1_rep/',views.des_br1_rep,name='des_br1_rep'),
    path('des_br2_rep/', views.des_br2_rep, name='des_br2_rep'),
    path('des_br3_rep/', views.des_br3_rep, name='des_br3_rep'),

###********* REPORTS DESPATCH END HERE *************
###**************************************************************** ALL REPORTS  START HERE *************

###********************************************* ALL BRANCH START HERE *************
###********* BRANCH1 START HERE *************

    path('br1_order_page',views.br1_order_page,name='br1_order_page'),
    path('br1_order_update/<id>',views.br1_order_update,name='br1_order_update'),
    path('copit/',views.copit,name='copit'),

###********* BRANCH1 END HERE *************
###********* BRANCH2 START HERE *************

    path('br2_order_page',views.br2_order_page,name='br2_order_page'),
    path('br2_order_update/<id>',views.br2_order_update,name='br2_order_update'),

###********* BRANCH2 END HERE *************
###********* BRANCH3 START HERE *************

    path('br3_order_page',views.br3_order_page,name='br3_order_page'),
    path('br3_order_update/<id>',views.br3_order_update,name='br3_order_update'),

###********* BRANCH3 END HERE *************
###******************************************** ALL BRANCH END HERE *************



#**** logout start here

    path('logout/',views.logout,name='logout'),

#**** logout end here

]