from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.

'''Class based APIView'''
class PersonView(APIView):
    def get(self,request):
       personobj = Person.objects.filter(team__isnull=False)
       serializer = PersonSerializer(personobj, many=True)
       return Response(serializer.data)
   
    def post(self,request):
       data = request.data
       serializer = PersonSerializer(data=data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors)

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
    
class PersonViewSets(viewsets.ModelViewSet):
    serializer_class= PersonSerializer
    queryset = Person.objects.all()
    
    def list(self,request):
        search = request.GET.get("search")
        queryset = self.queryset
        
        if search:
            queryset = queryset.filter(name__startswith = search)
            
        serializer = PersonSerializer(queryset, many=True)
        return Response({'status':200, 'data':serializer.data})