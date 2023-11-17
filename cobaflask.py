import csv
import json
from flask import Flask, jsonify
from flask import render_template
from flask import request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def hello_world():
    return render_template("utama.html")

@app.route("/biodata/")
def hello_w():
    return render_template("biodata2.html")

@app.route("/cv/")
def hello_cv():
    return render_template("cv.html")

@app.route("/movies/")
def hello_film():
    return render_template("movies.html")

@app.route("/gallery/")
def hello_foto():
    return render_template("galery.html")

@app.route("/fibonacci/")
def hello_fibonacci():
    return render_template("fibonacci.html")

@app.route('/get/')
def index():
    return render_template('get.html')

@app.route('/convert/', methods=['POST'])
def convert_to_json():
    csv_file = request.files['csv_file']
    if csv_file and csv_file.filename.endswith('.csv'):
        data = []
        csv_data = csv_file.read().decode('utf-8-sig')  # Baca file CSV sebagai teks
        csv_reader = csv.DictReader(csv_data.splitlines(), delimiter=',', quotechar='"')
        for row in csv_reader:
            data.append(row)
        return jsonify(data)
    else:
        return 'Invalid file format. Please upload a CSV file.'


data_submit = []  # Struktur data untuk menyimpan data submit

@app.route('/postdata', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        nama = request.form['nama']
        pesan = request.form['pesan']

        data_submit.append({'nama': nama, 'pesan': pesan})  # Menyimpan data submit

        return render_template('form.html', hasil_submit=data_submit)

    return render_template('form.html', hasil_submit=data_submit)

@app.route('/submit', methods=['POST'])
def handle_submit():
    nama = request.form['nama']
    pesan = request.form['pesan']

    data_submit.append({'nama': nama, 'pesan': pesan})  # Menyimpan data submit

    return render_template('hasil_submit.html', hasil_submit=data_submit)

if __name__ == '__main__':
    app.run()