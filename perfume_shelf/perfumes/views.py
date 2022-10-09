from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PerfumeForm
from .models import Comment, Perfume


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
    form = CommentForm()
    perfume_comments = perfume.comments.all()
    context = {
        'perfume': perfume,
        'form': form,
        'perfume_comments': perfume_comments
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


@login_required
def comment_add(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.perfume = perfume
        comment.save()
    return redirect('perfumes:perfume_detail', perfume_id=perfume_id)


@login_required
def comment_delete(request, perfume_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('perfumes:perfume_detail', perfume_id=perfume_id)
