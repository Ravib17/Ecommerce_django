from django.urls import path

from . import views
from .models import Customer,Product
app_name = 'Ecomm_users'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories',views.viewCategories.as_view(), name="viewCategories"),
    path('<int:cat_id>/showcatproducts',views.showCatProducts, name="showCatProducts"),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('<int:pk>/placeorder/',views.PlaceOrderView.as_view(), name='placeorder'),
    path('<int:product_id>/validateorder/',views.validateorder, name='validateorder'),
    path('<int:product_id>/createorder/?(<int:quantity>,<int:customer_id>)',views.createorder, name='createorder'),
    path('<int:product_id>/customerdetails/?(<int:quantity>,<str:cust_mail>)',views.customerDetailsView, name='customerDetailsView'),
    path('<int:product_id>/submitdetails/?(<int:quantity>)',views.addCustomerDetails, name='addCustomerDetails'),
    path('<int:product_id>/confirmorder/',views.confirmorder, name='confirmorder'),
    path('vieworderhistory',views.orderHistoryView,name='orderHistoryView')
]