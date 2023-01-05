from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', 
                  {'name': 'Cool'}) 

def password(request):
    characters = list('qwertyuiopåasdfghjklöäzxcvbnm')
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPÅASDFGHJKLÖÄZXCVBNM')
    
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    
    if request.GET.get('special'):
        characters.extend('!#%&/=?*>')
    
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', 
                  {'pass': thepassword})