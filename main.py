name = "Carlos"
age = 30
height = 1.75
is_client = True

print(name)
print(type(name))

def generate_welcome(business_name, haircut_price, frequent_client):
    """Return a welcome message with the final haircut price already calculated."""
    discount_percentage = 15

    if frequent_client:
        discounted_price = haircut_price - (haircut_price * discount_percentage / 100)
        return (
            f"Welcome back to {business_name}! "
            f"Your haircut costs ${discounted_price:.2f} "
            f"with your frequent client discount."
        )

    return (
        f"Welcome to {business_name}! "
        f"Your haircut costs ${haircut_price:.2f}."
    )


print(generate_welcome("Urban Style Barbershop", 350, False))
print(generate_welcome("Urban Style Barbershop", 350, True))


