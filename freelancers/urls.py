from django.urls import path
from .views import list_freelancers, freelancer_detail, update_portfolio

urlpatterns = [
    path('', list_freelancers),
    path('<int:id>/', freelancer_detail),
    path('<int:id>/portfolio/', update_portfolio),
]
