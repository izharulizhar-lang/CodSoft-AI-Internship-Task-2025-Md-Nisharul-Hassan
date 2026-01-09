import random
import time

BRANDING = """
╔═════════════════════════════════════════════════════════╗
║   Coded By: Md Nisharul Hassan | B.tech CSE, NOIDA INTERNATIONALUNIVERSITY                ║
║   LinkedIn: linkedin.com/in/md-nisharul-hassan-256656380 ║
║   #DesiCoder #InternshipWarrior                      ║
╚═════════════════════════════════════════════════════════╝
"""

GRAND_WELCOME = [
    "🌟 Swagat hai Coding Champions! Aaj ke arena mein, AI vs Insaan ka asli battle! 🌟",
    "🔥 Ab rule banayega coding ka king, naam hai: {user}! Best of luck!",
    "🎲 Dekh le dost, aaj Dosti vs Dimaag ki baazi lagne wali hai!"
]

ROUND_DIALOGUES = [
    "🚀 {user}, har move nayi kahani — champion banna hai toh risk uthao!",
    "🧠 Dimag ki taala khol, yaha AI se ladna hai!",
    "😎 Jo darega, woh har jayega — coding mein audacity dikhani hai!",
    "✨ Haar se mat ghabrao, jeet ka mausam aayega!",
    "🦸 Pro coder wahi, jo har round mein enjoy aur confident rahe!"
]

AI_DIALOGUES = [
    "🤖 AI ke thoughts: 'Aaj toh tumhe zor ka jhatka lagayenge!'",
    "🦾 Dekh ke chal, AI ne master plan ready kiya hai!",
    "😋 AI bolta: 'Abhi toh party shuru hui hai!'",
    "👀 AI: 'Aapka sahi logic, mere liye challenge!'"
]

TIPS = [
    "🧩 Tip: Haar jeet ka khel hai, har step self-improvement ka signal hai!",
    "😅 Galat choice mat soch, agli move banake sab change kar de!",
    "🏅 Jeetne ke liye kabhi kabhi risk uthana part of game hai!",
    "😂 Dosti bhi important hai, jitna maza batchmates ke saath coding mein!"
]

SUSPENSE = [
    "🔥 Kya game ka agla round tum sabko surprise karega? Dekhte raho!",
    "⭐ Next level pe paunchne wala hai, kisko milega coding ka crown?",
    "💫 Board ka halat badalne wala hai, aankhon se gaya na chuke!",
    "💡 Champions kabhi dosti nahi chhodte — match abhi bhi baaki hai!"
]

WIN_DIALOGUES = [
    "🙌 {user}, tu sahi mein coding ka Sultan nikla! Badhai ho!",
    "🎊 AI bhi keh raha hai: 'Yeh toh reality show winner hai!'",
    "🏆 LinkedIn par victory post daal de — dhamaka karega!",
    "⭐ Tu ab Intern King hai, aage HR bhi impress hoga!"
]

AI_WIN_DIALOGUES = [
    "😏 AI ne win kar diya! Lekin insan ka passion har defeat se strong hota hai!",
    "💪 Next time fir try kar, upar jaane ke liye failure important hai!",
    "🤖 Machine ki logic jeet gayi — ab tu next level planning seekh!",
    "✊ Coding ke dangal mein haar bhi victory ka pehla step hai!"
]

DRAW_DIALOGUES = [
    "🤝 Wah! Dosti jeet gayi, coding ke maidan mein tie badiya hai!",
    "👏 Both sides Pro! Yahi hai real competition!",
    "😂 Draw ho toh maza double, dosti bhi mission complete!",
    "✨ Pro coder hamesha try karta hai — draw hua toh kya hua, legend ban gaya!"
]

def dramatic_print(text, speed=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(speed)
    print()

def print_branded(text, delay=0.035, user=""):
    if "{user}" in text:
        text = text.replace("{user}", user)
    dramatic_print(text, delay)

def grand_wel(user):
    print(BRANDING)
    for line in GRAND_WELCOME:
        print_branded(line, 0.04, user)
    print("=" * 50)
    time.sleep(0.5)

def suspense(round, user):
    print_branded(SUSPENSE[round % len(SUSPENSE)], 0.04, user)
    print("-" * 33)

def print_board(board, turn, user):
    print_branded(ROUND_DIALOGUES[turn % len(ROUND_DIALOGUES)], 0.039, user)
    print()
    print("    0   1   2")
    for idx, row in enumerate(board):
        print(f" {idx}   " + " | ".join(row))
        if idx < 2:
            print("    ---+---+---")
    print()
    print_branded(TIPS[turn % len(TIPS)], 0.03)
    print("-" * 40)

def is_winner(board, player):
    win_cond = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player]*3 in win_cond

def is_board_full(board):
    return all(" " not in row for row in board)

def get_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0
    if is_maximizing:
        best = -float("inf")
        for i, j in get_moves(board):
            board[i][j] = "O"
            score = minimax(board, False)
            board[i][j] = " "
            best = max(best, score)
        return best
    else:
        best = float("inf")
        for i, j in get_moves(board):
            board[i][j] = "X"
            score = minimax(board, True)
            board[i][j] = " "
            best = min(best, score)
        return best

def best_move(board):
    best = -float("inf")
    move = None
    for i, j in get_moves(board):
        board[i][j] = "O"
        score = minimax(board, False)
        board[i][j] = " "
        if score > best:
            best = score
            move = (i, j)
    return move

def random_ai_move(board):
    moves = get_moves(board)
    return random.choice(moves) if moves else None

def main():
    board = [[" "]*3 for _ in range(3)]
    turn = 1
    user = input("Apna naam likho Coding Superstar: ")
    grand_wel(user)
    difficulty = input("AI ko kitna challenge? (easy/hard): ").strip().lower()
    while difficulty not in ["easy", "hard"]:
        print("Bas type karo: easy ya hard!")
        difficulty = input().strip().lower()

    print_board(board, turn, user)
    suspense(turn, user)

    while True:
        while True:
            try:
                row = int(input(f"[{user}] Row (0-2): "))
                col = int(input(f"[{user}] Col (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("⛔ Bhai, yeh box already full hai! Dusra box choose karo.")
                else:
                    print("Input sirf 0, 1, 2 hi valid hai!")
            except:
                print("Sirf number daalo, pro coder bane raho! (0-2)")
        print_board(board, turn, user)
        if is_winner(board, "X"):
            print_branded(WIN_DIALOGUES[turn % len(WIN_DIALOGUES)], 0.07, user)
            print(BRANDING)
            break
        if is_board_full(board):
            print_branded(DRAW_DIALOGUES[turn % len(DRAW_DIALOGUES)], 0.07, user)
            print(BRANDING)
            break
        suspense(turn+1, user)
        print_branded(AI_DIALOGUES[turn % len(AI_DIALOGUES)], 0.05, user)
        time.sleep(1 if difficulty == "hard" else 0.36)
        if difficulty == "easy":
            move = random_ai_move(board)
        else:
            move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
            print_board(board, turn, user)
            if is_winner(board, "O"):
                print_branded(AI_WIN_DIALOGUES[turn % len(AI_WIN_DIALOGUES)], 0.065, user)
                print(BRANDING)
                break
        if is_board_full(board):
            print_branded(DRAW_DIALOGUES[turn % len(DRAW_DIALOGUES)], 0.07, user)
            print(BRANDING)
            break
        turn += 1

if __name__ == "__main__":
    main()
