from django.shortcuts import render
from .models import table, order
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
import datetime

table = table.objects.all() 

this_day = datetime.datetime.now()
this_day_str = str(this_day.year) + '-'+ str(this_day.month) + '-' + str(this_day.day)

def index(request):
    if request.method == "POST":
        order_my = order.objects.all() 
        order_my.create(name=request.POST.get("name"), email=request.POST.get("email"), data = request.POST.get("data"), table = request.POST.get("tableitem"))

        send_mail('Заказ', 'Вы заказали стол №' + request.POST.get("tableitem") + ' - на ' + request.POST.get("data"), request.POST.get("email"), ['artemdegtyrov@gmail.com', request.POST.get("email")],fail_silently=False,)
        return redirect(request.path)
    else:
        order_all = order.objects.all() 
        return render(request, "index.html", {"table": table, "order": order_all, "this_day": this_day_str})
    
def table_ajax(request):
    data_this = request.GET.get('data')
    array = []
    order_all = order.objects.all() 
    for order_item in order_all:
        if(data_this == str(order_item.data)):
            array.append(order_item.table)   
            
    return JsonResponse({
        'item': array,
        'data': data_this,
    })
