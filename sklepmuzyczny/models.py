from django.db import models
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey('auth.User')
    active = models.BooleanField(default=True)
    sum_price = models.FloatField(default=0)
    
    created_date = models.DateTimeField(
            default=timezone.now)

    def create_order(cart, request):
        for cartentry in cart.cartentry_set.all():
            if cartentry.count > cartentry.disc.available_count:
                return False
            cart.sum_price+= cartentry.count * cartentry.disc.price
        for cartentry in cart.cartentry_set.all():
            disc = cartentry.disc
            disc.available_count-=cartentry.count
            disc.save()
        imie=request.get('imie', '')
        nazwisko=request.get('nazwisko', '')
        ulica=request.get('ulica', '')
        telefon=request.get('telefon', '')
        miasto=request.get('miasto', '')
        kodpocztowy=request.get('kodpocztowy', '')
        Order.objects.create(cart=cart, 
                             imie=imie,
                             nazwisko=nazwisko,
                             ulica=ulica,
                             telefon=telefon,
                             kodpocztowy=kodpocztowy,
                             miasto=miasto,
                             sum_price=cart.sum_price)
        cart.active = False     
        cart.save()
        return True
    def __str__(self):
        return "Koszyk uzytkownika:" + self.user.username
        
class Disc(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    price = models.FloatField(default=10.50)
    available_count = models.IntegerField()
    carts = models.ManyToManyField(Cart)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.title

class CartEntry(models.Model):
    cart = models.ForeignKey(Cart)
    disc = models.ForeignKey(Disc)
    count = models.IntegerField()

    created_date = models.DateTimeField(
            default=timezone.now)
    
class Order(models.Model):
    cart = models.ForeignKey(Cart)
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    miasto = models.CharField(max_length=200)
    ulica = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    kodpocztowy = models.CharField(max_length=200)
    sum_price = models.FloatField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.cart.__str__() + "  " + str(self.created_date)