from .serializers import ArticleSerializer,Article
from rest_framework import viewsets
  
class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    comented below is the real one can be used for more 
    customization
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# from .serializers import ArticleSerializer,Article
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
#     )

# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer