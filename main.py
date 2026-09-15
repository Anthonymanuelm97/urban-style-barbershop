customer_name = input("Enter your name: ")

new_client_answer = input(
    "Are you a new client? (yes/no): ").strip().lower()
is_new_client = new_client_answer == "yes"

if is_new_client:
    frequent_answer = "no"
    first_visit_answer = "no"
else:
    frequent_answer = input(
        "Are you a frequent client? (yes/no): ").strip().lower()

    first_visit_answer = input(
        "Is this your first visit of the month? (yes/no): ").strip().lower()

is_frequent = frequent_answer == "yes"
is_first_visit = first_visit_answer == "yes"


def generate_welcome(business_name, haircut_price, frequent_client,
                     first_visit_this_month=False, new_client=False):
    """Return a welcome message with the final haircut price already calculated."""
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
        discounted_price = haircut_price - \
            (haircut_price * first_visit_discount / 100)
        return (
            f"Welcome to {business_name}! "
            f"Your haircut costs ${discounted_price:.2f} "
            f"with your first visit discount."
        )

    if frequent_client:
        discounted_price = haircut_price - \
            (haircut_price * frequent_client_discount / 100)
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


welcome_message = generate_welcome(
    business_name="Urban Style",
    haircut_price=350,
    new_client=is_new_client,
    frequent_client=is_frequent,
    first_visit_this_month=is_first_visit
)

print(generate_receipt(customer_name, welcome_message))
