from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PerfumeForm
from .models import Perfume


def index(request):
    all_perfume = Perfume.objects.all()
    paginator = Paginator(all_perfume, settings.ELEMENTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'perfumes/index.html', context)


def perfume_detail(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    context = {
        'perfume': perfume
    }
    return render(request, 'perfumes/detail.html', context)


@login_required
def perfume_create(request):
    form = PerfumeForm(
        request.POST or None
    )
    if form.is_valid():
        form.save()
        return redirect('perfumes:index')
    return render(request, 'perfumes/perfume_form.html', {'form': form})


@login_required
def perfume_edit(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    form = PerfumeForm(
        request.POST or None,
        instance=perfume
    )
    if form.is_valid():
        perfume.save()
        return redirect('perfumes:perfume_detail', perfume_id=perfume_id)
    context = {
        'form': form,
        'perfume': perfume,
        'is_edit': True
    }
    return render(request, 'perfumes/perfume_form.html', context)


@login_required
def perfume_delete(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    perfume.delete()
    return redirect('perfumes:index')
