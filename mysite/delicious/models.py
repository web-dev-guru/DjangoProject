from django.db import models
import datetime

def increment_number():
    last_num = OrderHeader.objects.all().order_by('id').last()
    if not last_num:
        #print('D' + str(datetime.datetime.now().strftime('%Y%m%d')) + '0000')
        return 'D' + str(datetime.datetime.now().strftime('%Y%m%d')) + '0000'
    o_id = last_num.order_num
    o_int = o_id[12:16]
    new_int = int(o_int) + 1
    new_id = 'D' + str(datetime.datetime.now().strftime('%Y%m%d')) + str(new_int).zfill(4)
    return new_id


# Create your models here.
class OrderHeader(models.Model):
     customer_name=models.CharField(max_length=200)
     creation_time=models.DateTimeField("creation time")
     order_num=models.CharField(max_length=17,unique=False,default=increment_number, editable=False)

class Dish(models.Model):
    dish_name=models.CharField(max_length=200)
    creation_time = models.DateTimeField("creation time")
    def __str__(self):
        return self.dish_name

class Spicy(models.Model):
    spicy_name=models.CharField(max_length=200)
    def __str__(self):
        return self.spicy_name

class OrderLine(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    spicy = models.ForeignKey(Spicy,on_delete=models.CASCADE)
    head = models.ForeignKey(OrderHeader,on_delete=models.CASCADE)


class Contact(models.Model):
    address=models.CharField(max_length=200)
    telephone=models.CharField(max_length=200)
