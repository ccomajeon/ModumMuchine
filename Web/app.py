from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('./사용량머신러닝testModel.pkl')
model2 = joblib.load('./사용빈도머신러닝testModel.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        #파라미터 전달

        date_temp = float(request.form['date_temp'])
        date_temp2 = float(request.form['date_temp2'])
        age_temp = float(request.form['age_temp'])

        # 사용량 변수 선언, 사용빈도 변수 선언
        use = 0
        spend = 0

        # 입력 값을 토대로 예측 값을 찾아낸다
        dict = model.predict([[date_temp]])
        dict2 = model2.predict([[date_temp2, age_temp]])

        # 결과 저장
        spend = dict[0]
        use = dict2[0, 0]


    return render_template('index.html', use=use)
    return render_template('index.html', spend=spend)

if __name__ == '__main__':
    app.run(debug=True)