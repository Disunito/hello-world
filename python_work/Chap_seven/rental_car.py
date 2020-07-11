inquiry = "What kind of car would you like to rent?"
inquiry += "\nPlease name a Make of car: "
car = input(inquiry)

make = ['audi', 'ford', 'dodge', 'subaru', 'jeep', 'toyota', 'tesla', 'honda']

if car in make:
    print(f"\nGive us a moment as we get your {car.title()} ready!")
else:
    print(f"\nWe are sorry, we do not have any cars of that Make avaliable.")
