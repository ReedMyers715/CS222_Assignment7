def calculate_grade(grade):
    if not isinstance(grade, (float, int)):
        raise TypeError("Grade must be a number")
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")
    
    if grade >= 90 and grade <= 100:
        return "A"
    if grade >= 80 and grade < 90:
        return "B"
    if grade >= 70 and grade < 80:
        return "C"
    if grade >= 60 and grade < 70:
        return "D"
    else:
        return "F"