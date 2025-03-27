import json
import os

class Person:
    def __init__(self, height, weight, gender):
        self.height = height
        self.weight = weight
        self.gender = gender

    def calculate_bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def recommend_fitness(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight: Consider gaining weight through a balanced diet and exercise."
        elif 18.5 <= bmi < 24.9:
            return "Normal weight: Maintain your current lifestyle and stay active."
        elif 25 <= bmi < 29.9:
            return "Overweight: Consider a balanced diet and regular exercise."
        else:
            return "Obesity: It's advisable to consult with a healthcare provider."

    def save_to_file(self, filename):
        data = {
            'height': self.height,
            'weight': self.weight,
            'gender': self.gender,
            'bmi': self.calculate_bmi()
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

class FitnessRecommendation(Person):
    def __init__(self, height, weight, gender, activity_level):
        super().__init__(height, weight, gender)
        self.activity_level = activity_level  

    def fitness_plan(self):
        if self.activity_level == 'low':
            return "Start with 30 minutes of walking 3 times a week."
        elif self.activity_level == 'moderate':
            return "Include strength training and aerobic exercises 3-4 times a week."
        elif self.activity_level == 'high':
            return "Consider a combination of strength, cardio, and flexibility exercises 5-6 times a week."
        else:
            return "Invalid activity level."

def main():
    while True:
        # try:
        #     filename = 'fitness_data.json'
        #     with open(filename) as json_file:
        #         data = json.load(json_file)
        #     print(f"Saved data:{data}")  
        # except Exception as e:
        #     print(f"An error occurred could not find saving data: {e}") 
        #     break
        try:
            height = int(input("Enter your height in cm: "))
            weight = int(input("Enter your weight in kg: "))
            gender = input("Enter your gender (M/F): ").strip().upper()
            if gender not in ['M', 'F']:
                raise ValueError("Gender must be 'M' or 'F'.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        
    activity_level = ''
    while activity_level not in ['low', 'moderate', 'high']:
        activity_level = input("Enter your activity level (low, moderate, high): ").strip().lower()

    person = FitnessRecommendation(height, weight, gender, activity_level)
    
    print(f"Your BMI is: {person.calculate_bmi():.2f}")
    print(person.recommend_fitness())
    print(person.fitness_plan())

    person.save_to_file('fitness_data.json')

if __name__ == "__main__":
    main()
