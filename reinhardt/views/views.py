from decimal import Decimal, InvalidOperation

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def touchnet_post_receiver(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    pmt_amt = Decimal(request.POST.get('pmt_amt'))
    pmt_status = request.POST.get("pmt_status")
    posting_key = request.POST.get("posting_key")
    transaction_id = request.POST.get("EXT_TRANS_ID")

    if posting_key != settings.TOUCHNET["POST_KEY"]:
        raise ValueError("Invalid POST key supplied for TouchNet payment.")

    try:
        # Do something if object matching transaction_id exists
        # Ex.
        # transaction = Transaction.objects.get(pk=transaction_id)
        pass
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        raise ValueError(f"Invalid transaction id {transaction_id} on TouchNet payment.")

    try:
        amount = Decimal(pmt_amt)
    except (TypeError, InvalidOperation):
        raise ValueError("Invalid payment amount provided on TouchNet payment.")

    if not (Decimal("1.00") <= amount <= Decimal("100000.00")):
        raise ValueError("Invalid payment amount provided on TouchNet payment.")

    if pmt_status == "success":
        # Do something if pmt_status is success
        pass
    else:
        # Do something if unsuccessful payment
        pass

    return HttpResponse(status=200)
