class Car:
    def __init__(self, driver_name, rate_per_mile):
        self.total_earnings = 0
        self.driver_name = driver_name
        self.rate_per_mile = rate_per_mile
    def drive(self, miles):
        trip_cost = miles * self.rate_per_mile 
        self.total_earnings += trip_cost
        print(f"{self.driver_name} drove {miles} and earned ${trip_cost:.2f}")
        
    def cash_out(self):
        print(f"Total driver made: ${self.total_earnings:.2f}")
        self.total_earnings = 0
#test
new_car = Car("Alex",2.5)
new_car.drive(12)
new_car.drive(4)
new_car.cash_out()
