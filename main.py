def generate_welcome(business_name, haircut_price, frequent_client,
                     first_visit_this_month=False, new_client=False):
    """Return a welcome message with the final haircut price calculated."""
    frequent_client_discount = 15
    first_visit_discount = 20

    if haircut_price <= 0:
        return "Invalid price"

    if new_client:
        return (
            f"Welcome to {business_name}! "
            f"Your haircut costs ${haircut_price:.2f}."
        )

    if first_visit_this_month:
        discounted_price = haircut_price - (
            haircut_price * first_visit_discount / 100
        )
        return (
            f"Welcome to {business_name}! "
            f"Your haircut costs ${discounted_price:.2f} "
            f"with your first visit discount."
        )

    if frequent_client:
        discounted_price = haircut_price - (
            haircut_price * frequent_client_discount / 100
        )
        return (
            f"Welcome back to {business_name}! "
            f"Your haircut costs ${discounted_price:.2f} "
            f"with your frequent client discount."
        )

    return (
        f"Welcome to {business_name}! "
        f"Your haircut costs ${haircut_price:.2f}."
    )


def generate_receipt(customer_name, welcome_message):
    """Return a formatted multi-line receipt for a customer."""
    return (
        "--- Urban Style Receipt ---\n"
        f"Customer: {customer_name}\n"
        f"{welcome_message}"
    )


def ask_yes_no(question):
    """Ask for a yes/no answer and return it as a boolean."""
    while True:
        answer = input(question).strip().lower()

        if answer == "yes":
            return True

        if answer == "no":
            return False

        print("Invalid input. Please enter yes or no.")


customer_name = input("Enter your name: ")

is_new_client = ask_yes_no("Are you a new client? (yes/no): ")

if is_new_client:
    is_frequent = False
    is_first_visit = False
else:
    is_frequent = ask_yes_no(
        "Are you a frequent client? (yes/no): "
    )
    is_first_visit = ask_yes_no(
        "Is this your first visit of the month? (yes/no): "
    )


welcome_message = generate_welcome(
    business_name="Urban Style",
    haircut_price=350,
    new_client=is_new_client,
    frequent_client=is_frequent,
    first_visit_this_month=is_first_visit,
)

print(generate_receipt(customer_name, welcome_message))
