from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #do_the_login()
        return "hi"
    else:
        #show_the_login_form()
        return "hi"

if __name__ == '__main__':
    app.run()
