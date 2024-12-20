def print_header(title):
    """Print a formatted header for menu sections."""
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title))

def get_user_input(prompt, allowed_values=None):
    """Get and validate user input."""
    while True:
        user_input = input(prompt)
        if allowed_values and user_input not in allowed_values:
            print(f"Invalid input. Please choose from: {', '.join(allowed_values)}")
        else:
            return user_input
        
def display_table(data, headers):
    """Display data in a tabular format."""
    if not data:
        print("No data available.")
        return

    # Print the headers
    print(" | ".join(headers))
    print("-" * (len(" | ".join(headers))))

    # Print the rows
    for row in data:
        print(" | ".join(str(item) for item in row))

def confirm_action(action):
    """Ask the user to confirm an action."""
    while True:
        confirmation = input(f"Are you sure you want to {action}? (yes/no): ").lower()
        if confirmation in ("yes", "no"):
            return confirmation == "yes"
        print("Invalid input. Please type 'yes' or 'no'.")

