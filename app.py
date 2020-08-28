from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

@app.route('/sum')
def sum_():
    '''
    Adding two numbers
    '''
    if request.args.get('num1') and request.args.get('num2'):
        if "." in request.args.get('num1'):
            num1 = float(request.args.get('num1'))
        else:
            num1 = int(request.args.get('num1'))

        if "." in request.args.get('num2'):
            num2 = float(request.args.get('num2'))
        else:
            num2 = int(request.args.get('num2'))
        sum = num1+num2
        sum = round(sum, 2)
    else:
        return render_template("sum.html", msg="please enter both numbers.")
    return render_template("sum.html", total=sum, num1=num1, num2=num2)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)