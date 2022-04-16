from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class league(models.Model):
    users = models.ManyToManyField(User, related_name="league")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    game_code = models.CharField(max_length=1000)
    starting_balance = models.DecimalField(decimal_places=2,max_digits=100)
    trading_active = models.BooleanField()
    def __str__(self):
        return f"{self.name}"

class lauth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    league = models.ForeignKey(league,on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2,max_digits=100)

class stocks(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2,max_digits=100)
    league = models.ForeignKey(league, on_delete=models.CASCADE, related_name="stocks")
    listed = models.BooleanField()

    class Meta:
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"{self.name}"

class news(models.Model):
    title = models.CharField(max_length=10000)
    stock = models.ForeignKey(stocks, on_delete=models.CASCADE, related_name="news")
    description = models.CharField(max_length=10385760)
    created_at = models.DateTimeField(auto_now_add=True)
    league = models.ForeignKey(league, on_delete=models.CASCADE, related_name="news")

    class Meta:
        verbose_name_plural = "News"
    def __str__(self):
        return f"{self.title}"

class holdings(models.Model):
    stock = models.ForeignKey(stocks, on_delete=models.CASCADE, related_name='holdings')
    quantity = models.IntegerField()
    average_price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='holdings')
    created_at = models.DateTimeField(auto_now_add=True)
    league = models.ForeignKey(league, on_delete=models.CASCADE, related_name="holdings")
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10000)


    class Meta:
        verbose_name_plural = "Holdings"
    
    
class transaction(models.Model):
    ttype_choices = (('BUY','BUY'),('SELL','SELL'),('SHORT','SHORT'),('SQUARE OFF','SQUARE OFF'))
    ttype = models.CharField(max_length=100,choices = ttype_choices)
    stock = models.ForeignKey(stocks, on_delete=models.CASCADE, related_name='transaction')
    quantity = models.IntegerField()
    buy_price = models.DecimalField(decimal_places=2,max_digits=100)
    total_investment = models.DecimalField(decimal_places=2,max_digits=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transaction')
    created_at = models.DateTimeField(auto_now_add=True)
    league = models.ForeignKey(league, on_delete=models.CASCADE, related_name="transaction")


class transfer(models.Model):
    ttype_choices = (('PENDING','PENDING'),('ACCEPTED','ACCEPTED'),('DECLINED','DECLINED'),('INVALID','INVALID'))
    stock = models.ForeignKey(stocks, on_delete=models.CASCADE, related_name='transfer')
    quantity = models.IntegerField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transfer_to')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transfer_from')
    league = models.ForeignKey(league, on_delete=models.CASCADE, related_name="transfer")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices = ttype_choices)
    active = models.BooleanField()

class ipo(models.Model):
    stock = models.ForeignKey(stocks, on_delete=models.CASCADE, related_name='ipo')
    total_quantity = models.IntegerField()
    quantity_per_user = models.IntegerField()
    league = models.ForeignKey(league, on_delete=models.CASCADE, related_name="ipo")
    status = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "IPOs"

    def __str__(self):
        return f"{self.stock}"

class ipo_application(models.Model):
    ipo = models.ForeignKey(ipo, on_delete=models.CASCADE, related_name='ipo_application')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "IPO Applications"

    def __str__(self):
        return f"{self.ipo}"

