from flask import Flask,render_template, request, jsonify
from guessing import get_game_result

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/play", methods=["POST"])
def play_game():
    data=request.get_json()
    user_choice=data.get('user_choice')
                        
    
    result_text=get_game_result(user_choice)
    return jsonify({"result":result_text})

if __name__ == "__main__":
    app.run(debug=True)
   