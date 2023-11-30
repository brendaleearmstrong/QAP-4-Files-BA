## QAP 4 - Project 2 - Create a Github Repository and add a Readme file outlining the Python project.

Python Program - Insurance Premium Calculator
This is a Python program that calculates insurance premiums based on the number of cars insured, extra liability coverage, glass coverage, and loaner car coverage. It also calculates the monthly payment based on the payment method and down payment. The program also displays the receipt and previous claims.

## Author

Brenda Armstrong

## Version

1.4.0

## Date

2023-11-27

## Features

- Calculates insurance premiums based on various factors.
- Validates user input for postal code, phone number, and yes/no questions.
- Calculates the first monthly payment date.
- Stores and displays previous claims.
- Displays a detailed receipt of the insurance policy.

## Usage

To use this program, simply run the `main()` function. The program will prompt you to enter client information, insurance information, and payment information. You can also add claims. After all the information is entered, the program will display a detailed receipt.

## Functions

- `validate_postal_code(postal_code)`: Validates the format of a Canadian postal code.
- `validate_phone_number(phone_number)`: Validates the format of a phone number.
- `validate_yn(value)`: Validates a yes/no input.
- `convert_yn(value)`: Converts a 'Y'/'N' input to 'Yes'/'No'.
- `get_first_monthly_payment_date()`: Calculates the date of the first monthly payment.
- `calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car)`: Calculates the insurance premium.

## Dependencies

- Python 3
- `re` module for regular expressions
- `datetime` module for date and time operations

## License

This project is licensed under the MIT License - see the LICENSE file for details.
