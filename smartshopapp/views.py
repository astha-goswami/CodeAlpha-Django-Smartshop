from django.shortcuts import render,redirect
from smartshopapp.forms import UserForm,ProductForm,CategoryForm,CartForm,OrderForm,PaymentForm
from .models import Product,Category,User,Cart,Order,Payment

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def products(request): #view
    return render(request,"products.html")

def dashboard(request):
    return render(request,"dashboard.html")

def addtocart(request):
    return render(request,"products.html")

#====================================USER==============================================================================================
def user_dashboard(request):
    return render(request,"user/dashboard.html")

#=================================PRODUCT============================
def user_viewproduct(request):
    return render(request,"user/viewproduct.html")

def user_viewcategory(request):
    return render(request,"user/viewproduct.html")

def user_addProduct(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    form=ProductForm()
    return render(request,"user/addproduct.html",{'form':form})

def user_viewProduct(request):
    product=Product.objects.all()
    print(product.query)
    return render(request,"user/viewproduct.html",{'product':product})

def user_editProduct(request,pid):
    product=product.objects.get(pid=pid)
    if request.method=='POST': #GET==POST condition false
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_viewproduct')
    else:
        form=ProductForm(instance=product)
    return render(request,"user/editproduct.html",{'form':form})

def user_deleteProduct(request,pid):
    product=product.objects.get(pid=pid)
    product.delete()
    return redirect('user_viewproduct')


#========================ORDER==============================
def user_addOrder(request):
    if request.method == 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
    form=OrderForm()
    return render(request,"user/addorder.html",{'form':form})

def user_viewOrder(request):
    order=Order.objects.all()
    print(order.query)
    return render(request,"user/vieworder.html",{'order':order})

def user_editOrder(request,oid):
    order=Order.objects.get(oid=oid)
    if request.method=='POST': #GET==POST condition false
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('user_viewOrder')
    else:
        form=OrderForm(instance=order)
    return render(request,"user/editorder.html",{'form':form})

def user_deleteOrder(request,oid):
    order=Order.objects.get(oid=oid)
    order.delete()
    return redirect('user_viewOrder')


#========================PAYMENT==============================
def user_addPayment(request):
    if request.method == 'POST':
        form=PaymentForm(request.POST)
        if form.is_valid():
            form.save()
    form=PaymentForm()
    return render(request,"user/addpayment.html",{'form':form})

def user_viewPayment(request):
    payment=Payment.objects.all()
    print(payment.query)
    return render(request,"user/viewpayment.html",{'payment':payment})

def user_editPayment(request,paymentid):
    payment=Payment.objects.get(paymentid=paymentid)
    if request.method=='POST': #GET==POST condition false
        form=PaymentForm(request.POST,instance=payment)
        if form.is_valid():
            form.save()
            return redirect('user_viewPayment')
    else:
        form=PaymentForm(instance=payment)
    return render(request,"user/editpayment.html",{'form':form})

def user_deletePayment(request,paymentid):
    payment=Payment.objects.get(paymentid=paymentid)
    payment.delete()
    return redirect('user_viewPayment')







#=================================================ADMIN=================================================================================
def admin_dashboard(request):
    return render(request,"admin/dashboard.html")

#======================PRODUCT================
def admin_addProduct(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    form=ProductForm()
    return render(request,"admin/addproduct.html",{'form':form})

def admin_viewProduct(request):
    product=Product.objects.all()
    print(product.query)
    return render(request,"admin/viewproduct.html",{'product':product})

def admin_editProduct(request,pid):
    product=Product.objects.get(pid=pid)
    if request.method=='POST': #GET==POST condition false
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_viewProduct')
    else:
        form=ProductForm(instance=product)
    return render(request,"admin/editproduct.html",{'form':form})

def admin_deleteProduct(request,pid):
    product=Product.objects.get(pid=pid)
    product.delete()
    return redirect('admin_viewProduct')


#=============================CATEGORY=================
def admin_addCategory(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form=CategoryForm()
    return render(request,"admin/addcategory.html",{'form':form})

def admin_viewCategory(request):
    category=Category.objects.all()
    print(category.query)
    return render(request,"admin/viewcategory.html",{'category':category})

def admin_editCategory(request,cid):
    category=Category.objects.get(cid=cid)
    if request.method=='POST': #GET==POST condition false
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_viewCategory')
    else:
        form=CategoryForm(instance=category)
    return render(request,"admin/editcategory.html",{'form':form})

def admin_deleteCategory(request,cid):
    category=Category.objects.get(cid=cid)
    category.delete()
    return redirect('admin_viewCategory')


#==========================USER===================
def admin_addUser(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
    form=UserForm()
    return render(request,"admin/adduser.html",{'form':form})

def admin_viewUser(request):
    user=User.objects.all()
    print(user.query)
    return render(request,"admin/viewuser.html",{'user':user})

def admin_editUser(request,uid):
    user=User.objects.get(uid=uid)
    if request.method=='POST': #GET==POST condition false
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_viewUser')
    else:
        form=UserForm(instance=user)
    return render(request,"admin/edituser.html",{'form':form})

def admin_deleteUser(request,uid):
    user=User.objects.get(uid=uid)
    user.delete()
    return redirect('admin_viewUser')




#========================================================JOIN OPERATIONS===================================
# =========================================================
# 1. VIEW CATEGORY PRODUCT
# Category -> Product
# One Category has Many Products
# =========================================================
def admin_viewCategoryProduct(request):
    category = Category.objects.prefetch_related('Product').all()
    return render(request,"admin/viewcategoryproduct.html",{'category': category})


# =========================================================
# 2. VIEW PRODUCT ORDER
# Product -> Order
# One Product has Many Orders
# =========================================================
def admin_viewProductOrder(request):
    product = Product.objects.select_related('category').prefetch_related('Order').all()
    return render(request,"admin/viewproductorder.html",{'product': product})


# =========================================================
# 3. VIEW USER PRODUCT
# User -> Product
# =========================================================
def admin_viewUserProduct(request):
    user = User.objects.prefetch_related('Order__product').all()
    return render(request,"admin/viewuserproduct.html",{'user': user})


# =========================================================
# 4. VIEW USER ORDER
# User -> Order
# =========================================================
def admin_viewUserOrder(request):
    user = User.objects.prefetch_related('Order__product').all()
    return render(request,"admin/viewuserorder.html",{'user': user})


# =========================================================
# 5. VIEW USER PAYMENT
# User -> Payment
# =========================================================

def admin_viewUserPayment(request):
    user = User.objects.prefetch_related('Order__Payment').all()
    return render(request,"admin/viewuserpayment.html",{'user': user})


# =========================================================
# 6. VIEW USER ORDER PAYMENT
# User -> Order -> Payment
# =========================================================

def admin_viewUserOrderPayment(request):
    user = User.objects.prefetch_related('Order__Payment','Order__product').all()
    return render(request,"admin/viewuserorderpayment.html",{'user': user})