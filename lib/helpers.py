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