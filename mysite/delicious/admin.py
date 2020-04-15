from django.contrib import admin

# Register your models here.
from . models import Dish, Spicy, OrderHeader,OrderLine,Contact
admin.site.register(Dish)
admin.site.register(Spicy)
admin.site.register(OrderHeader)
admin.site.register(OrderLine)
admin.site.register(Contact)
