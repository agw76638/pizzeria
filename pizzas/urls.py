"""Defines URL patterns for pizzas"""

from django.urls import path

from . import views

app_name = "pizzas"
urlpatterns = [
    # Home page
    path("", view.index, name="index"),
    # Page that shows all topics
    path("pizzas/", views.pizzas, name="pizzas"),
    # Detail page for a single topic
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
]
