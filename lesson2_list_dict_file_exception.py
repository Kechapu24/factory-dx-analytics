# =========================================================
# レッスン2: リストの応用・辞書・ファイル操作・例外処理
# =========================================================
# 前回(変数・if・for・関数)を土台にしています。
# 分からなくなったら、いつでもlesson1に戻って確認して大丈夫です。


# ---------------------------------------------------------
# パート1(復習+発展): リストとfor文の組み合わせ
# ---------------------------------------------------------
oee_list = [0.92, 0.65, 0.45, 0.88]

# 前回学んだ関数を、ここでも使ってみます
def calc_oee_status(oee_value):
    if oee_value >= 0.85:
        return "優良"
    elif oee_value >= 0.6:
        return "注意"
    else:
        return "危険"

for oee in oee_list:
    status = calc_oee_status(oee)
    print(f"OEE {oee} → {status}")

# ■ 練習問題1
# oee_listの中から「危険」判定のものだけを数えて、
# 「危険な設備は◯件あります」と表示してください。
# ヒント: count = 0 という変数を用意し、for文の中でif文を使って+1していく
count = 0
for oee in oee_list:
    status = calc_oee_status(oee)
    if status == "危険":
        count = count + 1
print(f"危険な設備は{count}件あります")

# ---------------------------------------------------------
# パート2: 辞書(dict) — 「名前付きのデータのまとまり」
# ---------------------------------------------------------
# 辞書は「キー」と「値」のペアでデータを持つ入れ物です。
# 1つの設備の情報を、まとめて1つの箱に入れるイメージです。

equipment = {
    "id": "EQ-002",
    "uptime_min": 380,
    "downtime_min": 100,
    "defect_qty": 40,
    "production_qty": 700,
}

print(equipment["id"])           # "EQ-002" が表示される
print(equipment["uptime_min"])   # 380 が表示される

# 辞書の中身を使って計算することもできます
uptime_rate = equipment["uptime_min"] / (equipment["uptime_min"] + equipment["downtime_min"])
print(f"稼働率: {uptime_rate:.1%}")

# ■ 練習問題2
# 自分で新しい辞書 equipment2 を作り、id="EQ-003", uptime_min=460, downtime_min=20 を入れてください。
# その後、稼働率を計算して表示してください。
equipment2 ={
    "id" : "EQ-003",
    "uptime_min" : 460,
    "downtime_min" :20, 
}

uptime_rate2 = equipment2["uptime_min"] / (equipment2["uptime_min"] + equipment2["downtime_min"])
print(f"稼働率：{uptime_rate2:.1%}")

# ---------------------------------------------------------
# パート3: リストの中に辞書を入れる(実務でよく使う形)
# ---------------------------------------------------------
# 実際のデータ処理では、「複数設備の情報」をこの形で扱うことが多いです。
# これはまさに、CSVファイルを読み込んだ時にpandasが内部でやっていることに近い構造です。

equipment_data = [
    {"id": "EQ-001", "uptime_min": 432, "downtime_min": 48},
    {"id": "EQ-002", "uptime_min": 380, "downtime_min": 100},
    {"id": "EQ-003", "uptime_min": 460, "downtime_min": 20},
]

for eq in equipment_data:
    rate = eq["uptime_min"] / (eq["uptime_min"] + eq["downtime_min"])
    print(f"{eq['id']}: 稼働率 {rate:.1%}")

# ■ 練習問題3
# equipment_data の中から、稼働率が90%未満の設備IDだけを表示してください。
# ヒント: for文の中でrateを計算し、if文で90%(0.9)未満かどうか判定する


for eq2 in equipment_data:
    rate2 = eq2["uptime_min"] / (eq2["uptime_min"] + eq2["downtime_min"])
    if rate2 < 0.9 :
        print(f"{eq2['id']}: 稼働率 {rate2:.1%}")



# ---------------------------------------------------------
# パート4: ファイル操作(CSVを自力で読む)
# ---------------------------------------------------------
# 前回、equipment_data.csv を pandas の read_csv で読み込みましたが、
# ここでは「pandasを使わずに、素のPythonでファイルを読む」練習をします。
# 仕組みを理解しておくと、pandasが何を裏でやっているか腑に落ちます。

with open("equipment_data.csv", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

print("\n--- CSVの中身(1行ずつ) ---")
for line in lines[:3]:  # 最初の3行だけ表示
    print(line.strip())  # strip()で末尾の改行を取り除く
    print (lines)

# with open(...) as f: は「ファイルを開いて、処理が終わったら自動的に閉じる」という書き方です。
# 閉じ忘れを防げるので、ファイル操作では基本的にこの書き方をします。

# ■ 練習問題4
# lines の中身を1行ずつ、カンマ(,)で分割して表示してみてください。
# ヒント: line.split(",") を使うと、カンマ区切りでリストに分割できます
# (1行目はヘッダーなので、結果が少し変な形になりますが気にしなくてOKです)
with open("equipment_data.csv", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split(",")
    print(parts)



# ---------------------------------------------------------
# パート5: 例外処理(エラーが起きても止まらないようにする)
# ---------------------------------------------------------
# 実務データには「ゼロ割り」のような、計算できないケースがよく紛れ込みます。
# 例外処理を使うと、エラーで処理全体が止まるのを防げます。

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("警告: 0で割ろうとしました。0を返します。")
        return 0

print(safe_divide(10, 2))   # 通常の計算 → 5.0
print(safe_divide(10, 0))   # ゼロ割り → 警告が出て0が返る

# try: の中身を実行してみて、エラーが起きたら except: の中身が実行される、という仕組みです。

# ■ 練習問題5
# production_qty = 0 の設備があった場合を想定し、
# defect_qty / production_qty(不良率の計算)を safe_divide関数を使って計算してみてください。
defect_qty = 5 
production_qty = 0 
print (safe_divide(defect_qty,production_qty))
print("\n★ 5つの練習問題、無理せず今日できるところまでで大丈夫です。")
print("★ 次はいよいよ、これらを使って実際のOEE計算スクリプトを『自分で』書き直してみます。")
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