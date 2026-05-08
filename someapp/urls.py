# from django.urls import path
# from . import views

# urlpatterns = [
#     path('books/', views.BookListMyView.as_view(), name='book_list'),
#     path('author/<int:pk>/', views.AuthorDetailMyView.as_view(), name='author_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.calculator, name='calculator'),
]