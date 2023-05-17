import plugingIn
import factory
import json

def main() -> None:

    with open('./config.json') as f:
        data = json.load(f)

        plugingIn.load_register(data['modules'])

        farm = [factory.makeFromJson(**animal_stats) for animal_stats in data['animals']]

        for animal in farm:
            animal.do()

    
if __name__ == '__main__':
    main()