print("--- api.py を起動しています ---")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from generate_sudoku import generate_sudoku
from sudoku_solver import create_puzzle

app = FastAPI()

# フロントエンドからのアクセスを許可するためのCORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/generate")
def get_puzzle(difficulty: int = 40):
    """
    数独のパズルと回答を生成して返すエンドポイント
    difficulty: 空ける穴の試行回数 (default 40)
    """
    # 1. 解答盤面の生成
    solution_board = generate_sudoku()
    
    # 2. パズルの生成 (穴あけ)
    puzzle_board, holes = create_puzzle(solution_board, attempts=difficulty)
    
    return {
        "puzzle": puzzle_board,
        "solution": solution_board,
        "holes": holes
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
