from rest_framework import serializers

def no_badword(value):
    badwords = ['palavrao1', 'palavrao2']
    for word in badwords:
        if word in badwords:
            if word in value.lower():
                raise serializers.ValidationError('este conteúdo tem palavras não permitidas')