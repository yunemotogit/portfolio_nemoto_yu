const API_URL = 'http://localhost:8000/api/generate';
let currentPuzzle = null;
let currentSolution = null;
let selectedCell = null;

const gridElement = document.getElementById('sudoku-grid');
const statusElement = document.getElementById('status-message');
const timerElement = document.getElementById('timer');
const showSolutionBtn = document.getElementById('show-solution-btn');
const verifyBtn = document.getElementById('verify-btn');
const difficultyDisplay = document.getElementById('difficulty-display');

const diffBeginnerBtn = document.getElementById('difficulty-beginner');
const diffIntermediateBtn = document.getElementById('difficulty-intermediate');
const diffAdvancedBtn = document.getElementById('difficulty-advanced');

let timerInterval = null;
let startTime = null;

// 盤面の初期化
function initGrid() {
    gridElement.innerHTML = '';
    for (let i = 0; i < 81; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.index = i;
        cell.dataset.row = Math.floor(i / 9);
        cell.dataset.col = i % 9;
        cell.addEventListener('click', () => selectCell(cell));
        gridElement.appendChild(cell);
    }
}

function selectCell(cell) {
    document.querySelectorAll('.cell').forEach(c => c.classList.remove('selected'));
    cell.classList.add('selected');
    selectedCell = cell;
}

// タイマー処理
function startTimer() {
    stopTimer();
    startTime = Date.now();
    timerInterval = setInterval(updateTimer, 1000);
}

function stopTimer() {
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
}

function updateTimer() {
    const elapsedSeconds = Math.floor((Date.now() - startTime) / 1000);
    const minutes = Math.floor(elapsedSeconds / 60).toString().padStart(2, '0');
    const seconds = (elapsedSeconds % 60).toString().padStart(2, '0');
    timerElement.textContent = `${minutes}:${seconds}`;
}

// キーボード入力の処理
window.addEventListener('keydown', (e) => {
    if (!selectedCell || selectedCell.classList.contains('fixed')) return;

    if (e.key >= '1' && e.key <= '9') {
        selectedCell.textContent = e.key;
        clearStatus();
    } else if (e.key === 'Backspace' || e.key === 'Delete') {
        selectedCell.textContent = '';
        clearStatus();
    }
});

function clearStatus() {
    statusElement.textContent = '';
    statusElement.className = 'status';
}

async function fetchNewGame(difficulty = 45) {
    statusElement.textContent = '生成中...';
    clearStatus();
    try {
        const response = await fetch(`${API_URL}?difficulty=${difficulty}`);
        const data = await response.json();

        currentPuzzle = data.puzzle;
        currentSolution = data.solution;

        // 表示を更新
        const diffText = difficulty === 35 ? '初級' : difficulty === 45 ? '中級' : '上級';
        difficultyDisplay.textContent = diffText;

        displayPuzzle(currentPuzzle);
        startTimer(); // タイマー開始
        statusElement.textContent = `パズルを生成しました (穴: ${data.holes})`;
    } catch (error) {
        console.error('Error fetching puzzle:', error);
        statusElement.textContent = 'サーバーに接続できません。api.py を起動してください。';
    }
}

function displayPuzzle(board) {
    const cells = document.querySelectorAll('.cell');
    board.forEach((row, r) => {
        row.forEach((val, c) => {
            const index = r * 9 + c;
            const cell = cells[index];
            cell.textContent = val !== 0 ? val : '';
            cell.classList.remove('fixed');
            if (val !== 0) {
                cell.classList.add('fixed');
            }
        });
    });
}

function showSolution() {
    if (!currentSolution) return;
    displayPuzzle(currentSolution);
    stopTimer(); // （負けとして）停止
    statusElement.textContent = '正解を表示しました';
    statusElement.className = 'status';
}

function verifyPuzzle() {
    if (!currentSolution) return;
    const cells = document.querySelectorAll('.cell');
    let isCorrect = true;
    let isComplete = true;

    cells.forEach((cell, i) => {
        const r = parseInt(cell.dataset.row);
        const c = parseInt(cell.dataset.col);
        const userVal = cell.textContent;
        const correctVal = currentSolution[r][c].toString();

        if (!userVal) {
            isComplete = false;
        } else if (userVal !== correctVal) {
            isCorrect = false;
        }
    });

    if (!isComplete) {
        statusElement.textContent = 'すべてのマスを埋めてください';
        statusElement.className = 'status error';
    } else if (isCorrect) {
        stopTimer(); // 正解時のみ停止
        statusElement.textContent = '正解です！おめでとうございます！';
        statusElement.className = 'status success';
    } else {
        statusElement.textContent = '不正解が含まれています。見直してみましょう！';
        statusElement.className = 'status error';
    }
}

diffBeginnerBtn.addEventListener('click', () => fetchNewGame(35));
diffIntermediateBtn.addEventListener('click', () => fetchNewGame(45));
diffAdvancedBtn.addEventListener('click', () => fetchNewGame(50));
showSolutionBtn.addEventListener('click', showSolution);
verifyBtn.addEventListener('click', verifyPuzzle);

// 初回起動
initGrid();
fetchNewGame();
