from django.shortcuts import render
from .models import Author, Entry

def queries(request):
    #Obtener todos los elementos de la tabla Author
    authors = Author.objects.all()

    #Obtener datos filtrados de la tabla Author
    filtered = Author.objects.filter(email='devin38@example.org')
    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered})
