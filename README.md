# Urban Style Barbershop

A Python console application built to practice structured prompting, AI-assisted development, functions, input validation, conditional logic, and clean code organization.

The project simulates a simple pricing and receipt system for a barbershop while applying different pricing rules based on customer status.

## Features

- Interactive command-line interface
- Customer status handling
- Frequent-client discounts
- First-visit-of-the-month discounts
- New-client pricing rules
- Reusable yes/no input validation
- Invalid haircut price validation
- Dynamic welcome messages
- Receipt generation
- Clear separation between pricing and receipt logic

## Business Rules

The base haircut price is **$350.00**.

| Customer condition | Price rule |
| --- | --- |
| New client | Full price |
| Returning frequent client | 15% discount |
| Returning client on first visit of the month | 20% discount |
| Frequent client + first visit of the month | 20% discount |
| Regular returning client | Full price |

The first-visit discount has priority over the frequent-client discount, and discounts are never combined.

New clients are not asked whether they are frequent clients or whether it is their first visit of the month.

## Input Validation

The application uses a reusable `ask_yes_no()` function to validate yes/no questions.

It:

- accepts `yes` and `no`
- ignores capitalization
- removes leading and trailing spaces
- rejects invalid values
- keeps asking until the user provides a valid answer

Example:

```text
Are you a new client? (yes/no): maybe
Invalid input. Please enter yes or no.
Are you a new client? (yes/no): yes
```

## Main Functions

### `generate_welcome()`

Calculates the correct haircut price according to the customer's status and returns the corresponding welcome message.

### `generate_receipt()`

Receives the customer name and welcome message and returns a formatted receipt.

### `ask_yes_no()`

Handles reusable validation for yes/no user input.

## Example

```text
Enter your name: Antonio
Are you a new client? (yes/no): no
Are you a frequent client? (yes/no): yes
Is this your first visit of the month? (yes/no): no

--- Urban Style Receipt ---
Customer: Antonio
Welcome back to Urban Style! Your haircut costs $297.50 with your frequent client discount.
```

## Technologies

- Python 3.13
- uv
- Git
- GitHub
- Visual Studio Code
- GitHub Copilot

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Anthonymanuelm97/urban-style-barbershop.git
```

Move into the project directory:

```bash
cd urban-style-barbershop
```

Run the application with uv:

```bash
uv run main.py
```

## What I Practiced

This project was developed as part of my AI Builder learning path.

The main focus was not only writing Python code, but learning how to work effectively with an AI coding assistant through structured prompts.

I practiced how to:

- create functionality from a prompt
- modify existing functionality without breaking previous behavior
- combine multiple functions
- extend existing business logic
- identify ambiguous business requirements
- refine AI-generated code through better prompts
- validate user input
- review generated code instead of accepting it automatically
- organize a small Python project for readability

One additional improvement beyond the original exercise was separating **new clients** from **returning clients making their first visit of the month**, preventing conflicting pricing rules.

## Project Status

Completed as a learning and portfolio project.