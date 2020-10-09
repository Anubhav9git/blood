from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import bankreq, bank






@login_required
def bank(request):
    context = {
        'banks': bankreq.objects.all()
    }
    return render(request, 'bank/bank.html', context)

class bankreqListView(ListView):
    model = bankreq
    template_name = 'bank/bank.html'
    context_object_name = 'banks'
    ordering = ['-date_posted']




class bankreqDetailView(DetailView):
    model = bankreq


class bankreqUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = bankreq
    fields = ['contact', 'Units_of_A_Positive', 'Units_of_A_Negative', 'Units_of_B_Positive','Units_of_B_Negative', 'Units_of_O_Positive', 'Units_of_O_Negative']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        bankreq = self.get_object()
        if self.request.user == bankreq.author:
            return True
        return False


class bankreqDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = bankreq
    success_url = '/'

    def test_func(self):
        bankreq = self.get_object()
        if self.request.user == bankreq.author:
            return True
        return False




class bankreqCreateView(LoginRequiredMixin, CreateView):
    model = bankreq
    fields = ['Hospital_Name', 'Address', 'contact', 'Units_of_A_Positive', 'Units_of_A_Negative', 'Units_of_B_Positive',
              'Units_of_B_Negative', 'Units_of_O_Positive', 'Units_of_O_Negative']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

