import random
import copy

# --- 今回追加する「穴あけ」ロジック ---

def create_puzzle(full_board, num_holes=36):
    """完成盤面から指定された数の数字を削る"""
    # 元の盤面を壊さないようにコピーを作成
    puzzle = copy.deepcopy(full_board)
    
    # 全81マスの座標リストを作成 (0,0)から(8,8)まで
    all_positions = [(r, c) for r in range(9) for c in range(9)]
    
    # 穴をあける場所をランダムに選ぶ
    holes_to_make = random.sample(all_positions, num_holes)
    
    for r, c in holes_to_make:
        puzzle[r][c] = 0
        
    return puzzle

def print_board(board, title="Sudoku"):
    print(f"\n--- {title} ---")
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = " ".join(str(n) if n != 0 else "." for n in row)
        print(row_str[:6] + "|" + row_str[6:12] + "|" + row_str[12:])

# --- メイン処理 ---

if __name__ == "__main__":
    # 1. 完成盤面（答え）を作る
    answer_board = generate_full_board()
    
    # 2. 36箇所の穴をあけて「問題」を作る
    puzzle_board = create_puzzle(answer_board, num_holes=36)
    
    # 3. 表示
    print_board(puzzle_board, "Puzzle (36 holes)")
    print_board(answer_board, "Answer Key")