from flask import Flask, render_template, request,url_for,send_from_directory,jsonify,flash,redirect
import os

app = Flask(__name__)
app.secret_key = "123456"
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        gender = request.form.get('gender')
        age = request.form.get('age')  # 获取滑块的值
        image_file = request.files.get('photo')
        job=request.form.get('job')
        image_name_raw = image_file.filename
        image_name = image_name_raw.split('.')[0]
        # 保存图片到上传文件夹
        filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(filename)
        if gender and filename:
            gender = f"{'男' if gender == 'male' else '女'}"
            age=f"{age}"
            return render_template('result.html', selected_gender=gender,selected_age=age,selected_name=image_name,selected_image=filename,selected_job=job)
        else:
            flash('请选择性别!')
            return redirect(url_for('index'))

    return render_template('result.html', selected_name=None,selected_gender=None,selected_age=None,selected_job=None)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
