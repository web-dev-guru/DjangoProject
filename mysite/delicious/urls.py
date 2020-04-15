from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [


    path('',views.index,name='index'),
    #http://localhost:8000/delicious
    path('order/',views.order,name='order'),
    #http://localhost:8000/delicious/order
    path('createOrder',views.createOrder,name='createOrder'),
    #http://localhost:8000/delicious/createOrder
    #url(r'^order/$',views.order,name='order'),
    url(r'^order/(?P<order_number>[A-Z][0-9]+)/detail', views.detail, name="detail"),

    #rest url pattern
    #get(retrieve) post(add new)
    #put(update) delete(remove)

    path("api/contacts/",views.contact_list, name="contact_list"),

    #http://127.0.0.1:8000/delicious/api/contacts/

    path('api/contact/<int:pk>', views.contact_detail,name="contact_detail")
    #http://127.0.0.1:8000/delicious/api/contact/1(pk)

]