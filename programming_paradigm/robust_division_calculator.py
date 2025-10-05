def safe_divide(numerator, denominator):
    """
    Performs safe division, handling division by zero and non-numeric inputs.
    Returns a user-friendly message.
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
