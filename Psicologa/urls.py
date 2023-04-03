from django.urls import path
from Psicologa import views

app_name='Psicologa'
urlpatterns = [
    path('',views.PsicologaList.as_view(), name="list"),
    path('create/', views.PsicologaCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.PsicologaUpdate.as_view(), name="update"),
    path('detail/<int:pk>/', views.Psicologadetail.as_view(), name="detail"),
    path('delete/<int:pk>/', views.PsicologaDelete.as_view(), name="delete"),
]