from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import ArticleSerializer,Article

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer