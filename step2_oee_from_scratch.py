# =========================================================
# ステップ2: pandasを使わず、自分の手でOEEを計算する
# =========================================================
#
# これまで学んだ「辞書」「リスト」「for文」「関数」「ファイル操作」を
# 総動員して、pandasが裏でやっていることを、自分の手で再現してみます。


# ---------------------------------------------------------
# ① equipment_data.csv を読み込んで、
#    1行を1つの「辞書」にした、リストを作る
#    (レッスン2の「パート3: リストの中に辞書を入れる」を思い出してください)
#
#    完成イメージ:
#    equipment_data = [
#        {"id": "EQ-001", "uptime": 432, "downtime": 48, "production": 850, "defect": 17},
#        ...
#    ]
# ---------------------------------------------------------
with open ("equipment_data.csv","r",encoding="utf-8-sig")as f:
    lines = f.readlines()

equipment_data =[]

for line in lines[1:]:
    parts = line.strip().split(",")
    equipment = {
        "id" : parts[0],
        "uptime" : int(parts[2]),
        "downtime" : int(parts[3]),
        "production" : int(parts[4]),
        "defect" : int(parts[5])
    }

    equipment_data.append(equipment)

print(len(equipment_data), "件")
print(equipment_data[0])

# ---------------------------------------------------------
# ② OEEを計算する「関数」を作る
#    材料として、uptime・downtime・production・defect の4つを受け取り、
#    OEE(稼働率 × 良品率)を計算して、返す関数
#    (レッスン1の「パート4: 関数」を思い出してください)
# ---------------------------------------------------------
def calc_oee(equipment):
    availability = (
        equipment["uptime"]
        /
        (
            equipment["uptime"]
            + equipment["downtime"]
        )
    )
    quality = (
        equipment["production"]
        - equipment["defect"]
    ) / equipment["production"]
    oee = availability * quality
    return oee

# ---------------------------------------------------------
# ③ ①のリストを、for文で1個ずつ取り出し、
#    ②の関数を呼び出して、それぞれのOEEを表示する
# ---------------------------------------------------------
for equipment in equipment_data:
    oee = calc_oee(equipment)
    print(f"{equipment['id']}: OEE {oee:.1%}")

# ---------------------------------------------------------
# ④ (発展)OEEが70%未満の設備だけを、警告として表示する
#    (レッスン2の「練習問題1・3」を思い出してください)
# ---------------------------------------------------------
for equipment in equipment_data:
    oee = calc_oee(equipment)
    if oee < 0.7:
        print(f"{equipment['id']} OEE {oee:.1%} 警告")