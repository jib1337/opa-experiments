from flask import Flask, request, abort, redirect, url_for, session
import requests, json, os

app = Flask(__name__)
app.secret_key = os.urandom(16)

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
    print('Policy Decision:', decision)

    if decision:

        # Establish route to resource
        session['routeEnable'] = True
        return True
    else:
        return False

@app.route('/')
def index():

    # Route to resource is not established
    session['routeEnable'] = False

    # Using cookie values or URL params
    user = request.cookies.get('user')
    role = request.cookies.get('role')
    
    if user is None or role is None:
        user = request.args.get('user')
        role = request.args.get('role')

    # Query policy engine
    if queryPolicyEngine(user, role):
        return redirect(url_for('resource'))
    else:
        abort(401)

@app.route('/resource')
def resource():

    try:
        routeEnable = session['routeEnable']
    except KeyError:
        abort(401)

    print('Route established:', session['routeEnable'])

    if routeEnable:
        return f'<p>You have been granted access the resource, congrats!</p><br><img src="/static/cat.jpg">'
    else:
        abort(401)
