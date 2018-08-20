from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html',{'valuse':['If you have any questions, then ask them by phone', 'something number']})