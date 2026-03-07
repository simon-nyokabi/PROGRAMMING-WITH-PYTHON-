def generate_invoice(hours_worked, hourly_rate=50, tax_rate = 0.30):
    gross_total= hours_worked * hourly_rate
    tax_amount = gross_total * tax_rate
    take_home = gross_total - tax_amount

    summary = (
        f"Gross Total: {gross_total}"
        f"\nTax amount: {tax_amount}"
        f"\nTake-Home: {take_home}"
    )
    return summary
hours = float(input("Hours worked:"))
print(generate_invoice(hours))




