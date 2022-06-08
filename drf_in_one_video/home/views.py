from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer


# Create your views here.
@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method=='GET':
        return Response({
            'status':200,
            'message':'yow! django rest framwork is working',
            'method_called':'you called GET method',
        })
    elif request.method=='POST':
        return Response({
            'status':200,
            'message':'you! django rest framwork is working',
            'method_called':'you called POST method',
        })
    elif request.method=='PATCH':
        return Response({
            'status':200,
            'message':'you! django rest framwork is working',
            'method_called':'you called PATCH method',
        })
    else:
        return Response({
            'status':400,
            'message':'oops!, you called invalid method:) ',            
        })

@api_view(['POST',])
def post_todo(request):

    try:
        data=request.data
        serializer=TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.dat)

            return Response({
                'status':True,
                'message':'success to do created',
            })

        return Response({
                'status': False,
                'message':'false to perform operations',
            })
        
    except Exception as e:
        print(e)
        