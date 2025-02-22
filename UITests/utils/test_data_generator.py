import random
from constants import MAX_DEPENDENTS
from constants import MIN_DEPENDENTS

class TestDataGenerator:
    """Class responsible for generating random test data."""

    @staticmethod
    def generate_random_employee_data():
        dependents = random.randint(MIN_DEPENDENTS, MAX_DEPENDENTS)
        first_name = f"FirstName{random.randint(0, 1000)}"
        last_name = f"LastName{random.randint(0, 1000)}"
        return first_name, last_name, dependents