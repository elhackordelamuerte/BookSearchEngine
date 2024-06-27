from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Livre, Auteur, Edition
from .forms import FormLivre, FormAuteur
 
"""
    save() ,  delete()
    SELECT      : all(), get()
    INSERT      : create()
    WHERE       : filter()
                    __gt, __lt, __gte, __lte; __startswith (ex : field__gte)
    ORDER BY    : order_by()
    LIMIT       : [:N]    
"""
def testing(request):
    context = {
         "livres": Livre.objects.all().order_by('-id')
     }
    return render(request, "cale/test.html", context)


def index(request):
    context = {
         "livres": Livre.objects.all().order_by('-id')
     }
    return render(request, "cale/index.html", context)


    
@permission_required('cale.delete_livre')
def show(request, livre_id):
    context = {
        "livre" :get_object_or_404(Livre, pk = livre_id)
    }
    return render(request,"cale/show.html", context) #affiche la page template

@login_required
def ajouter_livre(request):
    if request.method == 'POST':
        form =  FormLivre(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("cale:index")
    else:
        form = FormLivre()
        
    return render(request, "cale/form_livre.html", {"form": form})

@login_required
def edit_livre(request, livre_id):
    livre = Livre.objects.get(pk=livre_id)
    
    if request.method == 'POST':
        form =  FormLivre(request.POST, instance = livre)
        
        if form.is_valid():
            form.save()
            return redirect("cale:index")
    else:
        form = FormLivre(instance=livre)
        
    return render(request, "cale/form_livre.html", {"form": form})
    
@login_required
def delete_book(request, livre_id):
    livre = Livre.objects.get(pk=livre_id)
    livre.delete()
    return redirect("cale:index")
    
def ajouter_auteur(request):
    if request.method == 'POST':
        form =  FormAuteur(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("cale:index")
    else:
        form = FormAuteur()
        
    return render(request, "cale/form_auteur.html", {"form": form})

def delete_author(request, auteur_id):
    auteur = Auteur.objects.get(pk=auteur_id)
    auteur.delete()
    return redirect("cale:index")
