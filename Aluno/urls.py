from django.urls import path
from Aluno import views

app_name='Aluno'

urlpatterns = [
    path('',views.AlunoList.as_view(), name="list"),
    path('create/', views.AlunoCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.AlunoUpdate.as_view(), name="update"),
    path('detail/<int:pk>/', views.Alunodetail.as_view(), name="detail"),
    path('delete/<int:pk>/', views.AlunoDelete.as_view(), name="delete"),
]
