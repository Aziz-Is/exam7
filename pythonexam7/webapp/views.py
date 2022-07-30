from django.shortcuts import render
from .models import Poll, Choice
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import MyForm, MyChoiceForm
from django.shortcuts import render, redirect

# Create your views here.

class PollListView(ListView):
    model = Poll
    template_name = 'home.html'
    context_object_name = 'polls'
    paginate_by = 5
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['polls']= Poll.objects.all().order_by('-created_at')
        print(context)
        return context


class DetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        poll = Poll.objects.get(pk=context['pk'])
        context['poll']= poll
        context['choices'] = poll.choices.all()
        return context

class AddView(TemplateView):
    template_name = 'add.html'
    form = MyForm
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['myform'] = self.form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            new_poll = Poll.objects.create(question=form.cleaned_data['question'])
            return redirect('home')
        return render(request, 'add.html', {'myform': form})

class AddChoiceView(TemplateView):
    template_name = 'add_choices.html'
    form = MyChoiceForm
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['myform'] = self.form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            new_choice = Choice.objects.create(text=form.cleaned_data['text'], poll=form.cleaned_data['poll'])
            return redirect('home')
        return render(request, 'add_choices.html', {'myform': form})



class UpdateView(TemplateView):
    template_name = 'add.html'
    form = MyForm
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        poll = Poll.objects.get(pk=context['pk'])
        context['myform'] = self.form(initial={'question':poll.question})
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            poll = Poll.objects.get(pk=kwargs['pk'])
            poll.question = form.cleaned_data['question']
            poll.save()
            return redirect('home')
        return render(request, 'add.html', {'myform': form})

class UpdateChoiceView(TemplateView):
    template_name = 'add_choices.html'
    form = MyChoiceForm
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        choice = Choice.objects.get(pk=context['pk'])
        context['myform'] = self.form(initial={'text':choice.text, 'poll': choice.poll})
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            choice = Choice.objects.get(pk=kwargs['pk'])
            choice.text = form.cleaned_data['text']
            choice.poll = form.cleaned_data['poll']
            choice.save()
            return redirect('home')
        return render(request, 'add_choices.html', {'myform': form})



class DeleteView(TemplateView):
    template_name = 'delete.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['poll']= Poll.objects.get(pk=context['pk'])
        return context
    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=kwargs['pk'])
        if poll:
            poll.delete()
            return redirect ('home')
        return render(request, 'delete.html', {'poll': poll})

class DeleteChoiceView(TemplateView):
    template_name = "delete_choice.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['choice']= Choice.objects.get(pk=context['pk'])
        return context

    def post(self, request, *args, **kwargs):
        choice = Choice.objects.get(pk=kwargs['pk'])
        if choice:
            choice.delete()
            return redirect('home')
        return render(request, 'delete_choice.html', {'choice': choice})
