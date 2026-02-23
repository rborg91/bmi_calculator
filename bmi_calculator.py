def bmi_calculation(weight, height):
    """
    Calculate the Body Mass Index (BMI), rounded to 2 decimal places.

    This function assumes:
        - weight is provided in kilograms (kg)
        - height is provided in centimetres (cm)

    Args:
        weight (float or int): The individual's weight in kilograms.
        height (float or int): The individual's height in centimetres.

    Returns:
        float: The calculated BMI value rounded to two decimal places.
    """

    bmi = round((weight / height / height * 10000), 2)
    return bmi


def bmi_category_calculation(bmi):
    """
    Determine the BMI category based on a BMI value.

    The classification is based on standard BMI ranges:
        - < 18.5: Underweight
        - 18.5–24.9: Normal weight
        - 25.0–29.9: Overweight
        - 30.0–34.9: Obese
        - 35.0–39.9: Severely obese
        - ≥ 40.0: Morbidly obese

    Args:
        bmi (float or int): The Body Mass Index value.

    Returns:
        str: The BMI category corresponding to the given BMI value.
    """
    if bmi > 0:
        if bmi < 18.5:
            bmi_category = "underweight"
        elif bmi <= 24.9:
            bmi_category = "normal weight"
        elif bmi <= 29.9:
            bmi_category = "overweight"
        elif bmi <= 34.9:
            bmi_category = "obese"
        elif bmi <= 39.9:
            bmi_category = "severely obese"
        else:
            bmi_category = "morbidly obese"

    return bmi_category


def main():
    name = input("Enter your first name: ")
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in centimetres (cm): "))
    bmi = bmi_calculation(weight, height)
    bmi_category = bmi_category_calculation(bmi)

    print(f"\nHello {name}")
    print(f"Your BMI is {bmi}")
    print(f"This is categorised as {bmi_category}")


if __name__ == "__main__":
    main()
