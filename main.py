from flask import Flask, request
#from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            text area {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label> Rotate By: 
                <input type="text" name="rot" id="rot" value="0"/>
            </label>

            <br>

            <textarea name="text" id="text" />
            </textarea>

            <br>
           
            <input type="submit" />
          
        
        </form>
    </body>
</html>
"""

@app.route("/")
def index ():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_string = str(rotate_string(rot,text))
    return '<h1>' + encrypted_string + '</h1>'
    
        
#for field in request.form.keys():
    #resp += "<b>(key)</b>: {value}<br>".format(key=field, value=request.form[field])


app.run()