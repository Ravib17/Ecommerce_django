from django.urls import path

from . import views

app_name = 'Ecomm_admin'
urlpatterns = [
    path('', views.indexPage, name='homePage'),
    path('suppliers', views.updateSeller.as_view(), name='updateSeller'),
    path('category', views.updateCategory.as_view(), name='updateCategory'),
    path('products', views.updateProduct.as_view(), name='updateProduct'),
    path('createCategory/', views.createCategory, name='createCategory'),
    path('createProduct/', views.createProduct, name='createProduct'),
    path('createSupplier/', views.createSupplier, name='createSupplier'),
	path('<int:pk>/product/', views.detailProduct, name ="detailProduct"),
	path('<int:pk>/product/delete/', views.removeProduct, name ="removeProduct"),
    path('<int:pk>/product/edit/', views.editProduct, name ="editProduct"),
	path('<int:pk>/Category/', views.detailCategory, name ="detailCategory"),
	path('<int:pk>/Category/delete/', views.removeCategory, name ="removeCategory"),
    path('<int:pk>/Category/edit/', views.editCategory, name ="editCategory"),
	path('<int:pk>/Supplier/', views.detailSupplier, name ="detailSupplier"),
	path('<int:pk>/Supplier/delete/', views.removeSupplier, name ="removeSupplier"),
    path('<int:pk>/Supplier/edit/', views.editSupplier, name ="editSupplier"),
]