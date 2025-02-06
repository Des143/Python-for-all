# Control Flow Assignment: Grade Classification

def classify_grade(score):
    """
    Classify student grade based on numerical score
    
    Args:
        score (float): Numerical score between 0 and 100
    
    Returns:
        str: Grade classification
    """
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    while True:
        try:
            score = float(input("Enter student score (0-100), or -1 to exit: "))
            
            if score == -1:
                break
            
            grade = classify_grade(score)
            print(f"Score: {score}, Grade: {grade}")
        
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()
