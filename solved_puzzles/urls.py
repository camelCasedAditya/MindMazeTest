from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="solved"),
    # Url based on the puzzle id for detailed view
    path("<int:puzzle_id>/", views.detail, name="solved_detail")
]
