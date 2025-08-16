from src.views.main_view import generate_story

def main():
    story = generate_story("Write a one-sentence bedtime story about a unicorn.")
    print(story)

if __name__ == "__main__":
    main()