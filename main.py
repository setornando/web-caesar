from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            text area {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            h1 {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Web Caesar</h1>
        <
        <form action="/" method="POST">
            <label for="rotate_by"> Rotate By:</label>
            <input id="rotate_by" type="text" name="rot" id="rot" value="0"/>
            
            <br>

            <textarea id="textarea" name="text"> {0} </textarea>

            <br>
           
            <input type="submit" value="Encrypt"/>
          
        
        </form>
    </body>
</html>
"""

@app.route("/")
def index ():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted_string = rotate_string(text,rot)
    return form.format(encrypted_string)

app.run()