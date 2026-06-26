from rest_framework import serializers
from .models import Post, Categoria, Comentario
from .validators import no_badword

class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categoria
       fields = ['id', 'name', 'slug']
      

class PostSerializer (serializers.ModelSerializer):
    titulo = serializers.CharField(validators=[no_badword] )
    categoria = serializers.SlugRelatedField(
        queryset = Categoria.objects.all(), 
        slug_field = 'slug',
        allow_null = True,
        required= False
    )
    categoria_info = CategoriaSerializer(
        source = 'categoria',
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
        'id', 'titulo', 'autor', 'content', 'criado_em', 
        'categoria',
        'categoria_info'
        ]
        
        read_only_fields = ['id', 'criado_em', 'autor', 'categoria_info']

        # CAMPO ESPECIFICO
        def validate_titulo(self, value):
            if len(value) < 10:
                raise serializers.ValidationError("não pode ter menos que 10 caracteres")
            if value[0].isdigit():
                raise serializers.ValidationError('titulo não pode começar com numeros')
            return value
        
        #CAMPOS GERAIS
        def validate(self, data):
            content = data.get('content', '')
            category = data.get('category')
            if category and len(content) < 10:
                raise serializers.ValidationError({
                    'content': 'posts com categorias não podem tem menos de 10 caracteres'
                })
            return data

class ComentarioSerializer(serializers.ModelSerializer):
    autor_nome = serializers.CharField(source = 'autor.username', read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'content', 'criado_em', 'autor_nome']
        read_only_fields= ['id', 'criado_em', 'autor_nome']

         