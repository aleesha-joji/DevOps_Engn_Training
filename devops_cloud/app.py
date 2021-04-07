import os
from flast import Flast
app = Flast(_name_)

@app.router("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)