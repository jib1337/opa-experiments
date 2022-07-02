from flask import Flask, request, abort, redirect, url_for
import requests, json

app = Flask(__name__)

# 
def queryPolicyEngine(user, role):
    
    # Parameters must exist
    if user is None or role is None: return False

    data = '''
    {
        "input": {
            "user": "''' + user + '''",
            "role": "''' + role + '''"
        }
    }
    '''

    # Query OPA endpoint with params
    queryResult = requests.post('http://localhost:8181/v1/data/policy/allow', headers={'Content-Type': 'application/json'}, data=data).text
    decision = json.loads(queryResult)['result']

    if decision:
        return True
    else:
        return False

@app.route('/')
def index():

    # Using cookie values for this example
    user = request.cookies.get('user')
    role = request.cookies.get('role')

    # Query policy engine
    if queryPolicyEngine(user, role):
        return redirect(url_for('resource'))
    else:
        abort(401)

@app.route('/resource')
def resource():
    return 'You have accessed the resource, congrats'
