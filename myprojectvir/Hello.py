from flask import Flask, abort, json, jsonify, render_template, request
from markupsafe import escape
import requests

app = Flask(__name__)

@app.route("/")
def Hello():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'
    # show the subpath after /path/

@app.route('/about')
def about ():
    return "about page"

@app.route('/gett/<int:id> ',methods=['GET'] ) 
def getdata (id):
    URL ="https://jsonplaceholder.typicode.com/posts"
    x= requests.get(URL)
    y= x.json()

    if 1 <= id <= len(y):
        return jsonify(y[id])  
    else:
        abort(400, description="data not found")
        

# @app.route('/ge/<int:id>') 
# def getdataff (id):
#     URL ="https://jsonplaceholder.typicode.com/posts"
#     x = requests.get(URL)
#     y = json.load(x)
   
#     return y[id-1]


@app.route('/home/<int:num>', methods = ['GET','POST']) 
def disp(num): 
    URL ="https://jsonplaceholder.typicode.com/posts"
    x= requests.get(URL)
    return json.dumps(x.text)
    

if __name__=="__main__" :
    app.run(debug=True)


# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file ():
#     if request.method == 'POST':
#         pass

# @app.route("/me")
# def me_api():
#     user =  URL ="https://jsonplaceholder.typicode.com/posts"
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url _ for("user_image", filename=user.image),
#     }

# @app.route("/users")
# def users_api():
#     URL ="https://jsonplaceholder.typicode.com/posts"
#     x = requests.get(URL).text
#     y = json.load(x)
#     users =y
#     return [user.to_json() for user in users]

     