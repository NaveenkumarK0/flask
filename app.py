from flask import Flask 

app=Flask(__name__)

@app.route('/')
def welcome():
    return(" Hi, Naveen")

@app.route('/greeting')
def greetings():
    return("It's great to connect with you")

if __name__ == "__main__":
    app.run(debug=True)