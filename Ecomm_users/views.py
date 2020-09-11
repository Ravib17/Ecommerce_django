from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.utils.timezone import datetime
import json

from .models import Customer,Product,Order,Category

class IndexView(generic.ListView):
    products = Product
    model = Product
    template_name = 'Ecomm_user/index.html'
    context_object_name = 'all_search_results'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'all_products': Product.objects.all(),
            'search':self.request.GET.get('search')
            
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            searchResult = Product.objects.filter(Q(pname__icontains=query) | Q(pdescription__icontains =query))
        else:
            searchResult = None
        return searchResult

class viewCategories(generic.ListView):
      model = Category
      template_name='Ecomm_user/viewcategories.html'
      context_object_name="all_categories"

      def get_queryset(self):
          return Category.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name="Ecomm_user/detail.html"

class PlaceOrderView(generic.DetailView):
    model = Product
    template_name="Ecomm_user/placeorder.html"
      
def validateorder(request,product_id):
    product  = Product.objects.get(pk=product_id)
    quantity = request.POST.get('quantity')

    try:
        cust_mail=str(request.POST.get('email'))
        print(cust_mail.strip())
        print("here")
        customer = Customer.objects.get(email=cust_mail)
    except (KeyError, Customer.DoesNotExist):
        return HttpResponseRedirect(reverse('Ecomm_users:customerDetailsView', args=(product_id,quantity,cust_mail,)))
    else:
        return HttpResponseRedirect(reverse('Ecomm_users:createorder', args=(product_id,quantity,customer.c_id)))

def customerDetailsView(request,product_id,quantity,cust_mail):
     context = {
         'product':Product.objects.get(pk=product_id),
         'quantity':quantity,
         'email':cust_mail
        
     }
     return render(request,"Ecomm_user\customerForm.html",context)

def addCustomerDetails(request,product_id,quantity):
    fname= request.POST.get('fname')
    lname= request.POST.get('lname')
    contact= request.POST.get('contact')
    dob= request.POST.get('dob')
    email= request.POST.get('email')
    customer = Customer(fname=fname,lname=lname,contact=contact,email=email,dob=dob)
    print(request.POST)
    customer.save()
    return HttpResponseRedirect(reverse('Ecomm_users:createorder', args=(product_id,quantity,customer.c_id)))

     

def createorder(request,product_id,quantity,customer_id):
    product  = Product.objects.get(pk=product_id)
    customer = Customer.objects.get(pk=customer_id)
    amount = int(product.price) * int(quantity)
    o_date= datetime.today()
    new_order = Order(customer=customer,product=product,quantity=quantity,order_date=o_date,amount=amount)
    new_order.save()
    data={
        'product_id':product_id,
        'customer_id':customer_id,
        'order_id':new_order.order_id
    }
    json_data = json.dumps(data)
    request.session['order_data']=json_data
    return HttpResponseRedirect(reverse('Ecomm_users:confirmorder',args=(product_id,)))

def confirmorder(request,product_id):
    json_data = request.session.get('order_data',None)
    data =json.loads(json_data)
    context = {
        "product":Product.objects.get(pk=data['product_id']),
        "customer":Customer.objects.get(pk=data['customer_id']),
        "order":Order.objects.get(pk=data['order_id'])
    }
    print(context)
    return render(request,"Ecomm_user\confirmorder.html",context)

def orderHistoryView(request):
    try:
        customer = Customer.objects.get(email=request.POST.get('email'))
    except (KeyError, Customer.DoesNotExist):
        context = {
            'customer':None
        }
        return render(request,'Ecomm_user/orderhistory.html',context)
    else:
        all_orders=Order.objects.filter(customer=customer)
        context = {
            'customer':customer,
            'all_orders':all_orders
        }
    return render(request,'Ecomm_user/orderhistory.html',context)

def showCatProducts(request,cat_id):
    products=Product.objects.filter(category=cat_id)
    context = {
        'products':products
    }
    return render(request,"Ecomm_user/viewcatproducts.html",context)

