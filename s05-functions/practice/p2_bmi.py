def bmi(weight_lb, height_in):
    return round(703 * weight_lb / height_in**2, 1)


def category(value):
    if value < 18.5:
        return "underweight"
    if value < 25:
        return "healthy"
    if value < 30:
        return "overweight"
    return "obese"


score = bmi(160, 68)
print(score, category(score))
