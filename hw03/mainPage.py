# 파이썬 파일이 직접 스크립트로 실행될 때만 flask 애플리케이션을 실행 
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
<<<<<<< HEAD
        result['Gender']=request.form.get('Gender')

=======
        result['Major']=request.form.get('Major')
        result['Languages']=request.form.getlist('Languages')
>>>>>>> 3d9fbc6f8cb074acc9b121bf89d36d2c8d8c980a
        return render_template('result.html',result=result)


if __name__ =='__main__':
    app.run(debug=True)