from django.db import models

# A chaque modification du modele, python manage.py makemigrtions <nomappli>
# python3 manage.py sqlmigrate cale 0001 pour tester la base de données
# python manage.py migrate pour effectuer la migration
# Relancer le serveur

#un modele/classe par table
class Auteur(models.Model):
    nom = models.CharField (max_length= 50, unique = True)
    
    def __str__(self):
        return self.nom

class Edition(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nom


class Livre(models.Model):
    cote = models.CharField(max_length=20)
    auteur = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING)
    titre = models.CharField(max_length=100)
    annee = models.CharField(max_length=4, default=None)
    quantite = models.IntegerField(default=1)
    observation = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.titre
