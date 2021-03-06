from django.db import models

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    image = models.URLField(null=True)
    description = models.TextField(default="")
    opened = models.BooleanField(default=False)
    sandbox = models.BooleanField(default=True)
    goal = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return '{} [{}]'.format(self.title, 'opened' if self.opened else 'closed')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('campaign-details', args=[self.slug])

    def collected(self):
        collected = sum(cart.ticket_type.cost
                        for cart in Cart.objects.filter(status=Cart.TICKET_ISSUED, ticket_type__campaign=self))
        return collected


class TicketType(models.Model):
    type = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    campaign = models.ForeignKey(Campaign)

    def __str__(self):
        return '"{}" ticket of <{}>'.format(self.type, self.campaign)


class IssuedTicket(models.Model):
    uid = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    ticket_type = models.ForeignKey(TicketType)

    def __str__(self):
        return self.uid

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('ticket-details', args=[self.uid])


class Cart(models.Model):
    CART_CREATED = 'CREATED'
    TICKET_ISSUED = 'TICKET_ISSUED'
    PAYMENT_FAILED = 'PAYMENT_FAILED'
    PAYMENT_WAIT_ACCEPT = 'PAYMENT_WAIT_ACCEPT'
    UNKNOWN_STATUS = 'UNKNOWN_STATUS'

    name = models.CharField(max_length=200, default='<noname>')
    uid = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    ticket_type = models.ForeignKey(TicketType)
    status = models.CharField(max_length=25, default=CART_CREATED,
                              choices=((CART_CREATED, 'Item in cart'),
                                       (TICKET_ISSUED, 'Payment confirmed, ticket issued'),
                                       (PAYMENT_FAILED, 'Payment failed'),
                                       (PAYMENT_WAIT_ACCEPT, 'Payment is waiting for acceptance...'),
                                       (UNKNOWN_STATUS, 'Unknown status, check LiqPay data')
                              ))
    ticket = models.ForeignKey(IssuedTicket, null=True, default=None)
    hide_money = models.BooleanField(default=False)
    hide_name = models.BooleanField(default=False)
    something = models.CharField(max_length=200, default='<no text>')

    def __str__(self):
        return self.uid


    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('cart-details', args=[self.uid])


class LiqPayData(models.Model):
    cart = models.ForeignKey(Cart)
    timestamp = models.DateTimeField(auto_now=True, null=True)

    lp_action = models.CharField(max_length=50, null=True)
    lp_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    lp_code = models.CharField(max_length=50, null=True)
    lp_currency = models.CharField(max_length=50, null=True)
    lp_err_code = models.CharField(max_length=50, null=True)
    lp_err_description = models.CharField(max_length=255, null=True)
    lp_ip = models.CharField(max_length=50, null=True)
    lp_liqpay_order_id = models.CharField(max_length=50, null=True)
    lp_payment_id = models.IntegerField(null=True)
    lp_paytype = models.CharField(max_length=50, null=True)
    lp_public_key = models.CharField(max_length=50, null=True)
    lp_sender_card_mask2 = models.CharField(max_length=50, null=True)
    lp_status = models.CharField(max_length=50, null=True)
    lp_transaction_id = models.CharField(max_length=50, null=True)
    lp_type = models.CharField(max_length=50, null=True)
