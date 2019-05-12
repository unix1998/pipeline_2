#!/usr/local/bin/python3
from flask import Flask  
  
app = Flask(__name__)  
 
@app.route('/')  
def hello_world():  
    a = 1  
    b = '1'  
    c = a + b  
    return 'Hello world!'  
  
if __name__ == '__main__':  
    app.run(debug = True)  
