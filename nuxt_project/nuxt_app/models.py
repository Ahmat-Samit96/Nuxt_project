from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class BitcoinPrice(models.Model):
    timestamp = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f'Bitcoin Price at {self.timestamp}: {self.price} {self.currency.symbol}'

class PricePeriod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class PriceSnapshot(models.Model):
    bitcoin_price = models.ForeignKey(BitcoinPrice, on_delete=models.CASCADE)
    period = models.ForeignKey(PricePeriod, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    def __str__(self):
        return f'Price Snapshot ({self.period}): {self.bitcoin_price.price} {self.bitcoin_price.currency.symbol} from {self.start_timestamp} to {self.end_timestamp}'

    def average_price(self):
        
        return self.bitcoin_price.price

    def price_change_percentage(self):
        
        if self.start_timestamp != self.end_timestamp:
            change_percentage = ((self.bitcoin_price.price - self.bitcoin_price.price) / self.bitcoin_price.price) * 100
            return round(change_percentage, 2)
        else:
            return 0.0

    def is_price_increasing(self):
     
        return self.end_timestamp > self.start_timestamp and self.bitcoin_price.price > self.bitcoin_price.price

    def get_price_fluctuation(self):
        
        return abs(self.bitcoin_price.price - self.bitcoin_price.price)

    def display_period(self):
       
        return f'{self.period.name} ({self.start_timestamp} to {self.end_timestamp})'
