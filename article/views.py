from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serialize=ArticleSerializer(articles, many=True)
#         return Response({'articles': serialize.data})
#
#     def post(self, request):
#         article = request.data.get('article')
#
#         serialize=ArticleSerializer(data=article)
#         if serialize.is_valid(raise_exception=True):
#             article_saved = serialize.save()
#
#         return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
#
#     def put(self, request, pk):
#         article_saved=get_object_or_404(Article.objects.all(), pk=pk)
#         data=request.data.get('article')
#         serialize=ArticleSerializer(instance=article_saved, data=data, partial=True)
#         if serialize.is_valid(raise_exception=True):
#             saved_article=serialize.save()
#
#         return Response({"success": "Article '{}' updated successfully".format(saved_article.title)})
#
#     def delete(self, request, pk):
#         article_saved = get_object_or_404(Article.objects.all(), pk=pk)
#         article_saved.delete()
#         return Response({"success": "Article '{}' deleted successfully".format(article_saved.title)})

class ArticleListPostView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



