from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# 사용자가 입력한 정보를 저장할 리스트
user_data = []  # 예: [{'id': '강감찬', 'password': 'mini'}]

@app.route('/')
def login_page():
    # 로그인 페이지 렌더링
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    # 사용자가 입력한 아이디와 비밀번호를 받아옵니다.
    user_id = request.form.get('userName')
    user_pass = request.form.get('userPass')
    
    # 새 사용자 정보를 딕셔너리 형태로 저장하고, 리스트에 추가합니다.
    new_user = {'id': user_id, 'password': user_pass}
    user_data.append(new_user)
    
    # 리스트에 저장된 사용자 정보를 출력 (디버깅용)
    print("현재 저장된 사용자 목록:", user_data)
    
    # test.html 페이지로 이동하면서 user_data 리스트 전달
    return render_template('test.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# 사용자가 입력한 정보를 저장할 리스트
user_data = []  # 예: [{'id': '강감찬', 'password': 'mini'}]

@app.route('/')
def login_page():
    # 로그인 페이지 렌더링
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    # 사용자가 입력한 아이디와 비밀번호를 받아옵니다.
    user_id = request.form.get('userName')
    user_pass = request.form.get('userPass')
    
    # 새 사용자 정보를 딕셔너리 형태로 저장하고, 리스트에 추가합니다.
    new_user = {'id': user_id, 'password': user_pass}
    user_data.append(new_user)
    
    # 리스트에 저장된 사용자 정보를 출력 (디버깅용)
    print("현재 저장된 사용자 목록:", user_data)
    
    # test.html 페이지로 이동하면서 user_data 리스트 전달
    return render_template('test.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
