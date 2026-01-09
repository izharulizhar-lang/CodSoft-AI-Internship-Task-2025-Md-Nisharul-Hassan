# 💬 CodSoft Internship: Super Fun Hinglish Chatbot 💬
# Coded by Md Nisharul Hassan (B.tech CSE AI/ML, NOIDA INTERNATIONAL UNIVERSITY)
import random

greetings = [
    "👋 Namaste legend! Kaise ho?", 
    "🙌 Hi! Internship ka champion mil gaya!", 
    "😄 Hey coder! Aaj coding me dhamaka karoge?"
]
internship = [
    "🛡️ CodSoft internship? Yeh toh coder banne ka ultimate chance hai!",
    "🚀 Career boost ka mission hai — project banao, learning pao!",
    "🌟 CodSoft: Masti, learning aur LinkedIn achievement! Kya help chahiye?"
]
motivation = [
    "🔥 Darr ke aage jeet hai, coding karo bina rukhe!", 
    "💪 Mehnat ka phal milke rahega, champion!", 
    "🤩 Haar mat maano, aaj ka error kal ki success hai!",
    "📈 Coding hai struggle par magic bhi — fail-ne se mat daro!"
]
creator = [
    "👨‍💻 Mujhe Izharul Hassan ne banaya hai — internship ke asli hero!", 
    "🧑‍💻 Mere creator Izharul Hassan hain, BCA ke coder king!",
    "📝 Yeh chatbot CodSoft internship ke liye special edition hai!"
]
fallback = [
    "🤔 Yeh bot abhi internship practice mode mein hai, fir se poochho!", 
    "😅 Thoda clear batao, tab best jawab milega!", 
    "🪄 Main abhi chatbot sikha raha hoon, professional query puchho!", 
    "🤓 Google bhi try karo, coder sab jagah expert hai!"
]
farewell = [
    "👋 Accha chalo, milte hain agle code session mein!", 
    "🙏 Shukriya! Interview mein coding confidence ke saath jaana!", 
    "✌️ Bye! Aaj coding seekh li, ab LinkedIn post bhi kar do!"
]

def chatbot():
    print("\n🟦 CodSoft Super Chatbot | Hinglish, Internship, Gaming Vibe! 🟦")
    print("Type 'exit' to end. Emoji, fun, and coder swag loaded!\n")
    while True:
        user = input("You: ").lower()
        # End chat
        if user == "exit":
            print("Bot:", random.choice(farewell)); break

        # Greeting
        elif any(greet in user for greet in ["hello", "hi", "namaste", "hey", "yo"]):
            print("Bot:", random.choice(greetings))

        # Internship/task
        elif "codsoft" in user or "internship" in user or "task" in user:
            print("Bot:", random.choice(internship))

        # Motivation/inspire
        elif "motivate" in user or "motivation" in user or "inspire" in user or "inspiration" in user:
            print("Bot:", random.choice(motivation))

        # Creator name
        elif "who made you" in user or "developer" in user or "creator" in user:
            print("Bot:", random.choice(creator))

        # Time/Date
        elif "time" in user:
            from datetime import datetime
            print("Bot: ⏰ Abhi ka time:", datetime.now().strftime('%H:%M:%S'))
        elif "date" in user:
            from datetime import datetime
            print("Bot: 📅 Aaj ki date:", datetime.now().strftime('%d-%m-%Y'))

        # Thanks
        elif "thank" in user or "shukriya" in user:
            print("Bot: 🙏 Welcome legend! Coder ki madad hamesha hoti hai.")

        # How are you/mood
        elif "kaise ho" in user or "how are you" in user or "haal" in user:
            print("Bot: 😃 Bilkul top! Tumhare saath coding kar ke aur bhi best feel ho raha hai.")

        # Fallback - unknown question
        else:
            print("Bot:", random.choice(fallback))

if __name__ == "__main__":
    chatbot()
