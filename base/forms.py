from django.forms import ModelForm
from . models import User,Order
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserPasswordResetForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1','password2']


class StaffUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'avatar','username','first_name','last_name', 'phone']

# class UserCreationForm(ModelForm):
#     class Meta:
#         model = User
#         field = ['username','email', 'password', 'confirm password']

class OrderCreationForm(ModelForm):
    class Meta:
        model = Order
        field = '__all__'
        exclude = ['date_added','complete','accured','accured_by','order_price','order_no']

class StaffRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','first_name','last_name', 'phone','documents']
        