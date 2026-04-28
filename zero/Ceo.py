import inspect
import random

# （先ほど定義した Ceo クラスはここにあると仮定します）
class Ceo:
    def __init__(self, name: str, x: int, y: int, z: int):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Ceo(name='{self.name}', x={self.x}, y={self.y}, z={self.z})"

# --- グループの定義 ---

class GroupA:
    # 第一引数に cls を取るクラスメソッドとして定義します
    @classmethod
    def action_1(cls, ceo_obj: Ceo):
        ceo_obj.x += 10
        print(f"  -> [A1] {ceo_obj.name}のxが10増加しました。")

    @classmethod
    def action_2(cls, ceo_obj: Ceo):
        ceo_obj.y -= 5
        print(f"  -> [A2] {ceo_obj.name}のyが5減少しました。")

    @classmethod
    def action_3(cls, ceo_obj: Ceo):
        ceo_obj.z += 20
        print(f"  -> [A3] {ceo_obj.name}のzが20増加しました。")


class GroupB:
    @classmethod
    def action_1(cls, ceo_obj: Ceo):
        ceo_obj.x -= 5
        print(f"  -> [B1] {ceo_obj.name}のxが5減少しました。")

    @classmethod
    def action_2(cls, ceo_obj: Ceo):
        ceo_obj.y += 10
        print(f"  -> [B2] {ceo_obj.name}のyが10増加しました。")


# --- 関数リストの自動生成 ---

# inspect.getmembers を使って情報を取得します
# not name.startswith('_') とすることで、Python内部で使われる __class__ などの関数を除外します
group_A_funcs = [func for name, func in inspect.getmembers(GroupA, predicate=inspect.ismethod) 
                 if not name.startswith('_')]

group_B_funcs = [func for name, func in inspect.getmembers(GroupB, predicate=inspect.ismethod) 
                 if not name.startswith('_')]


# --- 実行部分 ---

ceo_list = [
    Ceo("Alice", 100, 100, 100),
    Ceo("Bob", 50, 50, 50)
]

print("=== 処理開始 ===")
for ceo_instance in ceo_list:
    print(f"処理前: {ceo_instance}")
    
    # group_A_funcs (抽出したリスト) からランダムに関数を選ぶ
    selected_func = random.choice(group_A_funcs)
    
    # 選んだ関数を実行
    selected_func(ceo_instance)
    
    print(f"処理後: {ceo_instance}")
    print("-" * 30)
