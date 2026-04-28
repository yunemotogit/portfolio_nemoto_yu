from generate_sudoku import generate_sudoku, print_board
from sudoku_solver import create_puzzle

def main():
    print("=== 数独パズル自動生成 ===")
    
    # 1. 完成された盤面を生成する
    print("\n[1] 盤面を生成中...")
    complete_board = generate_sudoku()
    if not complete_board:
        print("盤面の生成に失敗しました。")
        return
        
    # 2-6. 盤面に穴を空けてパズルを作成する
    print("\n[2] 問題を作成中...")
    # attempts を調整することで、難易度（穴を空ける試行回数）を調整可能
    puzzle_board, holes = create_puzzle(complete_board, attempts=81)
    
    print(f"\n完成したパズル (空けた穴の数: {holes}):")
    print_board(puzzle_board)
    
    input("\nEnterキーを押すと回答を表示します")
    print("\n[解答]")
    print_board(complete_board)
if __name__ == "__main__":
    main()
