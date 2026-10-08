# app.py
import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# メモの初期値を空のリストに設定
memos = []

def read_memos_from_file():
    with open('memo.txt', 'r') as file:
        memos = file.readlines()
    return memos

@app.route('/')
def index():
    memos = read_memos_from_file()
    return render_template('index.html', memos=memos)

@app.route('/save', methods=['POST'])
def save_memo():
    dt = str(datetime.datetime.today())

    # フォームから送られたメモを取得
    new_memo = request.form.get('memo')
    
    # メモをリストの先頭に追加
    #memos.insert(0, new_memo + '\n' + dt)
    memos.insert(0, f"{new_memo.strip()}\n{dt}")   


    # メモをファイルに保存
    with open('memo.txt', 'w') as file:
        #file.write('\n'.join(memos))
        #file.write('\n'.join(map(str.strip, memos)))
        file.writelines(memo.replace('\r\n', '\n') + '\n' for memo in memos)
    # リダイレクトを行い、再読み込み時に再送信を防ぐ
    print(new_memo, memos)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
