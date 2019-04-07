from django.shortcuts import render

def myfunc(request):
    return render(request, 'tictactoe/welcome.html')
