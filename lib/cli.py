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

def developer_menu():
    print("\n=== Developer Management ===")
    print("1. Create Developer")
    print("2. List Developers")
    print("3. Find Developer by ID")
    print("4. Delete Developer")
    print("5. Back to Main Menu")
    return input("Choose an option: ")

def game_menu():
    print("\n=== Game Management ===")
    print("1. Create Game")
    print("2. List Games")
    print("3. Find Game by ID")
    print("4. Delete Game")
    print("5. Back to Main Menu")
    return input("Choose an option: ")

def library_menu():
    print("\n=== Library Menu ===")
    print("1. View Games")
    print("2. Add Game")
    print("3. Remove Game")
    print("4. Back to Main Menu")
    return input("Choose an option: ")

def search_menu():
    print("\n=== Search Menu ===")
    print("1. Search Games by Name")
    print("2. Search Games by Genre")
    print("3. Search Games by Developer")
    print("4. Back to Main Menu")
    return input("Choose an option: ")

def account_menu():
    print("\n=== Account Menu ===")
    print("1. View Account Information")
    print("2. Edit Account Information")
    print("3. Back to Main Menu")
    return input("Choose an option: ")
