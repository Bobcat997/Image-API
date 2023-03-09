from rest_framework import serializers
from .models import Image, Account, Thumbnail
from django.db.models import Q


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'user', 'expiration_seconds']


class ImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ImageListSerializer(serializers.ModelSerializer):
    plan = serializers.SerializerMethodField()
    thumbnails = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = '__all__'

    def get_plan(self, obj):
        return Account.objects.get(user=obj.user).plan.name

    def get_thumbnails(self, obj):
        request = self.context.get('request')
        thumb_200 = Thumbnail.objects.filter(original=obj.id, size=200)
        thumb_400 = Thumbnail.objects.filter(original=obj.id, size=400)
        thumb_custom = Thumbnail.objects.filter(Q(original=obj.id) & ~Q(size=200) & ~Q(size=400))

        thumbnails = {
            '200px': request.build_absolute_uri(thumb_200[0].image.url) if thumb_200 else "",
            '400px': request.build_absolute_uri(thumb_400[0].image.url) if thumb_400 else "",
            'custom': request.build_absolute_uri(thumb_custom[0].image.url) if thumb_custom else "",
        }
        return thumbnails

    def get_image(self, obj):
        request = self.context.get('request')
        plan = Account.objects.get(user=obj.user).plan.name
        if plan.lower() != 'basic':
            return request.build_absolute_uri(obj.image.url)
        else:
            return ""
