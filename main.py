from data import movies
from utils import parse_time
import random

def read_history():
    try:
        with open("history.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_to_history(title):
    with open("history.txt", "a") as f:
        f.write(title + "\n")

def main():
    mood = input("What's your mood (happy, romantic, thriller)? ").strip().lower()
    time_str = input("How much time do you have? (e.g., 1h 20m): ").strip()
    platform = input("Preferred platform (Netflix or Prime)? ").strip().lower()
    industry = input("Preferred industry (Hollywood, Bollywood, Tollywood or leave blank for any): ").strip().title()

    available_time = parse_time(time_str)
    watched = read_history()

    filtered = [
        m for m in movies
        if m['mood'] == mood
        and m['platform'].lower() == platform
        and m['runtime'] <= available_time
        and m['title'] not in watched
        and (industry == '' or m['industry'] == industry)
    ]

    if not filtered:
        print("\n😔 Sorry, no content matched your filters or available time.")
        return

    recommendation = random.choice(filtered)
    print(f"\n🎬 Recommended: {recommendation['title']} ({recommendation['runtime']} mins) on {recommendation['platform']} [{recommendation['industry']}]")
    save_to_history(recommendation['title'])

if __name__ == "__main__":
    main()
