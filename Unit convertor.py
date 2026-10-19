#9th program-Unit convertor
print("Unit Convertor")
print("1. Kilometer to Meter")
print("2. Meter to Kilometer")

choice = int(input("Enter your choice:"))
value = float(input("Enter the value:"))

if choice == 1:
    print("Meters =", value * 1000)

elif choice ==2:
    print("Kilometers =", value / 1000)

else:
    print("Invalid choice")
