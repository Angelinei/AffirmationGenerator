def get_day_affirmation():
  name = input("Your name: ")
  print("\nDays of the week:")
  print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday")
  print("5. Friday\n6. Saturday\n7. Sunday")
  day_num = int(input("\nEnter the day number (1-7): "))

  # Get user's mood
  mood = input("\nHow are you feeling today? (good/bad): ").lower()

  # Base affirmation that includes their name
  base_affirmation = f"Dear {name}, "

  # Select day-specific affirmation
  if day_num == 1:  # Monday
      day_affirmation = "the start of a new week brings endless possibilities."
  elif day_num == 2:  # Tuesday
      day_affirmation = "you have the power to make today amazing."
  elif day_num == 3:  # Wednesday
      day_affirmation = "you're halfway through the week and doing great."
  elif day_num == 4:  # Thursday
      day_affirmation = "your determination will lead you to success."
  elif day_num == 5:  # Friday
      day_affirmation = "you've worked hard and deserve to celebrate."
  elif day_num == 6:  # Saturday
      day_affirmation = "take time to appreciate your achievements."
  else:  # Sunday
      day_affirmation = "rest and recharge, you're worth it."

  # Add mood-specific encouragement
  if mood == "good":
      mood_boost = "\nKeep spreading your positive energy to others!"
  else:
      mood_boost = "\nRemember that tough times are temporary, and you are stronger than you think!"

  # Combine all parts
  final_affirmation = base_affirmation + day_affirmation + mood_boost
  return final_affirmation

# Run the affirmation generator
print("\n=== Daily Affirmation Generator ===\n")
affirmation = get_day_affirmation()
print("\nYour Daily Affirmation:")
print("-----------------------------")
print(affirmation)
print("-----------------------------")