from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

@app.route('/Heroku',methods=['GET', 'POST'])
def index():
    return "<h1> This is flask application </h1>"
if __name__=='__main__':
    app.run()