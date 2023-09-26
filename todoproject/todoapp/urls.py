from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('Listview/',views.Listview.as_view(),name='Listview'),
    path('cbvdetail/<int:pk>/',views.Detailview.as_view(),name='cbvdetail'),
    path('updateview/<int:pk>/',views.Updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.Deleteview.as_view(),name='deleteview'),
]