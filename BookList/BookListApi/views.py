from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import BookItem, Category
from .serializers import BookItemSerializer #, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
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
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default = 2)
        page = request.query_params.get('page',default=1)
        if category_name:
            items = items.filter(category__title = category_name)
        if to_price:
            items = items.filter(price = to_price)
        if search:
            items = items.filter(title__istartswith = search)
        if ordering:
            #items = items.order_by(ordering) Single ordering parameter
            ordering_fields = ordering.split(",")  #Multiple ordering parameters
            items = items.order_by(ordering_fields)
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
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

@api_view()
@permission_classes({IsAuthenticated})
def secret(request):
    return Response({'message' : 'some secret message'})

''' Comment - 1 #Ref - serializers.py file
class CreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer'''
    
#Easier way of settling everything upto pagination using built in classes
class BookItemsViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()   
    serializer_class = BookItemSerializer
    ordering_fields = ['price','inventory']
    search_fields = ['title', 'Category_title']