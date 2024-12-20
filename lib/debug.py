from models.game import Game
from models.developer import Developer

def debug():
    print("Setting up debug environment...")

    print("\n--- Developers ---")
    Developer.create_table()
    dev1 = Developer(name="Nintendo")
    dev1.save()
    dev2 = Developer(name="Sony")
    dev2.save()
    print(Developer.get_all())

    print("\n--- Games ---")
    Game.create_table()
    game1 = Game(name="The Legend of Zelda", genre="Adventure", developer_id=dev1.id)
    game1.save()
    game2 = Game(name="God of War", genre="Action", developer_id=dev2.id)
    game2.save()
    print(Game.get_all())

if __name__ == "__main__":
    debug()
