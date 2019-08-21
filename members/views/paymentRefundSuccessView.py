from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from members.utils.user import user_to_person, has_user


@login_required
@user_passes_test(has_user, '/admin_signup/')
def paymentRefundSuccessView(request):
    unique = user_to_person(request.user).family.unique
    return render(request, "members/payment_refund_success.html", {"unique": unique})
