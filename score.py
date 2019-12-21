from flask import Flask, request, render_template, redirect

app = Flask(__name__)

student = [
    {'name': 'tom', 'gender': 'male', 'chinese': 90, 'math': 78},
    {'name': 'bob', 'gender': 'male', 'chinese': 87, 'math': 65},
    {'name': 'lucy', 'gender': 'female', 'chinese': 74, 'math': 73},
    {'name': 'lily', 'gender': 'female', 'chinese': 86, 'math': 90},
    {'name': 'alex', 'gender': 'male', 'chinese': 91, 'math': 77},
    {'name': 'john', 'gender': 'male', 'chinese': 79, 'math': 72},
    {'name': 'jack', 'gender': 'male', 'chinese': 60, 'math': 99},
    {'name': 'tomas', 'gender': 'male', 'chinese': 88, 'math': 98},
    {'name': 'eva', 'gender': 'female', 'chinese': 100, 'math': 85},
    {'name': 'ella', 'gender': 'female', 'chinese': 70, 'math': 81}
]




if __name__ == '__main__':
    app.debug = True
    app.run()
