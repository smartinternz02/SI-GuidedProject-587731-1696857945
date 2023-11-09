from flask import Flask, render_template, request
uber=Flask(__name__)
@uber.route('/')
def helloworld():
    return render_template("index.html")
if __name__=="__main__":
    uber.run(debug=False, port=7000)