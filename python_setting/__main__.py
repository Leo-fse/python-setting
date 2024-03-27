# ! 割り算


def divide(x: int | float, y: int | float) -> float | None:
    """_summary_

    Args:
        x (int | float): _description_
        y (int | float): _description_

    Returns:
        float | None: _description_
    """
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        print(f"Error Occurred: {e}")


def python_setting():
    print("hello world!")


if __name__ == "__main__":
    python_setting()
