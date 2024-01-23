from salespeople import *
from cars import *
from customers import Customer

def menu():
    print("1. View Cars")
    print("2. Register as Customer")
    print("3. Search Cars")
    print("4. Purchase Car")
    print("For Sales")
    print("5. Manage Car Inventory")
    print("6. View Sales History")



def main():
    choice:int = 0
    while choice != 7:
        menu()
        choice = int(input("Choose: "))

        if choice == 1:
            elcars = Electric_Cars()
            print(elcars.electric_cars())
            hycars = Hybrid_Cars()
            print(hycars.hybrid_cars())

        if choice == 2:
            name = input("Enter your Name: ")
            contact_info = input("Enter your Contact Information: ")
            customer = Customer(name, contact_info)
            print(customer.register_as_user())

        elif choice == 3:
            customer = Customer(0,0)
            make = input("Enter the Make of your Car: ")
            print(customer.search_car(make))

        elif choice == 4:
            customer = Customer(0,0)
            make = input("Enter the Make of your Car: ")
            print(customer.purchase_car(make))

        elif choice == 5:
            sales = Sales_People()
            make = input("Enter the Make of your Car: ")
            print(sales.manage_car_inventory(make))

        elif choice == 6:
            sales = Sales_People()
            print(sales.view_sales_history())

        elif choice == 7:
            break


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(f"An error occurred: {e}")

        try_again = input("Do you want to try again? (y/n): ").lower()
        if try_again != 'y':
            break
