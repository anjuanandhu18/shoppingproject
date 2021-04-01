from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import apimodel
from .serializers import ApiModelSerializer


# Create your views here.

@csrf_exempt
def apiview(request):
    if request.method == 'GET':
        restapi = apimodel.objects.all()
        serializer = ApiModelSerializer(restapi, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ApiModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    print('vhjhhjhjhghgh')
    try:
        apimodels = apimodel.objects.get(pk=pk)
    except apimodels.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ApiModelSerializer(apimodels)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ApiModelSerializer(apimodels, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        apimodels.delete()
        return HttpResponse(status=204)
