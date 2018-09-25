from django.urls import path

from . import views

urlpatterns = [
    path('^$', views.index, name='index'),
    #path('boards/<board_id>$', views.board_detail, name='board_detail'),
    path(r'boards', views.board_detail, name='board_detail'),
]
