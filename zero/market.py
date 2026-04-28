class market:
    def __init__(self, name):
        self.name = name
    
def make_func(name):
    return lambda: print(f"{name} が実行されました")
# グループA, B, Cにそれぞれ5つの関数を格納
group_a = [make_func(f"A-{i}") for i in range(1, 6)]
group_b = [make_func(f"B-{i}") for i in range(1, 6)]
group_c = [make_func(f"C-{i}") for i in range(1, 6)]

# zip関数で各グループから1つずつ関数を取り出し、5回繰り返す
print("=== 処理開始 ===")
for i, (func_a, func_b, func_c) in enumerate(zip(group_a, group_b, group_c), 1):
    print(f"【{i}回目のループ】")
    
    # 取り出した関数を実行
    func_a()
    func_b()
    func_c()
    
    print("-" * 20)
print("=== 処理終了 ===")