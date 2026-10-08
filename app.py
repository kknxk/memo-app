from flask import Flask, render_template, request

app = Flask(__name__)

# メモの初期値を空に設定
memo_text = ""


@app.route("/")
def index():
    # index.htmlにメモの内容を渡す
    return render_template("index.html", memo=memo_text)


@app.route("/save", methods=["POST"])
def save_memo():
    global memo_text
    # フォームから送られたメモを取得
    memo_text = request.form.get("memo")

    # メモをファイルに保存
    with open("memo.txt", "w") as file:
        file.write(memo_text)

    # index.htmlにリダイレクト
    return render_template("index.html", memo=memo_text)


if __name__ == "__main__":
    app.run(debug=True)
