# CodSoft Internship Task 4: Final Professional Recommendation System
# By Md Nisharul Hassan (B.TECH CSE AI/ML,NOIDA INTERNATIONAL UNIVERSITY)
import random

profiles = {
    "Izharul": {
        "movies": ["Inception", "Avengers", "Sholay"],
        "books": ["Atomic Habits", "Deep Work"],
        "songs": ["Believer", "Love Dose"]
    },
    "Payal": {
        "movies": ["Interstellar", "Sholay", "3 Idiots"],
        "books": ["Ikigai", "Deep Work"],
        "songs": ["Shape of You", "Love Dose"]
    },
    "Rahul": {
        "movies": ["Inception", "3 Idiots", "Dangal"],
        "books": ["Atomic Habits", "5AM Club"],
        "songs": ["Tum Hi Ho"]
    }
}

all_catalog = {
    "movies": ["Inception", "Avengers", "Sholay", "Interstellar", "3 Idiots", "Dangal", "KGF", "Bahubali"],
    "books": ["Atomic Habits", "Deep Work", "5AM Club", "Ikigai", "Python Tricks", "Wings of Fire"],
    "songs": ["Believer", "Love Dose", "Shape of You", "Tum Hi Ho", "Let Me Love You"]
}

def recommend(user, category):
    if user in profiles:
        seen = set(profiles[user][category])
        pool = set()
        for other, lists in profiles.items():
            if other != user:
                pool.update(set(lists[category]) - seen)
        # Additional: Recommend new from overall catalog not yet seen
        all_new = set(all_catalog[category]) - seen
        recs = list(pool | all_new)
        random.shuffle(recs)
        return recs[:3] if recs else ["😅 Koi nayi recommendation nahi!"]
    else:
        # New user: Random picks from all catalog
        return random.sample(all_catalog[category], 3)

welcome = [
    f"🟦 Internship warrior, aaj ka recommendation time hai! 😎",
    "🎉 Hi, aaj apne coding break ko super banaate hain!",
    "🚀 CodSoft AI recommends: Must-watch, must-read, must-listen!"
]
ai_talk = [
    "🤖 AI bolta: LinkedIn pe yeh list share karo, panel bhi impress ho jayega!",
    "🧑‍💻 Kaam hua toh masti bhi zaruri — aaj ka suggestion great hoga!",
    "📚 Learning aur entertainment dono ek hi jagah milega.",
]
end_msg = [
    "😎 System mast hai! Next step: LinkedIn post aur GitHub update.",
    "🙌 Internship jeet lo, HR bhi mazaa karega.",
    "📝 Screenshot zaroor upload karo for full marks!"
]

def main():
    print(random.choice(welcome))
    user = input("Apna naam (e.g. Izharul, Payal, Rahul, ya kuch bhi): ").strip()
    category = input("Category choose karo: movies / books / songs: ").strip().lower()
    # Safe check if category exists
    if category not in all_catalog:
        print("⚠️ Galat category! Default: movies")
        category = "movies"
    # Profile show and recommend
    if user in profiles:
        print(f"👤 {user} ne abhi tak dekha/padha/suna: {profiles[user][category]}")
        print(random.choice(ai_talk))
    else:
        print(f"🆕 Welcome {user}! Fresh recommendations just for you!")
        print(random.choice(ai_talk))
    suggestions = recommend(user, category)
    print("✨ Aapke liye special AI recommendations:")
    for item in suggestions:
        print("  -", item)
    print(random.choice(end_msg))
    print("🟦 Powered by CodSoft | Coded by Izharul Hassan 💙")

main()

