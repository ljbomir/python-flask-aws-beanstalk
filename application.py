from flask import Flask, request, jsonify
import json

def hbrVal(YourAge):
    YourAge = int(YourAge)
    global maxHBR
    if (YourAge > 0) and (YourAge < 220):
        maxHBR = (220 - YourAge)
    else:
        return "Please enter a valid age"

    a = round(maxHBR * 0.64)
    b = round(maxHBR * 0.74)
    c = round(maxHBR * 0.77)
    d = round(maxHBR * 0.93)

    jsonOutput = {
        "MHBR": {
            "Max heart beat rate":f"{maxHBR} bpm",    
        }, 
        "Activity": {
        "Moderate-intensity physical activity":f"{a}-{b} bpm",
        "Vigorous-intensity physical activity":f"{c}-{d} bpm"
        }
    }
    return json.dumps(jsonOutput)

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# EB looks for an 'application' callable by default.
application = app = Flask(__name__)

# add a rule for the index page.
@application.route("/")
def home():
    return "Hello, World!"


@application.route('/age/<YourAge>', methods=['GET'])
def age(YourAge):
    return hbrVal(YourAge)


@application.route('/api', methods=['GET', 'POST'])
def apiHBR():
    content = request.json['age']
    return hbrVal(content)



if __name__ == "__main__":
    application.debug = True
    application.run()
