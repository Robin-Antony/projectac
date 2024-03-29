from django.forms import ModelForm
from . models import User,Order,Feedback,QandA
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']

class UserPasswordResetForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1','password2']


class StaffUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'avatar','first_name','last_name', 'phone']

# class UserCreationForm(ModelForm):
#     class Meta:
#         model = User
#         field = ['username','email', 'password', 'confirm password']

class OrderCreationForm(ModelForm):
    class Meta:
        model = Order
        field = '__all__'
        exclude = ['date_added','complete','accured','accured_by','order_price','order_no','history']

class StaffRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','first_name','last_name', 'phone','documents']


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        field = ['name','feedback','suggestion']
        exclude = ['created']

class QandAForm(ModelForm):
    class Meta:
        model = QandA
        field = ['name','question']
        exclude = ['answer','answered','created']

        