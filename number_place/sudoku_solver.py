import copy
import random
from generate_sudoku import find_empty, get_candidates

def count_solutions(board, count):
    """
    盤面の解の数をカウントするソルバー関数です。
    解が2つ以上見つかった時点で探索を打ち切ります。
    """
    # 空いているマスを探す（find_empty関数）
    empty = find_empty(board)
    # 空きマスがなければ解が1つ見つかったとカウント
    if not empty:
        count[0] += 1
        return count[0]
    
    row, col = empty
    # 候補数字のリストを取得（get_candidates関数）
    candidates = get_candidates(board, row, col)

    for num in candidates:
        # 候補数字を順番に試す
        board[row][col] = num
        count_solutions(board, count)
        board[row][col] = 0
        
        # 複数解が見つかったら即座に終了（全探索の枝刈り）
        if count[0] > 1:
            return count[0]
            
    return count[0]

def create_puzzle(board, attempts=81):
    """
    完成した盤面からマスをランダムに選び、唯一解を保てる範囲で穴を空けます。
    attempts: 穴を空けようと試みる回数（デフォルトは全マス）
    """
    # 盤面を壊さないようにコピーを作成
    puzzle = copy.deepcopy(board)
    
    # 穴を空ける候補の座標リストを作成してシャッフル
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)
    
    holes_made = 0
    tried = 0
    
    for r, c in positions:
        if tried >= attempts:
            break
            
        # 今の数字をバックアップして穴を空ける
        backup = puzzle[r][c]
        puzzle[r][c] = 0
        tried += 1
        
        # 解が1つだけ（一意）か確認するためにソルバーにかける
        test_board = copy.deepcopy(puzzle)
        count = [0]
        
        if count_solutions(test_board, count) != 1:
            # 複数解になってしまったら元に戻す
            puzzle[r][c] = backup
        else:
            holes_made += 1
            
    return puzzle, holes_made
