from rest_framework import generics, status
from rest_framework.response import Response
from .models import Image, Account
from .serializers import ImageSerializer, ImageListSerializer, ImageCreateSerializer
from . import helpers
from datetime import datetime, timedelta
from django.views.generic import DetailView


class ImageCreate(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = ImageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        base_image = Image.objects.get(id=serializer.data['id'])
        account = Account.objects.get(user=base_image.user)

        if account.plan.name.lower() in ("premium", "enterprise", "basic"):
            helpers.thumbnail(base_image, 200)
        if account.plan.name.lower() in ("premium", "enterprise"):
            helpers.thumbnail(base_image, 400)
            if account.plan.name.lower() not in ("premium", "basic"):
                base_image.link_expiration_time = datetime.now() + timedelta(seconds=base_image.expiration_seconds)
                base_image.save()
        if account.plan.name.lower() not in ("premium", "enterprise", "basic"):
            helpers.thumbnail(base_image, account.plan.size)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ImageList(generics.ListAPIView):
    serializer_class = ImageListSerializer

    def get_queryset(self):
        return Image.objects.filter(user__id=self.kwargs['pk'])


class GetImage(DetailView):
    model = Image
    template_name = 'images.html'

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context.update({'now': datetime.now()})
        return super().get_context_data(**context)
