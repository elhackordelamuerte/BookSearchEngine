from django.urls import path
from . import views

app_name = "cale"

urlpatterns =  [
    path('', views.index, name = 'index'),  # cale/
    path('<int:livre_id>', views.show, name = 'show'),     # cale/<id>
    path('ajouter_livre/', views.ajouter_livre, name = 'ajouter_livre'),
    path('modifier_livre/<int:livre_id>/', views.edit_livre, name = 'edit_livre'),
    path('delete_book/<int:livre_id>/', views.delete_book, name = 'delete_book'),
    path('ajouter_auteur/', views.ajouter_auteur, name = 'ajouter_auteur'),
    path('supprimer_auteur/<int:auteur_id>/', views.delete_author, name = 'supprimer_auteur'),
    path('test/', views.testing, name ='testing')
]