#from msilib.schema import Class
from multiprocessing import Condition
from tkinter import CASCADE, Entry
from unicodedata import category
from django.db import models
from django.forms import PasswordInput

#Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True, verbose_name='Nombre')
    description = models.CharField(max_length=500)
    Condition = models.BooleanField()
    
    def __str__(self):
        return self.name

#CLASES MODELO QUE REPRESENTA EL MAPEO CON LAS TABLAS DE LAS BD
class Users(models.Model):
    rol_id= models.IntegerField()
    first_names= models.CharField(max_length=255, null=False, unique=True, verbose_name='Nombres')
    last_names= models.CharField(max_length=255,  null=False, unique=True)
    type_id= models.CharField(max_length=125, null=False,)
    num_document= models.IntegerField()
    address= models.CharField(max_length=300, null=False)
    phone= models.CharField(max_length=20, null=False)
    email= models.CharField(max_length=300, null=False)
    Password= models.CharField(max_length=10, null=False)
    Condition= models.BooleanField()
    Rol= models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rol_id

class Category(models.Model):
    name= models.CharField(max_length=250, null=True)
    description= models.CharField(max_length=500)
    Condition= models.BooleanField()

class article(models.Model):
    category_id= models.IntegerField()
    code= models.CharField(max_length=150, null=True)
    name= models.CharField(max_length=150, null=True)
    price_sale= models.DecimalField(max_digits=11, decimal_places=4)
    stock= models.IntegerField()
    description= models.CharField(max_length=500)
    Condition= models.BooleanField()
    Category= models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

class Person(models.Model):
    type_person= models.CharField(max_length=125, null=True)
    name= models.CharField(max_length=150, null=True, unique=True)
    type_id= models.CharField(max_length=100, null=True)
    num_document= models.IntegerField(null=True,)
    address= models.CharField(max_length=400, null=True,)
    email= models.CharField(max_length=500, null=True,)

class Entry(models.Model):
    supplierid_id=models.IntegerField(null=True)
    users_id= models.IntegerField(null=True)
    type_voucher= models.CharField(max_length=300)
    serial_voucher= models.CharField(max_length=500, null=True)
    num_voucher= models.CharField(max_length=200, null=True)
    date_hour= models.DateTimeField(auto_now=False, auto_now_add=False)
    tax= models.DecimalField(max_digits=4, decimal_places=2)
    total= models.DecimalField(max_digits=11, decimal_places=2)
    state= models.CharField(max_length=50)
    supplierid_id= models.ForeignKey(Person,on_delete=models.CASCADE)
    users_id= models.ForeignKey(Users,on_delete=models.CASCADE)

class Income_detail(models.Model):
    entry_id= models.IntegerField(null=True)
    article_id= models.IntegerField(null=True)
    amont= models.IntegerField(null=True)
    Entry= models.ForeignKey(Entry, on_delete= models.CASCADE)
    Article= models.ForeignKey(article, on_delete= models.CASCADE)

class Sale(models.Model):
    customer_id= models.IntegerField()
    users_id= models.IntegerField()
    type_voucher= models.CharField(max_length=200, null=True)
    serial_voucher= models.CharField(max_length=300, null=True)
    mun_voucher= models.IntegerField(null=True)
    date_hour= models.DateTimeField(auto_now=False, auto_now_add=False)
    tax= models.DecimalField(max_digits=4, decimal_places=2)
    total= models.DecimalField(max_digits=11, decimal_places=2)
    state= models.CharField(max_length=100)
    Person= models.ForeignKey(Person, on_delete=models.CASCADE)
    Users= models.ForeignKey(Users, on_delete= models.CASCADE)

class Sale_detail(models.Model):
    sale_id= models.IntegerField()
    article_id= models.IntegerField()
    amount= models.IntegerField()
    price= models.DecimalField(max_digits=11, decimal_places=2)
    descuento= models.DecimalField(max_digits=11, decimal_places=2)
    Sale= models.ForeignKey(Sale, on_delete=models.CASCADE)
    Article= models.ForeignKey(article, on_delete=models.CASCADE)


    