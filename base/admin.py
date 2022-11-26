from django.contrib import admin
from .models import Order,User,Rating,AccurOrder,Feedback,QandA

# Register your models here.

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(AccurOrder)
admin.site.register(QandA)

