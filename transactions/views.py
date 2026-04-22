from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .utils import convert_ngn_to_xaf

@api_view(['POST'])
def send_money(request):
    amount = float(request.data['amount'])
    receiver = request.data.get('receiver')
    
    converted, rate = convert_ngn_to_xaf(amount)

    txn = Transaction.objects.create(
        sender=request.user,
        receiver_name=receiver,
        receiver_country="Cameroon",
        amount=amount,
        currency_from="NGN",
        currency_to="XAF",
        exchange_rate=rate,
        status="pending"
    )
    return Response({"message": "Transaction created", "xaf_amount": converted, "rate": rate })



# Create your views here.
