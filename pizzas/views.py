from django.shortcuts import render

from .models import Pizza


def index(request):
    """The home page for pizzeria"""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.object.order_by("date_added")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, topic_id):
    """Show a single pizza and all its toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.entry_set.order_by("-date_added")
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)
