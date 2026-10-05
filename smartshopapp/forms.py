from django import forms
from .models import Category,Product,User,Cart,Order,Payment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentForm(forms.ModelForm): 
    class Meta:
        model = Payment
        fields = '__all__'
