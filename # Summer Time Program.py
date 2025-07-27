# Summer Time Program

# Get user input for temperature and time of day
temperature = float(input("Enter the current temperature in °C: "))
time_of_day = input("Enter the time of day (morning/afternoon/evening): ").lower()

print("\n🌞 Summer Time Suggestion 🌴")

# Use conditional statements to suggest activities
if temperature > 35:
    if time_of_day == "afternoon":
        print("It's very hot! Stay indoors, hydrate, and maybe enjoy some ice cream 🍦.")
    elif time_of_day == "morning":
        print("Great time for a quick early morning walk! Don't forget sunscreen ☀️.")
    else:
        print("Hot evening! Try a cold shower and relax with a movie 🎬.")
elif 25 <= temperature <= 35:
    if time_of_day == "morning":
        print("Perfect morning weather! Go jogging or have breakfast outside 🥐.")
    elif time_of_day == "afternoon":
        print("Nice weather! Go swimming or visit the beach 🏖️.")
    else:
        print("Enjoy a peaceful evening walk or watch the sunset 🌅.")
elif 15 <= temperature < 25:
    print("It's a bit cool for summer. Consider a light jacket if you're going out 🧥.")
else:
    print("Unusually cold for summer. Stay warm and maybe make some hot cocoa ☕.")

print("\nHave a fun and safe summer! 😎")