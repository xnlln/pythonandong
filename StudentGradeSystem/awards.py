def determine_award(average):
    if 97 <= average <= 100:
        return "WITH HIGHEST HONORS"
    elif 95 <= average <= 96:
        return "WITH HIGH HONORS"
    elif 90 <= average <= 94:
        return "WITH HONORS"
    else:
        return "NO AWARD"