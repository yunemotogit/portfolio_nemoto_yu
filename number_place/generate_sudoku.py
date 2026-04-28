import random

def generate_sudoku():
    # 2次元リスト　9x9の盤面を0（空マス）で初期化
    board = [[0 for _ in range(9)] for _ in range(9)]

    # 1. 最初の1行目を1-9でシャッフルして埋める
    first_row = list(range(1, 10))
    random.shuffle(first_row)
    board[0] = first_row

    # 2. 探索開始　2行目、つまりインデックス[1, 0]から
    if solve(board):
        return board
    return None

def solve(board):
    """深さ優先探索"""
    # 空いているマスを探す（find_empty関数）
    empty = find_empty(board)
    if not empty:
        return True  # 全て埋まったら終了
    
    row, col = empty
    
    # 候補数字を取得（get_candidates関数）
    candidates = get_candidates(board, row, col)
    
    # 候補がない場合の枝刈り
    if not candidates:
        return False
    
    # 探索をバラけさせるために候補もシャッフル（毎回違う盤面にするため）
    random.shuffle(candidates)
    
    for num in candidates:
        board[row][col] = num
        
        # 再帰的に次のマスへ（1つでも解が見つかれば即座にTrueで戻る）
        if solve(board):
            return True
            
        # バックトラッキング
        board[row][col] = 0
        
    return False

def find_empty(board):
    """次に埋めるべき空マスを返す"""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def get_candidates(board, row, col):
    """指定されたマスの候補を取得する"""
    # 使用済み数字チェックリスト　index 0-8 が 数字 1-9 に対応
    is_used = [False] * 9

    # 行と列をチェック
    for i in range(9):
        if board[row][i] > 0:
            is_used[board[row][i] - 1] = True
        if board[i][col] > 0:
            is_used[board[i][col] - 1] = True

    # 3x3ボックスをチェック
    # 3x3の左上の座標（起点）を計算
    box_row, box_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            # 起点からの相対位置で3x3ボックス内の数字を取得
            val = board[box_row + i][box_col + j]
            if val > 0:
                is_used[val - 1] = True

    # 使われていない数字をリストとして返す
    return [i + 1 for i, used in enumerate(is_used) if not used]

def print_board(board):
    """盤面を見やすく表示"""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = " ".join(str(row[j]) if row[j] != 0 else "." for j in range(9))
        print(row_str[:6] + "|" + row_str[6:12] + "|" + row_str[12:])
