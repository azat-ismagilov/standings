from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("success", views.success, name="success"),
    path("parse_teams/", views.parse_teams, name="parse_teams"),
    path("parse_teams_file/", views.parse_teams_file, name="parse_teams_file"),
    path("parse_rating/", views.parse_rating, name="parse_rating"),
    path("process_invoices/", views.process_invoices, name="process_invoices"),
    path(
        "process_invoices/accept/<int:handleinvoice_id>/",
        views.process_invoices_accept,
        name="process_invoices_accept",
    ),
    path(
        "process_invoices/decline/<int:handleinvoice_id>/",
        views.process_invoices_decline,
        name="process_invoices_decline",
    ),
    path("add_handle/", views.add_handle, name="add_handle"),
    path("add_handle/<int:participant_id>/", views.add_handle, name="add_handle_id"),
    path("add_handle/success/", views.add_handle_success, name="add_handle_success"),
]
