

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Motorcycle, Brand
from comparison.forms import ComparisonForm

def motorcycle_list(request):
    motorcycles = Motorcycle.objects.all()
    
    # Фильтрация
    brand_filter = request.GET.get('brand')
    type_filter = request.GET.get('type')
    year_from = request.GET.get('year_from')
    year_to = request.GET.get('year_to')
    
    if brand_filter:
        motorcycles = motorcycles.filter(brand__id=brand_filter)
    if type_filter:
        motorcycles = motorcycles.filter(motorcycle_type=type_filter)
    if year_from:
        motorcycles = motorcycles.filter(year__gte=year_from)
    if year_to:
        motorcycles = motorcycles.filter(year__lte=year_to)
    
    brands = Brand.objects.all()
    return render(request, 'motorcycles/list.html', {
        'motorcycles': motorcycles,
        'brands': brands
    })

def motorcycle_detail(request, pk):
    motorcycle = get_object_or_404(Motorcycle, pk=pk)
    comparison_form = ComparisonForm(initial={'motorcycle_id': motorcycle.id})
    return render(request, 'motorcycles/detail.html', {
        'motorcycle': motorcycle,
        'comparison_form': comparison_form
    })
