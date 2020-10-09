from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import userreq






@login_required
def userreqs(request):
    context = {
        'userreq': userreq.objects.all()
    }
    return render(request, 'userreq/userreq_page.html', context)


class userreqListView(ListView):
    model = userreq
    template_name = 'userreq/userreq_page.html'
    context_object_name = 'userreq'
    ordering = ['-date_posted']




class userreqDetailView(DetailView):
    model = userreq


class userreqUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = userreq
    fields = ['contact', 'Age', 'Email']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        userreq = self.get_object()
        if self.request.user == userreq.author:
            return True
        return False


class userreqDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = userreq
    success_url = '/'

    def test_func(self):
        userreq = self.get_object()
        if self.request.user == userreq.author:
            return True
        return False




class userreqCreateView(LoginRequiredMixin, CreateView):
    model = userreq
    fields = ['Donor_name', 'contact', 'Age', 'Blood_group', 'City',
              'Email']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

