import random

def load_data(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def generate_story():
    characters = load_data('data/characters.txt')
    settings = load_data('data/settings.txt')
    plot_points = load_data('data/plot_points.txt')
    
    character = random.choice(characters)
    setting = random.choice(settings)
    plot_point = random.choice(plot_points)

    story = f"In the land of {setting}, there was a {character}. One day, {plot_point}."
    return story

if __name__ == "__main__":
    print(generate_story())
