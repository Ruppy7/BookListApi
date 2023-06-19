from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from .models import BookItem, Category
from .serializers import BookItemSerializer #, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
'''
@api_view()
def books(request):
    return Response('List of books', status = status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of the books by "+ author}, status.HTTP_200_OK)
        return Response({"message": "list of the books"}, status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"message": "new book created"}, status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, request, pk):
        return Response({"message": "single book with id "+ str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title": request.data.get("title")}, status.HTTP_200_OK)
        '''
'''        
class BookList(generics.ListCreateAPIView):
    queryset = BookItem.objects.select_related('category').all()
    serializer_class = BookItemSerializer
    '''
@api_view(['GET','POST'])
def BookList(request):
    if request.method == "GET":
        items = BookItem.objects.select_related('category').all()
        serialized_item = BookItemSerializer(items,many=True)
        return Response(serialized_item.data)
    if request.method == "POST":
        serialized_item = BookItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception = True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def SingleBook(request, id):
    item = get_object_or_404(BookItem, pk=id)
    serialized_item = BookItemSerializer(item)
    return Response(serialized_item.data)

''' Comment - 1 #Ref - serializers.py file
class CreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer'''