import pandas as pd

def load_data():
    # Load the exercises dataset
    file_path = "data/exercises.csv"
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("Dataset not found. Ensure 'exercises.csv' is in the 'data/' folder.")
        return pd.DataFrame()

def filter_exercises(data, fitness_goal, equipment, condition):
    # Filter exercises based on inputs
    filtered = data[
        (data['FitnessGoal'].str.contains(fitness_goal, case=False)) &
        (data['Equipment'].str.contains(equipment, case=False)) &
        (data['Condition'].str.contains(condition, case=False))
    ]
    return filtered

def generate_plan(fitness_goal, equipment, condition):
    data = load_data()
    if data.empty:
        return ["Error: Dataset not available or invalid."]

    filtered_exercises = filter_exercises(data, fitness_goal, equipment, condition)

    if filtered_exercises.empty:
        return ["No matching exercises found for your inputs."]
    
    # Format the plan
    workout_plan = []
    for _, exercise in filtered_exercises.iterrows():
        workout_plan.append(f"{exercise['Duration']} minutes: {exercise['Exercise']}")

    return workout_plan
