from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm, MyModelSearchForm
from .models import Transaction
import re

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Transaction
    template_name = 'book/home.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Transaction.objects.filter(user=self.request.user)
            description_filter_context = self.request.GET.get('description_filter', '')
            if description_filter_context:
                queryset = queryset.filter(Q(description__icontains=description_filter_context))
            return queryset.order_by('-date_time')[:100]  # Limits the results to the most recent 100 rows.
        else:
            return Transaction.objects.none()


    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['form'] = MyModelSearchForm(self.request.GET)
        return context


home_list_view = HomeListView.as_view(
    context_object_name = 'transaction_list',
)


def about(request):
    return render(request, 'book/about.html')


def contact(request):
    return render(request, 'book/contact.html')

@login_required
def addTransaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("home")
    else: # GET
        form = TransactionForm(user=request.user)
        return render(request, "book/add_transaction.html", {"form": form})


def deleteTransaction(request, transaction_id):
    Transaction.objects.filter(id = transaction_id).delete()
    return redirect("home")


# TODO: Currently working as delete
def UpdateTransaction(request, transaction_id):
    if request.method == "GET":
        transaction = Transaction.objects.get(id = transaction_id)
        form = TransactionForm(instance = transaction)
        return render(request, "book/update_transaction.html", {"form": form})
    elif request.method == "POST":
        form = TransactionForm(request.POST)
        message = form.save(commit=False)
        message.save()
        return redirect("home")