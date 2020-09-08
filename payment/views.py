from django.shortcuts import render
from django.http import HttpResponse
from .models import DetailCard
from .form import DetailForm
from gateways.abstract import ExpensivePaymentGateway, CheapPaymentGateway, PremiumPaymentGateway
# Create your views here.

expensive_payment_gw = ExpensivePaymentGateway()
cheap_payment_gw = CheapPaymentGateway()
premium_payment_gw = PremiumPaymentGateway()


def process_payment(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            transaction.save()
            if cheap_payment_gw.can_process_transaction(transaction):
                cheap_payment_gw.process(transaction)
            elif expensive_payment_gw.can_process_transaction(transaction):
                if expensive_payment_gw.is_available():
                    expensive_payment_gw.process(transaction)
                else:
                    cheap_payment_gw.process_with_retries(
                        transaction, retry_count=1)
            elif premium_payment_gw.can_process_transaction(transaction):
                premium_payment_gw.process_with_retries(
                    transaction, retry_count=3)
            return HttpResponse('200 OK')
        return HttpResponse('400 bad request')
    else:
        form = DetailForm()
    return render(request, 'payment.html', {'form': form})
