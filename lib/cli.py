from models.game import Game
from models.developer import Developer
from database import get_connection

def main_menu():
    print("\n=== Game Database CLI ===")
    print("1. Manage Developers")
    print("2. Manage Games")
    print("3. Library Menu")
    print("4. Search Menu")
    print("5. Account Menu")
    print("6. Exit")
    return input("Choose an option: ")