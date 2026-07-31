from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from form
        airline = int(request.form["airline"])
        source = int(request.form["source"])
        destination = int(request.form["destination"])

        day = int(request.form["day"])
        month = int(request.form["month"])
        departure_time = int(request.form["departure_time"])

        # Create input
        features = np.array([[
            airline,
            source,
            destination,
            day,
            month,
            departure_time
        ]])

        # Prediction
        prediction = model.predict(features)[0]

        # Probability
        probability = model.predict_proba(features)[0][1] * 100

        # Result
        if prediction == 1:
            result = "Flight is likely to be Delayed."
        else:
            result = "Flight is likely to be On Time."

        return render_template(
            "result.html",
            prediction=result,
            probability=round(probability, 2)
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)