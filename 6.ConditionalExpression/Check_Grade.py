def check_grade(score):
    # Handle invalid inputs first (Guard clause)
    if score < 0 or score > 100:
        return "Invalid score! Please enter a value between 0 and 100."

    # Main decision structure
    if score >= 90:
        return "Grade: A (Excellent!)"
    elif score >= 80:
        return "Grade: B (Good job!)"
    elif score >= 70:
        return "Grade: C (Passed)"
    elif score >= 60:
        return "Grade: D (Needs improvement)"
    else:
        return "Grade: F (Failed)"


# --- Test the function ---
user_score = 85
result = check_grade(user_score)
print(f"Score: {user_score} -> {result}")
