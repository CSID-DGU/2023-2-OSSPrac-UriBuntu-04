# 파이썬 파일이 직접 스크립트로 실행될 때만 flask 애플리케이션을 실행 
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['University']=request.form.get('University')
        result['Major']=request.form.get('Major')
        result['Gender']=request.form.get('Gender')
        result['Email']=request.form.get('Email')
        result['sites']=request.form.get('sites')
        result['Languages']=request.form.getlist('Languages')
        return render_template('result.html',result=result)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)