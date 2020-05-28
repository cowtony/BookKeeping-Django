import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from book.forms import TransactionForm
from book.models import Transaction

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Transaction

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "book/about.html")

def contact(request):
    return render(request, "book/contact.html")

def hello_there(request, name):
    return render(
        request,
        'book/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def addTransaction(request):
    form = TransactionForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.time = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "book/add_transaction.html", {"form": form})

def deleteTransaction(request, transaction_id):
    Transaction.objects.filter(id=transaction_id).delete()

    # 重定向
    return redirect("home")
   