from django.shortcuts import render,redirect

# Create your views here.
from django.views import generic
from django.http import HttpResponse
from django.db import models
from Ecomm_users.models import Category,Supplier,Product

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,"polls/detail.html",{'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def indexPage(request):
	#return HttpResponse('<h1>This is my home page</h1>')
	return render(request, 'Ecomm_admin/index.html')

# def updateSeller(request):
	# #return HttpResponse('<h1>This is my home page</h1>')
	# return render(request, 'Ecomm_admin/updateSeller.html')

# def updateCategory(request):
	# #return HttpResponse('<h1>This is my home page</h1>')
	# return render(request, 'Ecomm_admin/updateCategory.html')

# def updateProduct(request):
	# #return HttpResponse('<h1>This is my home page</h1>')
	# return render(request, 'Ecomm_admin/updateProduct.html')

class updateSeller(generic.ListView):
	template_name = 'Ecomm_admin/updateSeller.html'
	context_object_name = 'available_supplier'
	model = Supplier
	
class updateCategory(generic.ListView):
	template_name = 'Ecomm_admin/updateCategory.html'
	context_object_name = 'available_category'
	model = Category

class updateProduct(generic.ListView):
	template_name = 'Ecomm_admin/updateProduct.html'
	context_object_name = 'available_products'
	model = Product
	
def createCategory(request):
    if request.method=='POST':
        post = Category()
        post.cat_name = request.POST['cat_name']
        post.save()
        return render(request,'Ecomm_admin/index.html')
    else:
        return render(request,'Ecomm_admin/createCategory.html')	
	
def detailCategory(request,pk):
    cats= Category.objects.get(cat_id=pk)
    return render(request,'Ecomm_admin/detailCategory.html',{'cats':cats})

def removeCategory(request,pk):
    Category.objects.get(cat_id=pk).delete()
    return render(request,'Ecomm_admin/index.html')

def editCategory(request,pk):
	if request.method =='POST':
		cats = Category.objects.get(cat_id=pk)
		cats.cat_name = request.POST['cat_name']
		cats.save()
		return render(request,'Ecomm_admin/index.html')
	else:
		cats = Category.objects.get(cat_id=pk)
		return render(request,'Ecomm_admin/editCategory.html',{'cats' : cats})
		
def detailProduct(request,pk):
    pros= Product.objects.get(pid=pk)
    return render(request,'Ecomm_admin/detailProduct.html',{'pros':pros})

def removeProduct(request,pk):
	try: 
		Product.objects.get(pid=pk).delete()
		return render(request,'Ecomm_admin/index.html')
	except (KeyError, models.RestrictedError ):
		return render(request, 'Ecomm_admin/product_error.html', None)

def editProduct(request,pk):
	if request.method =='POST':
		pros = Product.objects.get(pid=pk)
		pros.pname = request.POST['pname']
		pros.pdescription = request.POST['pdescription']
		pros.price = request.POST['price']
		pros.category = Category.objects.get(cat_name=request.POST.get('category'))
		pros.Supplier =  Supplier.objects.get(sname=request.POST.get('supplier'))
		pros.save()
		return render(request,'Ecomm_admin/index.html', {})
	else:
		supplier=Supplier.objects.all()
		category=Category.objects.all()
		pros = Product.objects.get(pid=pk)
		return render(request,'Ecomm_admin/editProduct.html',{'pros' : pros, 'allSuppliers' : supplier, 'allCategories' : category})


def createProduct(request):
	if request.method=='POST':
		pro = Product()
		pro.pname = request.POST['pname']
		pro.pdescription = request.POST['pdescription']
		pro.price = request.POST['price']
		pro.category = Category.objects.get(cat_name=request.POST.get('category'))
		pro.Supplier = Supplier.objects.get(sname=request.POST.get('supplier'))
		pro.save()
		return render(request,'Ecomm_admin/index.html') 
	else:
		supplier=Supplier.objects.all()
		category=Category.objects.all()
		return render(request,'Ecomm_admin/createProduct.html',{'allSuppliers' : supplier, 'allCategories' : category})
 

def createSupplier(request):
    if request.method=='POST':
        sup = Supplier()
        sup.sname = request.POST['sname']
        sup.company = request.POST['company']
        sup.contact = request.POST['contact']
        sup.email = request.POST['email']
        sup.save()
        return render(request,'Ecomm_admin/index.html')
    else:
        return render(request,'Ecomm_admin/createSupplier.html')	

def detailSupplier(request,pk):
    sup= Supplier.objects.get(sid=pk)
    return render(request,'Ecomm_admin/detailSupplier.html',{'sup':sup})

def removeSupplier(request,pk):
	try: 
		Supplier.objects.get(sid=pk).delete()
		return render(request,'Ecomm_admin/index.html')
	except (KeyError, models.RestrictedError ):
		return render(request, 'Ecomm_admin/product_error.html', None)

def editSupplier(request,pk):
	if request.method =='POST':
		sup = Supplier.objects.get(sid=pk)
		sup.sname = request.POST['sname']
		sup.company = request.POST['company']
		sup.contact = request.POST['contact']
		sup.email = request.POST['email']
		sup.save()
		return render(request,'Ecomm_admin/index.html')
	else:
		sup = Supplier.objects.get(sid=pk)
		return render(request,'Ecomm_admin/editSupplier.html',{'sup' : sup})
		