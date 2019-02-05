from character_classes.warrior import Warrior

def main():
    new_char = Warrior(
        name='Kevin Arthur',
        strength=40
    )
    print('Character Name:', new_char.name)
    print('Character Strength:', new_char.strength)

if __name__ == '__main__':
    main()
