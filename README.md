# Workout Planner

## Overview
Workout Planner is a personalized workout plan generator that creates custom fitness routines based on user inputs such as fitness goals, available equipment, and physical condition. By selecting these parameters, users receive a tailored workout plan to help them achieve their fitness objectives. The app uses **Flask** for the web framework and **Pandas** for processing exercise data.

---

## Features

- **Personalized Workout Plans**: Generate a customized workout plan based on your fitness goal, available equipment, and current physical condition.
- **Easy-to-Use Interface**: A user-friendly web interface for submitting details and receiving a tailored workout plan.
- **Customizable**: The dataset can easily be expanded with more exercises to support different goals and conditions.
- **Fast & Lightweight**: Built with Flask to handle requests efficiently and Pandas to process data quickly.

---

## Technologies Used

- **Flask**: A lightweight Python web framework used to handle HTTP requests and render HTML templates.
- **Pandas**: A Python library used to filter and manipulate exercise data based on user input.
- **HTML/CSS**: For building the basic structure and design of the user interface, utilizing **Bootstrap** for responsive design.
- **JavaScript**: Used for form validation and showing a loading spinner while generating the workout plan.

---

## How to Run the Application

1. **Clone the repository**:
    ```bash
    git clone https://github.com/VindyaLenawala/ai-personalized-workout-plans.git
    cd ai-personalized-workout-plans
    ```

2. **Set up a virtual environment**:
    - On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask app**:
    ```bash
    python app.py
    ```
    The app will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## How to Use

1. **Input your details**:
    - **Fitness Goal**: Select from options like "Lose Weight", "Build Muscle", or "General Fitness".
    - **Available Equipment**: Specify the equipment available, such as "No Equipment" or "Dumbbells".
    - **Physical Condition**: Choose from conditions like "Beginner", "Intermediate", or "Advanced".

2. **Generate Workout Plan**:
    - Once you submit the form, a personalized workout plan will be displayed based on your input.

---

## Future Improvements

- **Expand the exercise dataset**: Add more exercises to provide more variety and coverage.
- **AI/ML Integration**: Implement AI algorithms to suggest workout plans dynamically based on user history and preferences.
- **User Profiles**: Allow users to save their workout plans and track progress over time.
