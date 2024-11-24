# AI Workout Planner

## Overview
AI Workout Planner is a personalized workout plan generator that creates custom fitness routines based on user inputs. By selecting their fitness goals, available equipment, and physical condition, users can receive a tailored workout plan designed to help them achieve their fitness objectives. This project leverages **Flask** for the web framework and **Pandas** for data processing.

---

## Features

- **Personalized Workout Plans**: Generate a workout plan based on your fitness goal, available equipment, and current physical condition.
- **Easy to Use**: A simple web interface that allows users to input their details and receive a workout plan in seconds.
- **Customizable**: Designed to allow you to easily add more exercises or expand the dataset to suit different goals or conditions.
- **Lightweight and Fast**: Built with Flask for efficient web handling and Pandas for fast data processing.

---

## Technologies Used

- **Flask**: Lightweight Python web framework used to handle HTTP requests and render templates.
- **Pandas**: Data manipulation library used to process the exercises dataset and filter based on user input.
- **HTML/CSS**: For the basic structure and design of the user interface, using Bootstrap for responsive styling.
- **JavaScript**: Used to enhance form validation and provide a loading spinner while generating the plan.

---

## How to Run the Application

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/VindyaLenawala/ai-personalized-workout-plans.git
    cd ai-personalized-workout-plans
    ```

2. **Set up a virtual environment** and activate it:
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
    The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## How to Use

1. Open the app in your browser.
2. Fill out the form with your **fitness goal**, **available equipment**, and **physical condition**.
3. Click on **Generate Workout Plan** to receive your custom workout plan.
4. View the plan with the suggested exercises based on your inputs.

