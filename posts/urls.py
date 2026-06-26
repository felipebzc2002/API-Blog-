from django.urls import path
from .views import PostViewSet, CategoriaViewSet, ComentarioViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter(trailing_slash = False)
router.register('posts', PostViewSet, basename='post')
router.register('categorias', CategoriaViewSet, basename='categoria') 

post_router = routers.NestedDefaultRouter(router, 'posts', lookup = 'post')
post_router.register("comentarios", ComentarioViewSet, basename="post-comentarios" )

urlpatterns = router.urls + post_router.urls