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

def run():
    Developer.create_table()
    Game.create_table()

    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                dev_choice = developer_menu()
                if dev_choice == "1":
                    name = input("Enter developer name: ")
                    Developer(name=name).save()
                elif dev_choice == "2":
                    print(Developer.get_all())
                elif dev_choice == "3":
                    dev_id = input("Enter developer ID: ")
                    print(Developer.find_by_id(dev_id))
                elif dev_choice == "4":
                    dev_id = input("Enter developer ID: ")
                    Developer.delete(dev_id)
                elif dev_choice == "5":
                    break
                else:
                    print("Invalid choice!")

        elif choice == "2":
            while True:
                game_choice = game_menu()
                if game_choice == "1":
                    name = input("Enter game name: ")
                    genre = input("Enter game genre: ")
                    developer_id = input("Enter developer ID: ")
                    Game(name=name, genre=genre, developer_id=developer_id).save()
                elif game_choice == "2":
                    print(Game.get_all())
                elif game_choice == "3":
                    game_id = input("Enter game ID: ")
                    print(Game.find_by_id(game_id))
                elif game_choice == "4":
                    game_id = input("Enter game ID: ")
                    Game.delete(game_id)
                elif game_choice == "5":
                    break
                else:
                    print("Invalid choice!")

        elif choice == "3":
            while True:
                library_choice = library_menu()
                if library_choice == "1":
                    print(Game.get_all())
                elif library_choice == "2":
                    name = input("Enter game name: ")
                    genre = input("Enter game genre: ")
                    developer_id = input("Enter developer ID: ")
                    Game(name=name, genre=genre, developer_id=developer_id).save()
                elif library_choice == "3":
                    game_id = input("Enter game ID to remove: ")
                    Game.delete(game_id)
                elif library_choice == "4":
                    break
                else:
                    print("Invalid choice!")

        elif choice == "4":
            while True:
                search_choice = search_menu()
                if search_choice == "1":
                    name = input("Enter game name to search: ")
                    with get_connection() as conn:
                        results = conn.execute(
                            "SELECT * FROM games WHERE name LIKE ?", (f"%{name}%",)
                        ).fetchall()
                    print(results)
                elif search_choice == "2":
                    genre = input("Enter game genre to search: ")
                    with get_connection() as conn:
                        results = conn.execute(
                            "SELECT * FROM games WHERE genre LIKE ?", (f"%{genre}%",)
                        ).fetchall()
                    print(results)
                elif search_choice == "3":
                    developer_id = input("Enter developer ID to search games by: ")
                    with get_connection() as conn:
                        results = conn.execute(
                            "SELECT * FROM games WHERE developer_id = ?", (developer_id,)
                        ).fetchall()
                    print(results)
                elif search_choice == "4":
                    break
                else:
                    print("Invalid choice!")

        elif choice == "5":
            while True:
                account_choice = account_menu()
                if account_choice == "1":
                    print("Account Information: [Add logic for account details]")
                elif account_choice == "2":
                    print("Edit Account Information: [Add logic for editing account details]")
                elif account_choice == "3":
                    break
                else:
                    print("Invalid choice!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run()

