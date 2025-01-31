def adventure_game():
    print("Welcome to the Mysterious Dungeon!")
    print("You find yourself in a dark dungeon with two doors ahead.")
    print("One leads to treasure, the other to danger.")
    
    choice = input("Do you choose the LEFT or RIGHT door? (left/right): ").strip().lower()
    
    if choice == "left":
        print("You enter a room filled with gold and jewels! But a puzzle stands before you.")
        answer = input("Solve this riddle to claim your reward: 'I speak without a mouth and hear without ears. What am I?' (echo/fire): ").strip().lower()
        if answer == "echo":
            print("Correct! The treasure is yours. You win!")
        else:
            print("Wrong! The treasure vanishes into thin air. You leave empty-handed.")
        print("As you turn to leave, another door appears, leading to an underground tunnel.")
        tunnel_choice = input("Do you enter the tunnel? (yes/no): ").strip().lower()
        if tunnel_choice == "yes":
            print("You navigate through the tunnel and find a hidden city of gold! You win!")
        else:
            print("You leave the dungeon, wondering what might have been.")
    
    elif choice == "right":
        print("A fierce dragon appears! You must choose to FIGHT, RUN, or TALK.")
        action = input("What do you do? (fight/run/talk): ").strip().lower()
        
        if action == "fight":
            print("You bravely battle the dragon and emerge victorious! You win!")
        elif action == "run":
            print("You escape safely but leave empty-handed. Maybe next time!")
        elif action == "talk":
            print("The dragon listens and reveals a hidden passage. You find a magical sword and become the dungeon's new protector! You win!")
            print("The dragon, impressed by your wisdom, offers to guide you to an ancient library filled with forbidden knowledge.")
            library_choice = input("Do you follow the dragon to the library? (yes/no): ").strip().lower()
            if library_choice == "yes":
                print("You learn powerful secrets and become a legendary wizard! You win!")
            else:
                print("You decline and leave the dungeon, forever wondering what knowledge you missed.")
        else:
            print("Hesitation leads to defeat! The dragon roars, and you lose.")
    
    else:
        print("Confusion leads you nowhere. Lost in the dungeon, you lose.")
    
if __name__ == "__main__":
    adventure_game()
