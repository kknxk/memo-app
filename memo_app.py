import datetime
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

def read_memos_from_file():
    with open("memo.txt", "r", encoding="utf-8-sig") as file:
        memos = file.readlines()
    return memos


@app.route("/")
def index():
    memos = read_memos_from_file()
    return render_template("index.html", memos=memos)


@app.route("/api/memos", methods=["GET"])
def get_memos():
    memos = read_memos_from_file()
    return {
        "memos": memos
    }

@app.route("/api/memos", methods=["POST"])
def save_memo_api():

    data = request.get_json()
    print(data)  # デバッグ用に受信したデータを出力
    # 新しいメモを取得
    new_memo = data.get("memo")
    print(f"Received memo: {new_memo}")  # デバッグ用に新しいメモを出力

    timestamp= str(datetime.datetime.today())

    # メモをリストの先頭に追加
    memos = read_memos_from_file()
    memos.insert(0, f"{timestamp}\n{new_memo.strip()}\n")

    # メモをファイルに保存
    with open("memo.txt", "w", encoding="utf-8") as file:
        file.writelines(memos)
    # JSON形式でレスポンスを返す
    return jsonify({
        "status": "success",
        "message": "メモが保存されました。",
        "memo": new_memo,
        "timestamp": timestamp
    })


if __name__ == "__main__":
    app.run(debug=True)
