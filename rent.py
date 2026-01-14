# Rent Calculator

# Step 1: Define variables using user input
total_rent = float(input("Enter total house rent (₹): "))
num_people = int(input("Enter number of people sharing the rent: "))

electricity_units = float(input("Enter total electricity units consumed: "))
cost_per_unit = float(input("Enter cost per electricity unit (₹): "))

extra_charges = float(input("Enter additional charges (maintenance, water, etc.) (₹): "))

# Step 2: Calculate electricity bill
electricity_bill = electricity_units * cost_per_unit

# Step 3: Calculate total expenses
total_expenses = total_rent + electricity_bill + extra_charges

# Step 4: Calculate rent per person
rent_per_person = total_expenses / num_people

# Step 5: Display result
print("\n===== Rent Summary =====")
print(f"House Rent           : ₹{total_rent}")
print(f"Electricity Bill     : ₹{electricity_bill}")
print(f"Extra Charges        : ₹{extra_charges}")
print(f"Total Expenses       : ₹{total_expenses}")
print(f"Rent per Person      : ₹{rent_per_person:.2f}")
