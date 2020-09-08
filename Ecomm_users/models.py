from django.db import models



# Create your models here.
# Create table customers(c_id INT AUTO_INCREMENT, fname varchar(32) Not Null ,lname varchar(32), contact varchar(10) Not Null,
#  email varchar(32) , dob date, primary key(c_id), Unique(contact));

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    contact = models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=True)
    dob = models.DateField()

# Create table categories(cat_id Int AUTO_INCREMENT, cat_name varchar(32), primary key(cat_id));
class Category(models.Model):
    cat_id =  models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=32)
    

# create table suppliers(sid int AUTO_INCREMENT , sname varchar(32) not null, company varchar(32), contact varchar(10) not null, 
# email varchar(32) , primary key(sid), Unique(contact));
class Supplier(models.Model):
    sid= models.AutoField(primary_key=True)
    sname =  models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    contact = models.CharField(max_length=10)
    email =  models.EmailField(unique=True)

# create table products(pid Int AUTO_INCREMENT , pname varchar(32) , pdescription varchar(32) , price Int not null, 
# category Int , supplier Int ,  primary key(pid) , foreign key(category) references categories(cat_id), 
# foreign key(supplier) references suppliers(sid));

class Product(models.Model):
        pid= models.AutoField(primary_key=True)
        pname =  models.CharField(max_length=32)
        pdescription = models.CharField(max_length=32)
        price = models.IntegerField()
        category =  models.ForeignKey(Category,on_delete=models.CASCADE)
        Supplier =  models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)

#create table orders(order_id Int AUTO_INCREMENT, c_id Int not null , pid int not null ,quantity int, order_date date, amount int,
# primary key(order_id),  foreign key(c_id) references customers(c_id), foreign key(pid) references products(pid));
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Category,on_delete=models.RESTRICT)
    product_id = models.ForeignKey(Product,on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    date = models.DateField()