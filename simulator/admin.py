from django.contrib import admin


from .models import ipo_application, league, stocks,news,holdings, transaction,transfer,lauth, ipo

admin.site.site_header = 'DStreet Administration'


@admin.register(league)
class leagueAdmin(admin.ModelAdmin):
    list_display = ("name", "game_code")

@admin.register(ipo)
class leagueAdmin(admin.ModelAdmin):
    list_display = ("stock",)
@admin.register(ipo_application)
class leagueAdmin(admin.ModelAdmin):
    list_display = ("ipo",'user')

@admin.register(stocks)
class stockAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name__startswith",)

@admin.register(news)
class newsAdmin(admin.ModelAdmin):
    list_display = ("title", "stock",'created_at')


@admin.register(holdings)
class holdingsAdmin(admin.ModelAdmin):
    list_display = ("user", "stock",'type')
    list_filter = ("user",'stock','type')
    search_fields = ("user__startswith", 'stock__startswith')


@admin.register(transaction)
class transactionAdmin(admin.ModelAdmin):
    list_display = ("user", "stock",'quantity','buy_price','created_at')
    list_filter = ("user",'stock')
    search_fields = ("user__startswith", 'stock__startswith')

@admin.register(transfer)
class transferAdmin(admin.ModelAdmin):
    list_display = ("to_user", "from_user",'stock','quantity','status')
    list_filter = ("to_user",'stock','from_user')
    search_fields = ("to_user__startswith", 'stock__startswith',"from_user__startswith",)
