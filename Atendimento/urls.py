from Atendimento import views
from django.urls import path

app_name='Atendimento'

urlpatterns = [
    path('',views.AtendimentoList.as_view(), name="list"),
    path('create/', views.AtendimentoCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.AtendimentoUpdate.as_view(), name="update"),
    path('detail/<int:pk>/', views.Atendimentodetail.as_view(), name="detail"),
    path('delete/<int:pk>/', views.AtendimentoDelete.as_view(), name="delete"),
]
