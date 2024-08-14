from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_app import models
from django.core.paginator import Paginator
from django_app import serializers
from pathlib import Path
from django.conf import settings

def index(request):

    file_exists = Path(settings.BASE_DIR / 'frontend/build/index.html').exists()
    print(f"Файл существует: {file_exists}")

    context={}

    print("index")
    return render(request=request, template_name = 'index.html', context=context, status=status.HTTP_200_OK)

def users(request):
    return JsonResponse({"response": "Ok!"})

@api_view(http_method_names = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
@permission_classes([AllowAny])
def chat(request, sms_id=None):
    try:
        if sms_id:
            if request.method == "GET":            
                return Response(status=status.HTTP_200_OK)
            elif request.method == "PUT" or request.method == "PATCH":
                return Response(status=status.HTTP_200_OK)
            elif request.method == "DELETE":
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            if request.method == "GET":            
                page = int(request.GET.get("page", 1))
                limit = int(request.GET.get("limit", 3))

                object_list = models.TextModel.objects.all()
                paginator_obj = Paginator( object_list = object_list, per_page= limit)
                current_page = paginator_obj.get_page(page).object_list
                serialized_object_list = serializers.TextModelSerializer(instance=current_page, many=True).data
                response = {"list": serialized_object_list, "x-total-count": len(object_list)}
                return Response(data=response, status=status.HTTP_200_OK)
                
                  
            elif request.method == "POST":
                text = int(request.GET.get("rext", ""))
                if text:
                    models.TextModel.objects.create(
                        text=text
                    )
                    return Response(status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as error:
        print(error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  