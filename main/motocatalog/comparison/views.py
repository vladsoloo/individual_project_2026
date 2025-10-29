from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ComparisonSession, ComparisonItem
from motorcycles.models import Motorcycle

def add_to_comparison(request):
    if request.method == 'POST':
        motorcycle_id = request.POST.get('motorcycle_id')
        motorcycle = get_object_or_404(Motorcycle, id=motorcycle_id)
        
        # Получаем или создаем сессию сравнения
        if request.user.is_authenticated:
            session, created = ComparisonSession.objects.get_or_create(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            session, created = ComparisonSession.objects.get_or_create(
                session_key=session_key,
                user=None
            )
        
        # Проверяем лимит (макс 4 мотоцикла)
        if ComparisonItem.objects.filter(session=session).count() >= 4:
            messages.warning(request, 'Максимум 4 мотоцикла для сравнения')
        else:
            ComparisonItem.objects.get_or_create(session=session, motorcycle=motorcycle)
            messages.success(request, f'{motorcycle} добавлен к сравнению')
    
    return redirect(request.META.get('HTTP_REFERER', 'motorcycle_list'))

def comparison_view(request):
    if request.user.is_authenticated:
        session = ComparisonSession.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        session = ComparisonSession.objects.filter(session_key=session_key).first()
    
    comparison_items = ComparisonItem.objects.filter(session=session) if session else []
    motorcycles = [item.motorcycle for item in comparison_items]
    
    return render(request, 'comparison/comparison.html', {
        'motorcycles': motorcycles
    })