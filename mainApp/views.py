from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html',{'valuse':['Если у вас остались вопросы, то задавайте их мне по телефону', '+1(676)1234']})