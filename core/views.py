from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorii, Topics
from .forms import NewTopicForm, NewCommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    categorii = Categorii.objects.all()
    return render(request, 'core/index.html', {'categorii': categorii})

@login_required
def topics(request, pk):
    # categorie = Categorii.objects.get(pk=pk)
    categorie = get_object_or_404(Categorii, pk=pk)

    return render(request, 'core/topics.html', {'categorie': categorie})

@login_required
def postari(request, pk, topic_pk):
    # topic = Topics.objects.get(categorie__pk=pk, pk=topic_pk)
    topic = get_object_or_404(Topics, categorie__pk=pk, pk=topic_pk)
    return render(request, 'core/discutii.html', {'topic': topic})


@login_required
def new_topic(request, pk):
    # categorie = Categorii.objects.get(pk=pk)
    categorie = get_object_or_404(Categorii, pk=pk)

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.categorie = categorie
            topic.save()
            return redirect('core:topics', pk=categorie.pk)
    else:
        form = NewTopicForm()
    return render(request, 'core/reteta noua.html', {'categorie':categorie, 'form':form})


@login_required
def new_post(request, pk, topic_pk):
    topic = get_object_or_404(Topics, categorie__pk=pk, pk=topic_pk)

    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.topic = topic
            message.save()
            return redirect('core:discutii', pk=pk, topic_pk=topic_pk)
    else:
        form = NewCommentForm()
    return render(request, 'core/comentariu nou.html', {'topic':topic, 'form':form})