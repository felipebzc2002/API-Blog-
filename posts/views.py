from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria, Comentario
from .serializers import PostSerializer, CategoriaSerializer, ComentarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import PostPagination


from rest_framework import viewsets
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filterset_fields = ['categoria__slug', 'autor__username']
    search_fields = ['titulo', 'content']
    ordering_fields = ['criado_em', 'titulo' ]
    ordering = ['-criado_em']
    pagination_class = PostPagination

####################################################################################################################################################
# RELACIONAR O AUTOR AO POST 
#################################################################################################################################################### 
 
    def perform_create(self, serializer):
        serializer.save(autor = self.request.user)

class ComentarioViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comentario.objects.filter(post_id=self.kwargs['post_pk'])
    
    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(autor = self.request.user, post=post )
        # autor é o usuário Logado
        

        