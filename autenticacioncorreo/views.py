import re
from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import  

# Create your views here.

#recibir los datos enviados por POST
def recibirdireccion(request):
    # if request.method == 'GET':
    #     print('se conecto por get')
    

    # else:
    #    print(request.POST)
    #    print('obteniendo datos')

    return render(request, 'recibirdireccion.html')      


def direccionRecibida (request):

    if request.POST["correo"]:

         #mensaje = "La direccion de correo electronico recibida es: %r" %request.POST["correo"]
         correointroducido = request.POST["correo"]

         #como buscar en la base de datos
         mensaje = "la direccion es: " + correointroducido

        
    else:
        mensaje = "No introduciste una direccion de correo electronico"

        

    return HttpResponse(mensaje)