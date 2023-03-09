from django.urls import path
from .views import ImageCreate, ImageList, GetImage

urlpatterns = [
    path('images/', ImageCreate.as_view(), name='images-create'),
    path('images/<int:pk>/', ImageList.as_view(), name='images-list-create'),
    path('public/images/<int:pk>/', GetImage.as_view(), name='get-Image')
]


