import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader,RequestContext,context
from rest_framework import generics
from .serializers import ContactSerializer
from .models import Spicy, Dish, OrderHeader, Contact
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
def index(request):
    return HttpResponse("Congratulation,first page")

def order(request):
    spicy=Spicy.objects.all()
    dish=Dish.objects.all()
    context={'spicy':spicy}
    context['dish']=dish
    return render(request,'order/order.html',context)

def createOrder(request):
    if request.method == 'GET':
        cn = request.GET['customer_name']
        newOrderHeader = OrderHeader(customer_name=cn, creation_time=datetime.datetime.now())
        newOrderHeader.save();
        lastOrder = OrderHeader.objects.all().order_by('pk').first()
        print(lastOrder.order_num)
        res = {"order_num": lastOrder.order_num}
        return JsonResponse({"order_num": lastOrder.order_num}, status=200)  # Sending an success response
    elif request.method == 'POST':
        received_json_data = json.loads(request.body)
        customer_name = received_json_data['customer'];
        order_line = received_json_data['orderLine'];
        print(order_line)
        order_header = OrderHeader(customer_name=customer_name, creation_time=datetime.datetime.now())
        order_header.save();
        for item in order_line:
            order_dish = Dish.objects.get(dish_name=item['dish'])
            order_spicy = Spicy.objects.get(spicy_name=item['spicy'])
            order_qty = item['qty']
            order_header.orderline_set.create(dish=order_dish, qty=order_qty, spicy=order_spicy)
        return JsonResponse({"order_num": order_header.order_num}, status=200)  # Sending an success response



def detail(request,order_number):
    print("order number is " + order_number)
    order = OrderHeader.objects.get(order_num=order_number)
    d = order.orderline_set.all()
    for i in d:
        print(i.spicy)
    context = {'orderDetail': order}
    return render(request, 'order/detail.html', context)



@api_view(['GET', 'POST'])
def contact_list(request):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    if request.method == 'GET':

        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    try:
        contact = Contact.objects.get(pk=pk)
    except contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)