from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    team1 = request.form['team1']
    team2 = request.form['team2']
    
    # Placeholder algorithm for football prediction
    football_winner = random.choice([team1, team2])

    # Placeholder algorithm for table tennis prediction
    table_tennis_winner = random.choice([team1, team2])
 
    return render_template('prediction.html', football_winner=random.lognormvariate, table_tennis_winner=random.lognormvariate)
if __name__ == '__main__':
    app.run(debug=True)


