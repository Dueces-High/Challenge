from django.http import JsonResponse
from .models import Router, Interface
from .serializers import SerialRouter,SerialInterface
from django.http import HttpResponse
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def router_list(request):
    if request.method == 'GET':
        All_Routers = Router.objects.all()
        serializer = SerialRouter(All_Routers, many=True)
    return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = SerialRouter(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def Routerinfo(request, id):

    Router1 = Router.objects.get(pk=id)

    if request.method == 'GET':
        serializer = SerialRouter(Router1)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = SerialRouter(Router1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse("nada")

    elif request.method == 'DELETE':
        Router1.delete()
        return HttpResponse("All Gone")


@api_view(['GET', 'POST'])
def Interfaces(request):
    if request.method == 'GET':
        All_Interfaces = Interface.objects.all()
        serializer = SerialInterface(All_Interfaces, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = SerialInterface(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def Interfacesinfo(request, id):

    Interface1 = Interface.objects.get(pk=id)

    if request.method == 'GET':
        serializer = SerialInterface(Interface1)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = SerialInterface(Interface1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse("nada")

    elif request.method == 'DELETE':
        Interface1.delete()
        return HttpResponse("All Gone")