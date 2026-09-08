name = "Carlos"
age = 30
height = 1.75
is_client = True

print(name)
print(type(name))

business_name = "Urban Style Barbershop"
haircut_price = 350
discount_percentage = 15
frequent_client = False

discounted_price = haircut_price - (haircut_price * discount_percentage / 100)

if frequent_client:
    message = (
        f"Welcome back to {business_name}! "
        f"Your haircut costos ${discounted_price:.2f} "
        f"with your frequent client discount. "
    )
else:
    message = (
        f"Welcome to {business_name}! "
        f"Your haircut costs ${haircut_price:.2f}. "
    )

print(message)


