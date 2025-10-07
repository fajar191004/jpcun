# Tic Tac Toe sederhana untuk 2 pemain

# Membuat papan kosong
board = [" " for _ in range(9)]

# Fungsi menampilkan papan
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # baris
        [0,3,6], [1,4,7], [2,5,8],  # kolom
        [0,4,8], [2,4,6]            # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Mengecek apakah papan penuh
def is_draw():
    return " " not in board

# Main game
def play_game():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(input(f"Pemain {current_player}, pilih posisi (1-9): ")) - 1
            if board[move] != " ":
                print("❌ Posisi sudah terisi! Coba lagi.")
                continue
        except (ValueError, IndexError):
            print("⚠ Masukkan angka 1 sampai 9!")
            continue
        
        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Pemain {current_player} menang!")
            break
        elif is_draw():
            print_board()
            print("🤝 Seri!")
            break
        
        current_player = "O" if current_player == "X" else "X"

play_game()