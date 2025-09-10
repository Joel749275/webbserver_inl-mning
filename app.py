from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def product():
    contacts = [
        {'name': 'Joel', 'email': 'joel.hogg@skola.taby.se'},
    ]
    return render_template('contact.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')