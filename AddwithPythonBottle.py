from bottle import route, run, template

@route('/add/<number1:int>/<number2:int>')
def index(number1, number2):
    finalAnswer = (number1) + (number2)
    return template('<b>{{number1}} + {{number2}}</b> = {{finalAnswer}}', finalAnswer=finalAnswer, number1=number1, number2=number2)

run(host='localhost', port=8080)