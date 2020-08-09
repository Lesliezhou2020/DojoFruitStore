

from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime

def index(request):
    return render(request, "index.html")


def checkout(request):
    context = {}
    if request.method == 'POST':

        # Data fetching
        Strawberry = request.POST['Strawberry_count']
        Raspberry = request.POST['Raspberry_count']
        Apple = request.POST['Apple_count']
        Name = request.POST['name']
        Your_Student_ID = request.POST['id']

        # Business logic
        dt = custom_strftime('%B {S}, %Y %I:%M:%S %p', datetime.now())
        Number = int(Strawberry) + int(Raspberry) + int(Apple)

        # Aggregation
        context = {
            "Total_num": Number,
            "time": dt,
    	    "count1" : Strawberry,
    	    "count2" : Raspberry,
            "count3" : Apple,
            "name": Name,
            "id": Your_Student_ID,
        }      
    return render(request, 'checkout.html', context)


def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))