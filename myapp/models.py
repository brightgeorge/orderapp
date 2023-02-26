from django.db import models
import datetime

# Create your models here.

class user(models.Model):
    user_code=models.CharField(max_length=25)
    emp_name=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    user_description=models.CharField(max_length=250)
    user_flage=models.CharField(max_length=10)

class item(models.Model):
    item_code=models.CharField(max_length=25)
    item_name=models.CharField(max_length=200)
    item_uom=models.CharField(max_length=50)
    item_barcode=models.CharField(max_length=100)
    item_category = models.CharField(max_length=50)
    item_kitchen = models.CharField(max_length=50)
    item_production_cost = models.FloatField(max_length=10)
    item_sales_rate = models.FloatField(max_length=10)
    item_branch_sales_rate = models.FloatField(max_length=10)
    item_mrp = models.FloatField(max_length=10)
    item_image = models.ImageField(upload_to='itemimages')
    item_description= models.CharField(max_length=250)
    item_flag=models.IntegerField()

class catergory(models.Model):
    catergory_name=models.CharField(max_length=200)
    catergory_created_by=models.CharField(max_length=200)
    catergory_flag=models.CharField(max_length=2)

class department(models.Model):
    department_name=models.CharField(max_length=200)
    department_created_by=models.CharField(max_length=200)
    department_flag=models.CharField(max_length=2)

class uom(models.Model):
    uom_name=models.CharField(max_length=200)
    uom_created_by=models.CharField(max_length=200)
    uom_flag=models.CharField(max_length=2)

class branch(models.Model):
    branch_code=models.CharField(max_length=50)
    branch_name = models.CharField(max_length=200)
    branch_description = models.CharField(max_length=250)
    branch_created_by = models.CharField(max_length=200)
    branch_flag = models.IntegerField()

class branch_1(models.Model):
    item_name=models.CharField(max_length=200)
    item_uom = models.CharField(max_length=50)
    item_qty=models.FloatField(max_length=200)
    date_time=models.DateTimeField()
    updated_by=models.CharField(max_length=200)
class branch_2(models.Model):
    item_name=models.CharField(max_length=200)
    item_uom = models.CharField(max_length=50)
    item_qty=models.FloatField(max_length=200)
    date_time=models.DateTimeField()
    updated_by=models.CharField(max_length=200)
class branch_3(models.Model):
    item_name=models.CharField(max_length=200)
    item_uom = models.CharField(max_length=50)
    item_qty=models.FloatField(max_length=200)
    date_time=models.DateTimeField()
    updated_by=models.CharField(max_length=200)

class consolidated(models.Model):
    item_code=models.CharField(max_length=25)
    item_name=models.CharField(max_length=200)
    item_uom=models.CharField(max_length=50)
    item_barcode=models.CharField(max_length=100)
    item_category = models.CharField(max_length=50)
    item_kitchen = models.CharField(max_length=50)
    item_production_cost = models.FloatField(max_length=10)
    item_sales_rate = models.FloatField(max_length=10)
    item_branch_sales_rate = models.FloatField(max_length=10)
    item_mrp = models.FloatField(max_length=10)
    item_image = models.ImageField(upload_to='itemimages')
    item_description= models.CharField(max_length=250)
    item_created_by=models.CharField(max_length=200)
    order_qty_br1=models.FloatField()
    order_qty_br1_date = models.DateField()
    order_qty_br2 = models.FloatField()
    order_qty_br2_date = models.DateField()
    order_qty_br3 = models.FloatField()
    order_qty_br3_date = models.DateField()
    item_flag=models.IntegerField()


    def get_total(self):
        return self.order_qty_br1+self.order_qty_br2+self.order_qty_br3


    def get_total_f(self):
        if self.order_qty_br3_date != datetime.date.today():
            return self.order_qty_br1
    def get_total_s(self):
            return self.order_qty_br2
    def get_total_t(self):
            return self.order_qty_br3

    def get_total1(self):
        if self.order_qty_br1_date != datetime.date.today() and self.order_qty_br2_date == datetime.date.today() and self.order_qty_br3_date == datetime.date.today():
            return self.order_qty_br2 + self.order_qty_br3
    def get_total2(self):
        if self.order_qty_br2_date != datetime.date.today() and self.order_qty_br1_date == datetime.date.today() and self.order_qty_br3_date == datetime.date.today():
            return self.order_qty_br1 + self.order_qty_br3
    def get_total3(self):
        if self.order_qty_br3_date != datetime.date.today() and self.order_qty_br1_date == datetime.date.today() and self.order_qty_br2_date == datetime.date.today():
            return self.order_qty_br1 + self.order_qty_br2

    def my_get_total(self):
        if self.order_qty_br1_date != datetime.date.today() and self.order_qty_br2_date == datetime.date.today() and self.order_qty_br3_date == datetime.date.today():
            return self.order_qty_br2 + self.order_qty_br3
        if self.order_qty_br2_date != datetime.date.today() and self.order_qty_br1_date == datetime.date.today() and self.order_qty_br3_date == datetime.date.today():
            return self.order_qty_br1 + self.order_qty_br3
        if self.order_qty_br3_date != datetime.date.today() and self.order_qty_br1_date == datetime.date.today() and self.order_qty_br2_date == datetime.date.today():
            return self.order_qty_br1 + self.order_qty_br2







