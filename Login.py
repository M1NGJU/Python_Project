from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# 사용자가 입력한 정보를 저장할 리스트
user_data = []  # 예: [{'id': '강감찬', 'password': 'mini'}]

@app.route('/')
def home():
    # 홈 페이지 렌더링
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # 사용자가 입력한 아이디와 비밀번호를 받아옵니다.
        user_id = request.form.get('userName')
        user_pass = request.form.get('userPass')
        
        # 새 사용자 정보를 딕셔너리 형태로 저장하고 리스트에 추가합니다.
        new_user = {'id': user_id, 'password': user_pass}
        user_data.append(new_user)
        
        # test.html 페이지로 이동하면서 user_data 리스트 전달
        return render_template('test.html', user_data=user_data)
    
    # GET 요청일 경우 로그인 페이지 렌더링
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)
