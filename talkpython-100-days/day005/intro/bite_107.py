def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return [num for num in numbers if num > 0 and num % 2 == 0]
