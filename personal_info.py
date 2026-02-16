# # Kaitha Bhanu Teja
# A simple Python program that collects and stores personal details like name, age, city, and hobby using variables and user input.
# It displays the information in a clean format, performs a small calculation (age in months), and demonstrates basic Python concepts.


# ========================================
#        PERSONAL INFORMATION MANAGER
# ========================================

print("========================================")
print("    PERSONAL INFORMATION MANAGER")
print("========================================\n")

name = "Alex Johnson"        # string: stores name
age = 22                     # integer: stores age
city = "San Francisco"       # string: stores city
hobby = "playing guitar"     # string: stores hobby

print("Please tell me about yourself:")
print("------------------------------")

fav_food = input("What's your favorite food? ").strip()
if fav_food == "":
    fav_food = "Not provided"

fav_color = input("What's your favorite color? ").strip()
if fav_color == "":
    fav_color = "Not provided"

age_in_months = age * 12

print("\n========================================")
print("        YOUR INFORMATION")
print("========================================\n")

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}\n")

print(f"Favorite Food: {fav_food}")
print(f"Favorite Color: {fav_color}")

print("\n========================================")
print("Thanks for using this program!")
print("========================================")
