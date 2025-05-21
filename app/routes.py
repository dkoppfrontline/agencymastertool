from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# Example tool dictionary that links tool names to routes
tools = {
    'Tool 1': '/tool1',
    'Tool 2': '/tool2',
    'Tool 3': '/tool3',
}

@main.route('/')
def home():
    return render_template('index.html', tools=tools)

@main.route('/tool1')
def tool1():
    return render_template('tool1.html')

@main.route('/tool2')
def tool2():
    return render_template('tool2.html')

@main.route('/tool3')
def tool3():
    return render_template('tool3.html')
