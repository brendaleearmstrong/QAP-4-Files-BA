# File: sd10-qap4-python-ba.py
# Desc: Python program to calculate insurance premiums
# Auth: Brenda Armstrong
# Date: 2023-11-27
# Vers: 1.4.0
# Note: This program calculates insurance premiums based on the number of cars insured, extra liability coverage,
#       glass coverage, and loaner car coverage. It also calculates the monthly payment based on the payment method
#       and down payment. The program also displays the receipt and previous claims.

import re
from datetime import datetime, timedelta

# Constants
NEXT_POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_FOR_ADDITIONAL_CARS = 0.25
COST_EXTRA_LIABILITY_COVERAGE = 130.00
COST_GLASS_COVERAGE = 86.00
COST_LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99

# Lists to store claims
claims = []

# Function to validate postal code format
def validate_postal_code(postal_code):
    while not re.match(r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$', postal_code):
        print("Invalid postal code. Please enter a valid postal code.")
        postal_code = input("Postal Code (A#A #A#): ")
    return postal_code

# Function to validate phone number format
def validate_phone_number(phone_number):
    while not re.match(r'^\d{3}-\d{3}-\d{4}$', phone_number):
        print("Invalid phone number. Please enter a valid phone number.")
        phone_number = input("Phone Number (###-###-####): ")
    return phone_number

# Function to validate Y/N input
def validate_yn(value):
    while value.upper() not in ['Y', 'N']:
        print("Invalid input. Please enter 'Y' or 'N'.")
        value = input("Enter 'Y' for Yes or 'N' for No: ")
    return value.upper()

# Function to convert Y/N to Yes/No in uppercase
def convert_yn(value):
    return "Yes" if value == "Y" else "No"

# Function to convert a string to title case
def title_case(s):
    return ' '.join(word.capitalize() for word in s.split())

# Function to get the first monthly payment date
def get_first_monthly_payment_date():
    current_date = datetime.today()
    next_month_date = current_date + timedelta(days=30)
    return next_month_date.strftime('%Y-%m-%d')

# Function to calculate the insurance premium
def calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    total_cost_extra_coverage = (
        num_cars * (COST_EXTRA_LIABILITY_COVERAGE * extra_liability +
                   COST_GLASS_COVERAGE * glass_coverage +
                   COST_LOANER_CAR_COVERAGE * loaner_car)
    )
    discount = (num_cars - 1) * DISCOUNT_FOR_ADDITIONAL_CARS
    total_premium = BASIC_PREMIUM * (1 - discount) + total_cost_extra_coverage
    return total_premium

# Function to calculate HST
def calculate_hst(total_premium):
    return total_premium * HST_RATE

# Function to calculate total cost
def calculate_total_cost(total_premium, hst):
    return total_premium + hst

def calculate_monthly_payment(total_cost, down_payment=0):
    monthly_payment = max((total_cost - down_payment + PROCESSING_FEE) / 8, 0)
    return monthly_payment

def add_claim():
    while True:
        add_claim_option = input("Do you want to add a claim? (Y or N): ").upper()
        if add_claim_option == "Y":
            while True:
                claim_date = input("Enter the claim date (YYYY-MM-DD) or press Enter to finish: ")
                if not claim_date:
                    break  # Exit loop if the user presses Enter
                try:
                    claim_date_obj = datetime.strptime(claim_date, "%Y-%m-%d")
                    if claim_date_obj > datetime.today():
                        print("Claim date cannot be in the future. Please enter a valid date.")
                    else:
                        claim_amount = float(input("Enter the claim amount: $"))
                        claims.extend([claim_date, claim_amount])
                        break  # Exit the inner loop if the date is valid
                except ValueError:
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        elif add_claim_option == "N":
            break  # Exit the outer loop if the user doesn't want to add more claims
        else:
            print("Invalid option. Please enter Y or N.")

# Function to display the receipt
def display_receipt(client_info, insurance_info, payment_info, claims):
    print("-" * 78)
    print("The One Stop Insurance Company".rjust(40) + f'{"Invoice Date:":<20} {datetime.today().strftime("%Y-%m-%d")}')
    print("Car Insurance Policy Invoice".rjust(40) + f'{"Receipt No:":<20} #{insurance_info["invoice_num"]}')
    print()

    # Policy Holder Information
    print(f'Policy Holder: {title_case(client_info["fname"])} {title_case(client_info["lname"])}')
    print(f'Phone: {client_info["phone"]}')
    print(f'Address: {title_case(client_info["address"])}')
    print(f'{title_case(client_info["city"])}, {client_info["province"]} {client_info["postal_code"]}')
    print()

    # Coverage Inclusions
    print("Coverage Inclusions:")
    print(f'Number of Cars: {insurance_info["num_cars"]}')
    print(f'Extra Liability: {validate_yn(insurance_info["extra_liability"])}')
    print(f'Glass Coverage: {validate_yn(insurance_info["glass_coverage"])}')
    print(f'Loaner Car Coverage: {validate_yn(insurance_info["loaner_car"])}')
    print()

    # Coverage Information
    print("Coverage Information:")
    print(f'{"Extra Liability Price:":<40}${insurance_info["ex_liability_cost"]:.2f}')
    print(f'{"Glass Coverage Price:":<40}${insurance_info["glass_cov_cost"]:.2f}')
    print(f'{"Loaner Vehicle Payment:":<40}${insurance_info["loan_cov_cost"]:.2f}')
    print()

    # Premium Breakdown
    print("Premium Breakdown:")
    print(f'{"Policy Premium:":<40}${insurance_info["total_premium"]:.2f}')
    print(f'{"HST (15%):":<40}${insurance_info["hst"]:.2f}')
    print(f'{"Total Cost:":<40}${insurance_info["total_cost"]:.2f}')
    print(f'{"Down Payment:":<40}${payment_info["down_payment"]:.2f}')
    print(f'{"Processing Fee:":<40}${PROCESSING_FEE:.2f}')
    print(f'{"Monthly Payment:":<40}${payment_info["monthly_payment"]:.2f}')
    print()

    # First Monthly Payment Date
    print("First Monthly Payment Date: " + f'{get_first_monthly_payment_date()}')
    print()

    # Claims Information
    print("Previous Claim Information:")
    print(f'{"Claim #":<12}{"Claim Date":<15}{"Amount":<15}')
    print("-" * 40)
    for i, (claim_date, claim_amount) in enumerate(claims, start=1):
        print(f'{i}. {claim_date:<15}${claim_amount:,.2f}')
    print("-" * 40)

# Function to get client information
def get_client_info():
    print("-" * 40)
    print("Welcome to The One Stop Insurance Company")
    print("_" * 40)
    print("Enter Client Information:")
    fname = input("First Name: ").title()
    lname = input("Last Name: ").title()
    address = input("Address: ").title()
    city = input("City: ").title()
    province_list = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC"]
    province = input("Province (e.g. ON): ").upper()
    while province not in province_list:
        print("Invalid province. Please enter a valid 2-letter abbreviation.")
        province = input("Province): ").upper()
    postal_code = validate_postal_code(input("Postal Code (A#A #A#): "))
    phone_number = validate_phone_number(input("Phone Number (###-###-####): "))
    return {
        "fname": fname,
        "lname": lname,
        "address": address,
        "city": city,
        "province": province,
        "postal_code": postal_code,
        "phone": phone_number
    }

# Function to get insurance information
def get_insurance_info():
    print()
    print("Enter Insurance Information:")
    global NEXT_POLICY_NUMBER
    num_cars = int(input("Number of Cars Being Insured: "))
    
    # Validate extra liability input
    extra_liability = 1 if validate_yn(input("Extra Liability Coverage? (Y or N): ")) == 'Y' else 0
    
    # Validate glass coverage input
    glass_coverage = 1 if validate_yn(input("Glass Coverage? (Y or N): ")) == 'Y' else 0
    
    # Validate loaner car input
    loaner_car = 1 if validate_yn(input("Loaner Car Coverage? (Y or N): ")) == 'Y' else 0

    total_premium = calculate_insurance_premium(
        num_cars,
        extra_liability,
        glass_coverage,
        loaner_car
    )

    hst = calculate_hst(total_premium)

    total_cost = calculate_total_cost(total_premium, hst)

    insurance_info = {
        "num_cars": num_cars,
        "extra_liability": extra_liability,
        "glass_coverage": glass_coverage,
        "loaner_car": loaner_car,
        "total_premium": total_premium,
        "invoice_num": NEXT_POLICY_NUMBER,
        "ex_liability_cost": num_cars * COST_EXTRA_LIABILITY_COVERAGE,
        "glass_cov_cost": num_cars * COST_GLASS_COVERAGE,
        "loan_cov_cost": num_cars * COST_LOANER_CAR_COVERAGE,
        "hst": hst,
        "total_cost": total_cost
    }

    NEXT_POLICY_NUMBER += 1
    return insurance_info

# Function to get payment information
def get_payment_info(total_cost):
    print()
    print("Enter Payment Information:")
    payment_option_list = ["Full", "Monthly", "Down Pay"]
    payment_option = input("Payment Option (Full, Monthly, or Down Pay): ").title()
    while payment_option not in payment_option_list:
        print("Invalid payment option. Please enter Full, Monthly, or Down Pay.")
        payment_option = input("Payment Option (Full, Monthly, or Down Pay): ").title()

    if payment_option == "Down Pay":
        down_payment = float(input("Enter the down payment amount: $"))
    else:
        down_payment = 0

    if payment_option == "Monthly" or payment_option == "Down Pay":
        monthly_payment = calculate_monthly_payment(total_cost, down_payment)
    else:
        monthly_payment = 0

    return {
        "payment_option": payment_option,
        "down_payment": down_payment,
        "monthly_payment": monthly_payment
    }

# Main function
def main():
    global claims

    while True:
        client_info = get_client_info()
        insurance_info = get_insurance_info()
        total_premium = calculate_insurance_premium(
            insurance_info["num_cars"],
            insurance_info["extra_liability"],
            insurance_info["glass_coverage"],
            insurance_info["loaner_car"]
        )
        hst = calculate_hst(total_premium)
        total_cost = calculate_total_cost(total_premium, hst)
        payment_info = get_payment_info(total_cost)

        add_claim()

        payment_info["invoice_date"] = get_first_monthly_payment_date()
        display_receipt(client_info, insurance_info, payment_info, claims)

        another_client = validate_yn(input("Would you like to add another client? (Y or N): "))
        if another_client == 'N':
            break

if __name__ == "__main__":
    main()
