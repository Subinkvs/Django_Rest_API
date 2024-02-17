from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer

# Create your views here.

'''API function'''
@api_view(['GET', 'POST', 'PUT'])
def index(request):
    if request.method == 'GET':
        people_detail = {
            'name': 'Subin',
            'age': '28',
            'job': 'Python developer'
        }
        return Response(people_detail)
    
    elif request.method == 'POST':
        return Response("POST METHOD")
    
    elif request.method == 'PUT':
        return Response('PUT METHOD')
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])  
def person(request):
    if request.method == 'GET':
        personobj = Person.objects.filter(team__isnull=False)
        serializer = PersonSerializer(personobj, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data=data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'Person deleted'})