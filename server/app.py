from flask import Flask, request, abort, redirect, url_for, session
import requests, json, os, jwt

app = Flask(__name__)
app.secret_key = os.urandom(16)

def queryPolicyEngine(user, role, sourceAddress, token=None):
    
    # Parameters must exist
    if user is None or role is None: return False
    
    data = '''
    {
        "input": {
            "user": "''' + user + '''",
            "role": "''' + role + '''",
            "sourceAddress": "''' + sourceAddress + '''"
        }
    }
    '''

    print(data)

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

def handleToken(token):
# Verify and extract claims from provided JWT
    with open('../pe/public_key.pem', 'rb') as keyFile:
        pubkey = keyFile.read()

    claims = jwt.decode(token, pubkey, algorithms=["RS256"])
    return claims['user'], claims['role']

@app.route('/')
def index():

    sourceAddress = request.remote_addr
    print('Source address:', sourceAddress)

    authHeader = request.headers.get('Authorization')
    if authHeader is not None:
        token = authHeader.split('Bearer ')[1]
        user, role = handleToken(token)
        
    else:

        # Using cookie values or URL params
        token = None
        user = request.cookies.get('user')
        role = request.cookies.get('role')
            
        if user is None or role is None:
            user = request.args.get('user')
            role = request.args.get('role')

        # Query policy engine with all relevant request data
    if queryPolicyEngine(user, role, sourceAddress, token):
        return redirect(url_for('resource'))
    else:
        abort(401)

@app.route('/resource')
def resource():

    # Note: Currently any request sent via Curl doesn't trigger the route.
    try:
        routeEnable = session['routeEnable']
    except KeyError:
        abort(401)

    print('Route established:', session['routeEnable'])

    if routeEnable:
        return f'<p>You have been granted access the resource, congrats!</p><br><img src="/static/cat.jpg">'
    else:
        abort(401)
