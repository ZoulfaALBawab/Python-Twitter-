from flask import Flask, render_template

#########################################################################

app = Flask(__name__)

#For each page you need to render ,, you add a router in the server ,, not in sperate file ::

@app.route("/")

def main():
    return render_template('index.html')




#########################################################################
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)

#test for test
