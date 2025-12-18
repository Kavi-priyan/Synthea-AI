import os
from flask import Flask, request, render_template, jsonify
import traceback

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create Flask app
app = Flask(__name__)

# Load the ML pipeline once on startup
try:
    pipeline = PredictPipeline()
except Exception as e:
    print("Error loading PredictPipeline:", e)
    traceback.print_exc()
    pipeline = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict_datapoint", methods=["GET", "POST"])
def predict_datapoint():
    try:
        if request.method == "GET":
            return render_template("home.html")
        elif request.method == "POST":
            # Get form data
            data = CustomData(
                gender=request.form.get("gender"),
                race_ethnicity=request.form.get("ethnicity"),
                parental_level_of_education=request.form.get("parental_level_of_education"),
                lunch=request.form.get("lunch"),
                test_preparation_course=request.form.get("test_preparation_course"),
                reading_score=float(request.form.get("reading_score")),
                writing_score=float(request.form.get("writing_score")),
            )

            pred = data.get_data_as_dataframe()
            print(pred)

            if pipeline is None:
                return render_template("home.html", results="Error: model not loaded")

            results = pipeline.predict(pred)
            return render_template("home.html", results=results[0])

    except Exception as e:
        print("Prediction error:", e)
        traceback.print_exc()
        return render_template("home.html", results=f"Error: {str(e)}")

# Dynamic port for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
