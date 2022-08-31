"""Classes for melon orders."""

from random import randint
from datetime import datetime

class AbstractMelonOrder:

    def __init__(self, species, qty, holiday):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.holiday = holiday
     
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    
          
    def get_base_price(self):
        
        random_base_price = 5

        current_date_time = datetime.now()

        if current_date_time.hour() >= 17 and current_date_time.hour() <= 3 and current_date_time.weekday() <= 5:
            random_base_price += 4
            
       
        return random_base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.holiday == True:
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total
       
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty, holiday):
        """Initialize melon order attributes."""
        super().__init__(species, qty, holiday)
 

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code, holiday):
        """Initialize melon order attributes."""
        super().__init__(species, qty, holiday)
    
        self.country_code = country_code
        
    def get_total(self):
        total = super().get_total()
        
        if self.qty < 10:
            total += 3
        
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False
    
    def __init__(self, species, qty, holiday):
        super().__init__(species, qty, holiday)

    def mark_inspection(self):
        self.passed_inspection = True