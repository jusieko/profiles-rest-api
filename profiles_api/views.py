from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers




class HelloApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializer
    


    def get(self, request, format=None):
        """REturns a list of APIView features"""
        an_appiview= [
            'Uses HTTP methods as function (get, post , patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you applications logic',
            'is mapped manually to urls',

        ]

        return Response({'message':'Hello', 'an_apiview': an_appiview})

    def post(self, request):
        """"create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response ({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk=None):

        """handle updating objects"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete (self, request, pk=None):
        """Delete object"""
        return Response({'method':'DELETE'})
class HelloViewSet(viewsets.ViewSet):

    """TST Api ViewSET"""

    serializer_class=serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset= [
            'User actions(list,create , retrieve, update,partial_update)',
            'Autamitically maps to urls using ruters',
            'Provides more fuionality with less code',

        ]

        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}!'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an obcjet by its Id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ Handle updating object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request, pk=None):
        """handle updating part of an object"""
        return Response ({'http_method':'PATCH'})

    def destroy(self,request, pk=None):
        """handle removing an object"""
        return Response ({'http_method':'DELETE'})





