from flask import Flask, render_template, request
from model import generate_plan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_workout():
    fitness_goal = request.form.get('fitness_goal')
    equipment = request.form.get('equipment')
    condition = request.form.get('condition')

    # Generate workout plan
    workout_plan = generate_plan(fitness_goal, equipment, condition)

    return render_template('plan.html', plan=workout_plan)

if __name__ == '__main__':
    app.run(debug=True)
