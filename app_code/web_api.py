# Файл 'web_api.py': примитивный веб интерфейс.
# Клиент - браузер. Получает 'сырые' данные отчета в виде json.

import os
from flask import Flask, render_template, request, jsonify
from app_code.modules.program_process import ProgramProcess


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def show_main_page():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def handle_file_upload():
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        filename = uploaded_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)

        result_log_path = os.path.abspath(r'.\output')

        scaner_app = ProgramProcess(file_path, request.form.get("api-key"), result_log_path, 'json')

        return jsonify(scaner_app.result)

    return None


app.run(debug=True)
