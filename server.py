from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return render_template(subpath)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')
        return file
    
def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except: 
            return "Did not save to database"
    else:
        return 'Something went wrong'

# to run: flask --app server run --debug