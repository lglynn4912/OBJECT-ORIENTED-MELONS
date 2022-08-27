"""Classes for melon orders."""

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

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5
        
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

