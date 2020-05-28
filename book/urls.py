from django.urls import path
from book import views
from book.models import Transaction

home_list_view = views.HomeListView.as_view(
    queryset=Transaction.objects.order_by("-time")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="book/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("addTransaction/", views.addTransaction, name="addTransaction"),
    path('deleteTransaction/<int:transaction_id>', views.deleteTransaction, name='deleteTransaction'),
]

