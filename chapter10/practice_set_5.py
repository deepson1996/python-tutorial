class Train:
    railway = "Indian Railway"
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def book(self):
        print("===========Book=======")
        if self.seats > 0:
            print(f"Your ticket has been booked and your sear number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry this train is full")
        print("===========Book=======")
        
    def status(self):
        print("===========status=======")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("===========status=======")

        

    def getFare(self):
        print("===========Fare=======")
        print(f"The price of the ticket is : {self.fare}")
        print("===========Fare=======")

    def cancel(self):
        print("=========Cancel========")
        print("Your seat has been cancelled")
        self.seats = self.seats+1
        print("=========Cancel========")


intercity = Train("Indian Express", 4000, 3)
intercity.status()
intercity.book()
intercity.book()
intercity.book()
intercity.book()
intercity.book()
intercity.status()
intercity.cancel()
intercity.status()
intercity.getFare()



