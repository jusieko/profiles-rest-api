from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """REturns a list of APIView features"""
        an_appiview= [
            'Uses HTTP methods as function (get, post , patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you applications logic',
            'is mapped manually to urls',

        ]

        return Response({'message':'Hello', 'an_apiview': an_appiview})