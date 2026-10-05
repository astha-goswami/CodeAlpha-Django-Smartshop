# from django.db import models

# # Create your models here.
# class User(models.Model):
#     uid=models.IntegerField(primary_key=True)
#     uusername=models.CharField(max_length=100)
#     uemail=models.EmailField(unique=True)
#     upassword=models.CharField(max_length=100)
#     uaddr=models.CharField(max_length=100)

#     def __str__(self):
#         return self.uusername

# class Category(models.Model):
#     categoryid=models.IntegerField(primary_key=True)
#     categoryname=models.CharField(max_length=100)

#     def __str__(self):
#          return self.categoryname

# class Product(models.Model):
#     pid=models.IntegerField(primary_key=True)
#     pname=models.CharField(max_length=100)
#     pcategory=models.ForeignKey(Category,on_delete=models.CASCADE)
#     pprice=models.CharField(max_length=100)
#     pstock=models.IntegerField(default=0)

#     def __str__(self):
#         self.pname

# class Cart(models.Model):
#     cartid=models.IntegerField(primary_key=True)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)

#     def __str__(self):
#         return self.user.uusername + " - " + self.product.pname

# class Order(models.Model):
#     oid=models.IntegerField(primary_key=True)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)
#     totalprice = models.DecimalField(max_digits=10,decimal_places=2)
#     address = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.oid)
    

    
from django.db import models

class Category(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=100)
    cdescription = models.TextField(blank=True)

    def __str__(self):
        return self.cname

class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=100)
    uemail = models.EmailField(unique=True)
    uphone = models.IntegerField()
    uaddr = models.TextField()

    def __str__(self):
        return self.uname

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    pprice = models.FloatField()
    pquantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Product')

    def __str__(self):
        return self.pname

class Cart(models.Model):
    cartid = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Cart')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Cart')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.uusername} - {self.product.pname}"


class Order(models.Model):
    oid = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Order')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Order')
    quantity = models.IntegerField(default=1)
    total_amount = models.FloatField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50,default='Pending')

    def __str__(self):
        return f"Order {self.oid}"

class Payment(models.Model):
    paymentid = models.IntegerField(primary_key=True)
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name='Payment')
    payment_method = models.CharField(max_length=50)
    payment_amount = models.FloatField()
    payment_status = models.CharField(max_length=50,default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.paymentid}"

