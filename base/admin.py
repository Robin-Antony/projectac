from django.contrib import admin
from .models import Order,User,Rating,AccurOrder

# Register your models here.

admin.site.register(User)
admin.site.register(Order)
# admin.site.register(Address)
admin.site.register(Rating)
admin.site.register(AccurOrder)
# admin.site.register(Staff)

