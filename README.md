# Streaming-Smart-Planner
 A personalized OTT movie planner based on mood, time, platform, and industry.


# 🎬 Streaming Smart Planner

A personalized movie/episode recommender built with Python that tailors your entertainment options based on:

- 😄 **Mood** (happy, romantic, thriller)
- ⏱️ **Time available** (e.g., 1h 30m)
- 📺 **Platform preference** (Netflix or Prime)
- 🌏 **Industry** (Hollywood, Bollywood, Tollywood)

## 💡 Features

- 🎯 Avoids long movies if you’re short on time
- 🔁 Never recommends repeats — uses a watch history file
- 🎭 Filters by mood, time, OTT platform, and origin
- 📚 Contains 100+ diverse movie/show entries

## 🚀 How It Works

1. User provides their mood, time, platform, and (optional) industry.
2. The app filters movies/shows from the dataset.
3. Randomly recommends something you've not watched yet.
4. Saves it to your watch history.

## 🛠 Built With

- Python 3
- 30DaysOfPython concepts:
  - File Handling
  - Functions
  - Lists & Dictionaries
  - String Manipulation
  - Random Module
  - Conditional Logic

## 📂 Project Structure

```
StreamingSmartPlanner/
├── main.py            # Main program logic
├── data.py            # Dataset of 100 movies/shows
├── utils.py           # Time parsing helper
├── history.txt        # Watch history log
└── README.md          # Project description (this file)
```

## ▶️ Run the Project

Open terminal inside the project folder and run:

```bash
python main.py
```

## 📌 Example

```
What's your mood (happy, romantic, thriller)? happy
How much time do you have? (e.g., 1h 20m): 45m
Preferred platform (Netflix or Prime)? Netflix
Preferred industry (Hollywood, Bollywood, Tollywood or leave blank for any): Bollywood

🎬 Recommended: Dil Dhadakne Do (43 mins) on Netflix [Bollywood]
```

---

👥 Created by the me as part of the #30DaysOfPython Challenge 💻
