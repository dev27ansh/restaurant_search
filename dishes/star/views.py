from django.shortcuts import render

from star.models import Item

# Create your views here.
def search_dishes(request):
    query = request.GET.get('q')
    items = Item.objects.filter(name__icontains=query) if query else []
    context = {
        'items': items,
        'query': query,
    }
    return render(request, 'dishes/search_results.html', context)