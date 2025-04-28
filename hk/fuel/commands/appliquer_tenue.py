from django.core.management.base import BaseCommand
from django.utils.timezone import now
from fuel.models import BankOperation

class Command(BaseCommand):
    help = "Appliquer les frais de tenue de compte bancaire chaque mois"

    def handle(self, *args, **kwargs):
        today = now()
        premier = today.replace(day=1, hour=0, minute=0, second=0)
        operations = BankOperation.objects.filter(date__gte=premier).exclude(type_operation='tenue')
        total = operations.count()
        montant = 2000 if total < 20 else 4000

        BankOperation.objects.create(
            type_operation='tenue',
            montant=montant,
            motif=f"Tenue de compte automatique ({total} transactions)",
            effectué_par=None,
        )
        self.stdout.write(self.style.SUCCESS(f"Frais de {montant} FBu appliqué avec succès."))
