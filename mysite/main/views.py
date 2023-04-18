from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    return render(request, 'home.html')

def calculator(request):
    res = 0
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        char = request.POST.get('char')
        number2 = request.POST.get('number2')
        try:
            if char == '+':
                res = int(number1) + int(number2)
            elif char == '-':
                res = int(number1) - int(number2)
            elif char == '/':
                res = int(number1) / int(number2)
            elif char == '*':
                res = int(number1) * int(number2)
        except Exception as ex:
            res = f'{ex.__class__.__name__} - {datetime.datetime.now()}'
    return render(request, 'calculator.html', context={'result':res})
