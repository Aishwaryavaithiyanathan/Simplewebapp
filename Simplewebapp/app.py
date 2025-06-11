from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store for messages
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        messages.append({'name': name, 'message': message})
        return redirect(url_for('messages_page'))
    return render_template('contact.html')

@app.route('/messages')
def messages_page():
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
