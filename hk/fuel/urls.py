from django.urls import path
from fuel.views import achat,depense,vente, accueil, way, user, bank

urlpatterns = [
    path('', accueil.dashboard, name='dashboard'),

    path('achats/', achat.fuel_purchase_list, name='fuel_purchase_list'),
    path('ajouter-achat/', achat.create_fuel_purchase, name='create_fuel_purchase'),
    path('modifier-achat/<int:pk>/', achat.edit_fuel_purchase, name='update_fuel_purchase'),
    path('supprimer-achat/<int:pk>/', achat.delete_purchase, name='delete_fuel_purchase'),
    
    path('ventes/', vente.fuel_sale_list, name='fuel_sale_list'),
    path('ajouter-vente/', vente.create_fuel_sale, name='create_fuel_sale'),
    path('modifier-vente/<int:pk>/', vente.edit_fuel_sale, name='update_fuel_sale'),
    path('supprimer-vente/<int:pk>/', vente.delete_sale, name='delete_fuel_sale'),

    path('ways/', way.list_way, name='way_list'),
    path('ajouter-way/', way.create_way, name='create_way'),
    path('modifier-way/<int:pk>/', way.edit_way, name='update_way'),
    path('supprimer-way/<int:pk>/', way.delete_way, name='delete_way'),

    path('depenses/', depense.expense_list, name='expense_list'),
    path('ajouter-depense/', depense.create_expense, name='create_expense'),
    path('modifier-depense/<int:pk>/', depense.edit_expense, name='update_expense'),
    path('supprimer-depense/<int:pk>/', depense.delete_expense, name='delete_expense'),

    path('login/', user.login_view, name='login'),
    path('register/', user.register_view, name='register'),
    path('logout/', user.logout_view, name='logout'),
    path('user/', user.user_list, name='user_list'),
    path('modifier-user/<int:pk>/', user.edit_user, name='update_user'),
    path('supprimer-user/<int:pk>/', user.delete_user, name='delete_user'),

    path('banque/', bank.bank_operation_list, name='bankoperation_list'),
    path('banque/ajouter/', bank.create_bank_operation, name='bankoperation_create'),
    path('banque/modifier/<int:pk>/', bank.update_bank_operation, name='bankoperation_update'),
    path('banque/supprimer/<int:pk>/', bank.delete_bank_operation, name='bankoperation_delete'),
]