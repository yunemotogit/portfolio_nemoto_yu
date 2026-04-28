import random

# １．事前に用意した複数の関数をABCのグループに分ける
def make_func(name):
    # 関数名を見えるように保持
    func = lambda: print(f"{name} が実行されました")
    func.__name__ = name 
    return func

group_a = [make_func(f"A-{i}") for i in range(1, 8)]
group_b = [make_func(f"B-{i}") for i in range(1, 8)]
group_c = [make_func(f"C-{i}") for i in range(1, 8)]

def main():
    # ２．各グループから関数をランダムに5つ選んで、グループごとに表示
    # （元のリストから5つ分をランダムに抽出）
    selected_a = random.sample(group_a, 5)
    selected_b = random.sample(group_b, 5)
    selected_c = random.sample(group_c, 5)

    print("【最初に選ばれた5つの関数】")
    print("グループA:", [f.__name__ for f in selected_a])
    print("グループB:", [f.__name__ for f in selected_b])
    print("グループC:", [f.__name__ for f in selected_c])
    print("-" * 30)

    results = [] # リザルト用
    turn = 1

    # ６．「３～５」を繰り返し、すべての関数（選ばれた各5個）の処理が終わるまで
    # リストの中身が空になるまでループします
    while selected_a and selected_b and selected_c:
        print(f"\n=== ターン {turn} ===")

        # ３．各グループ（選ばれた5つのリスト）から１つずつ関数を取り出す
        # pop() を使ってランダムなインデックスから取り出し（リストからも削除される）
        func_a = selected_a.pop(random.randrange(len(selected_a)))
        func_b = selected_b.pop(random.randrange(len(selected_b)))
        func_c = selected_c.pop(random.randrange(len(selected_c)))

        print(f"[取り出し] {func_a.__name__}, {func_b.__name__}, {func_c.__name__}")

        # ４ ＆ ５．取り出した3つの関数から１つ選択して処理を実行 -> 残り２つも実行
        # どれから順に実行されるかを決めるためにシャッフル
        funcs_to_run = [
            ("A", func_a), 
            ("B", func_b), 
            ("C", func_c)
        ]
        random.shuffle(funcs_to_run)

        print("[実行]")
        for i, (g_name, func) in enumerate(funcs_to_run):
            if i == 0:
                print(f" -> 最初の選択({g_name}): ", end="")
            else:
                print(f" -> 残りの処理({g_name}): ", end="")
            
            func() # 実行
            results.append(func.__name__) # リザルトに記録
            
        turn += 1

    # すべての処理が終わったらリザルトを表示
    print("\n===============================")
    print("リザルト：すべての関数の処理が完了しました")
    print("===============================")
    print("【実行された順番】")
    for idx, name in enumerate(results, 1):
        print(f" {idx:2d}番目: {name}")

if __name__ == "__main__":
    main()
