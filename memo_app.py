import datetime
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def read_memos_from_file():
    with open("data/memo.json", "r", encoding="utf-8") as file:
        memos = json.load(file)
    return memos

def write_memos_to_file(memos):
    with open("data/memo.json", "w", encoding="utf-8") as file:
        json.dump(
            memos,
            file,
            ensure_ascii=False,
            indent=2
        )


@app.route("/")
def index():
    memos = read_memos_from_file()
    return render_template("index.html", memos=memos)


@app.route("/api/memos", methods=["GET"])
def get_memos():
    memos = read_memos_from_file()
    return jsonify({
        "memos": memos
    })

@app.route("/api/memos", methods=["POST"])
def save_memo_api():

    data = request.get_json()
    # 新しいメモを取得
    new_memo = data.get("memo")

    if not new_memo or not new_memo.strip():
        return jsonify({
            "message": "メモを入力してください。"
        }), 400


    timestamp= str(datetime.datetime.today())
    # メモをリストの先頭に追加
    memos = read_memos_from_file()

    if memos:
        new_id = max(memo["id"] for memo in memos) + 1
    else:
        new_id = 1

    memo_data = {
        "id": new_id,
        "timestamp": timestamp,
        "memo": new_memo.strip()
    }

    memos.insert(0, memo_data)

    write_memos_to_file(memos)

    # JSON形式でレスポンスを返す
    return jsonify({
        "message": "メモが保存されました。",
        "memo": memo_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
