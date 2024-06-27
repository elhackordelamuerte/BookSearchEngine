from django import forms
from .models import Auteur, Livre, Edition

"""
cote = models.CharField(max_length=20)
    auteur = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING)
    titre = models.CharField(max_length=100)
    annee = models.CharField(max_length=4, default=None)
    quantite = models.IntegerField(default=1)
    observation = models.CharField(max_length=256, default=None)

"""
class FormLivre(forms.ModelForm):
    auteur = forms.ModelChoiceField(queryset = Auteur.objects.all(), label='Auteur')
    edition = forms.ModelChoiceField(queryset = Edition.objects.all(), label='Edition')

    class Meta:
        model = Livre
        fields = ['cote','titre', 'auteur', 'edition','annee','quantite', 'observation']
        labels = {'titre': 'Titre', 'quantite':'Quantité', 'annee':'Année'}
        

class FormAuteur(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom']
        