# Import necessary modules
import json
import os

# Define a function to collect user feedback
def collect_feedback():
    # Check if feedback file exists
    if os.path.isfile("feedback.json"):
        # If it exists, load feedback data
        with open("feedback.json", "r") as feedback_file:
            feedback_data = json.load(feedback_file)
    else:
        # If it doesn't exist, create empty feedback data
        feedback_data = {"feedback": []}

    # Ask user for feedback
    feedback = input("Please enter your feedback: ")

    # Add feedback to feedback data
    feedback_data["feedback"].append(feedback)

    # Save feedback data to file
    with open("feedback.json", "w") as feedback_file:
        json.dump(feedback_data, feedback_file)

    # Offer incentive for providing feedback
    print("Thank you for your feedback! As a token of our appreciation, please enjoy this exclusive content.")

# Call the function to collect feedback
collect_feedback()
