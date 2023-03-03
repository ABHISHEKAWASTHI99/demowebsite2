from django.shortcuts import render

# Create your views here.
def home(request):
    author='Saul Goodman'
    age=50
    address='Mexico'
    ctx={'athr':author, 'age':age, 'addr':address}
    return render(request, 'home.html',context=ctx)


