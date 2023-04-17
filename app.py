from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if (ops == 'add'):
            result = f'the sum of {num1} and {num2} is {num1 + num2}'
        if (ops == 'subtract'):
            result = f'the subtract of {num1} and {num2} is {num1 - num2}'
        if (ops == 'multiply'):
            result = f'the multiply of {num1} and {num2} is {num1 * num2}'
        if (ops == 'divide'):
            result = f'the divide of {num1} and {num2} is {num1 / num2}'

        return render_template('result.html',result = result)

@app.route('/postman_data',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if (ops == 'add'):
            result = f'the sum of {num1} and {num2} is {num1 + num2}'
        if (ops == 'subtract'):
            result = f'the subtract of {num1} and {num2} is {num1 - num2}'
        if (ops == 'multiply'):
            result = f'the multiply of {num1} and {num2} is {num1 * num2}'
        if (ops == 'divide'):
            result = f'the divide of {num1} and {num2} is {num1 / num2}'
            
        return jsonify(result)


# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"

# @app.route("/test")
# def test():

#     return f"this is my fuction to run app. 'girishjaiswal'"

# @app.route("/hello_world1")
# def hello_world1():
#     return "<h1>Hello, World1!</h1>"


# @app.route("/hello_world2")
# def hello_world2():
#     return "<h1>Hello, World2!</h1>"

# @app.route('/test2')
# def test2():
#     data = request.args.get('x')
#     return 'this is a data input form my url {}'.format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
