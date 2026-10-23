print("----Welcome to smart fittness planner-----")
user_input=input("ENTER YOUR NAME: ")
print(/n "Welcome",user_input )
print(" Here is our menu pleae type your choice" "\n1. Weight Loss",
"\n2. Weight Gain"
,"\n3. Muscle Building",
"\n4. General Fitness")
choice=int(input("Enter your choice: "))
if choice==1:
    print("Start your Weight loss journey")
    weight_loss=int(input("Enter Current Weight: "))
    loss_target=int(input("Enter Target Weight: "))
    loss_days=int(input("Enter Number of Days: "))
    if loss_days<=30:
        print("Here Is  Your today's Workout and Diet Plane")
        print("==========================================================")
        print("Warm-up: 5 Mins Stretching.")

        print("Circuit Training (Do 3 Rounds")

        print("\n High Knees - 45 Seconds","/nBurpees - 12 Reps","/nMountain Climbers - 45 Seconds","\nJump Squats - 15 RepsCore: Plank Hold - 1 Minute.","\nCool Down: 5 Mins walking and deep breathing.")
        print("---DIET PLAN FOR TODAY---")
        print(" PURE VEGETARIAN CLEAN DIET CHART:""\n---------------------------------","\n Early Morning: 1 Glass Warm Water with Lemon or Jeera water.", "\n- Breakfast    : Oats with low-fat milk OR a heavy bowl of Sprouts Salad / Moong Dal Chilla.","\n- Lunch        : 1 Multigrain Roti + 1 Big Bowl of Dal OR Soya Chunks Curry + Low-fat Curd + Green Salad.","\n- Evening Snack: Green Tea + a handful of Roasted Makhana (Foxnuts) or 5-6 Almonds.""\n- Dinner       : Mixed Vegetable Soup with 50g-70g of Grilled/Stir-fried Paneer (Before 8 PM).","\n- Golden Rule  : Strictly NO Sugar, NO Fried Food! Drink 3-4 Liters of water daily.")
    else:
        print("Here Is  Your today's Workout and Diet Plane")
        print("==========================================================")
        print("\n TODAY'S WORKOUT ROUTINE:")
      
        print("1. Warm-up   : 10 Mins (Light Stretching & Spot Jogging)")
        print("2. Cardio    : 20-30 Mins of Steady Running or Brisk Walking")
        print("3. Strength  : 3 Sets x 15 Reps of Bodyweight Squats")
        print("4. Upper Body: 3 Sets x 10 Reps of Modified/Knee Push-ups")
        print("5. Core      : 3 Sets x 30 Seconds Plank Hold")
        print("6. Cool Down : 5 Mins of Deep Breathing and Full Body Stretching")
            
        print("\n  DIET PLAN:")
        print("------------------------------------")
        print("- Breakfast    : Vegetable Poha or Upma OR 2 Besan Chillas.")
        print("- Lunch        : 2 Multigrain Rotis + 1 Bowl of Seasonal Veggies + 1 Bowl of Dal + Curd.")
        print("- Evening Snack: 1 Seasonal Fruit (Apple/Papaya) OR Green Tea with 5-6 Almonds.")
        print("- Dinner       : 1 Large Bowl of Khichdi with Veggies OR Soya Chunks Salad (Before 8:30 PM).")
        print("- Golden Rule  : Limit your portion sizes and drink 3 Liters of water daily.")

        
elif choice==2:
    print("Start your Weight Gain journey")
    weight_gain=int(input("Enter Current Weight: "))
    gain_target=int(input("Enter Target Weight: "))
    gain_days=int(input("Enter Number of Days: "))
    if gain_days<=30:
        print("Here Is  Your today's Workout and Diet Plane")
        print("==========================================================")
        print("1. 5 Mins Warm-up (Light Stretching & Rotating Joints)")
        print("2. Weight Training (Focus on heavy movements, 3 Sets x 8-10 Reps):")
        print("   - Weighted Squats (Heavy legs workout)")
        print("   - Push-ups / Bench Press (Chest & Arms)")
        print("   - Dumbbell Rows / Pull-ups (Back strength)")
        print("3. Cool Down: 5 Mins Normal Stretching")
        
        print("\n  DIET CHART:")
        print("---------------------------------------")
        print("- Early Morning: 1 Glass Full-fat Milk + 1 Banana OR 5-6 Almonds & Raisins.")
        print("- Breakfast    : 2 Paneer Paranthas with Curd OR Heavy bowl of Oats with Milk, Honey & Nuts.")
        print("- Lunch        : 2-3 Rotis + 1 Large Bowl of Rice + Heavy Bowl of Dal + 100g Paneer/Soya.")
        print("- Evening Snack: Banana Shake with Peanut Butter OR Roasted Chana with Jaggery (Gud).")
        print("- Dinner       : 2 Rotis + Rice + Thick bowl of Dal/Rajma + Potato Veggie (Before 9 PM).")
        print("- Golden Rule  : Don't drink water just before meals. Eat every 2-3 hours!")
    else:
            print("Here Is  Your today's Workout and Diet Plane")
            print("==========================================================")
            print("1. Warm-up   : 5 Mins Light Cardio")
            print("2. Split Routine (Focus on 1-2 muscle groups daily, 4 Sets x 12 Reps):")
            print("   - Day A: Chest & Triceps (Bench press, Dips)")
            print("   - Day B: Back & Biceps (Lat pulldown, Bicep curls)")
            print("   - Day C: Legs & Shoulders (Squats, Shoulder press)")
            print("3. Core      : 2 Sets x 45 Seconds Plank Hold")
            print("4. Cool Down : 5 Mins Stretching")
            
            print("\n                  BULK DIET:")
            print("-------------------------------------")
            print("- Breakfast    : 3-4 Slices of Whole Wheat Bread with Peanut Butter + 1 Glass Milk.")
            print("- Lunch        : 2 Multigrain Rotis + Veggies + 1 Bowl of Curd + Soya Chunks Rice.")
            print("- Evening Snack: A bowl of Boiled Kala Chana Chat OR 1 Plate Poha with Peanuts.")
            print("- Dinner       : 2 Rotis + 1 Bowl Paneer Bhurji / Tofu + Green Salad (Before 9 PM).")
            print("- Golden Rule  : Focus on consistent clean eating and track your strength progress weekly.")


elif choice==3:
        print("\n--- Muscle Building Journey ---")
        weight_muscle=int(input("Enter Current Weight (kg): "))
        gain_target=input("Enter Targeted Area: ").lower().strip()
        gain_days=int(input("Enter Number of Days: "))
        experience=input("Enter Experience [easy/medium/hard]: ").lower().strip()
        
        daily_protein = weight_muscle * 1.8
        
        if experience == "easy":
            print(f"\nTarget Protein: {daily_protein:.1f}g | Days: {gain_days} | Target: {gain_target.upper()}")
            print("\n WORKOUT: Warm-up -> Knee Push-ups / Squats -> Stretching")
            print(" DIET   : Moong Dal Chilla / Oats / Banana Shake / Paneer")
            
        elif experience == "medium":
            print(f"\nTarget Protein: {daily_protein:.1f}g | Days: {gain_days} | Target: {gain_target.upper()}")
            print("\n WORKOUT: Light Cardio -> Bench Press / Dumbbell Squats -> Stretching")
            print(" DIET   : Oats Smoothie / Rajma Rice / Kala Chana / Soya Curry")
            
        elif experience == "hard":
            print(f"\nTarget Protein: {daily_protein:.1f}g | Days: {gain_days} | Target: {gain_target.upper()}")
            print("\n WORKOUT: Dynamic Warm-up -> Heavy Bench Press / Barbell Squats -> Foam Rolling")
            print(" DIET   : Peanut Butter Bread / Grilled Paneer / Whey or Chana / Tofu Bhurji")
            
        else:
            print("\n Invalid Experience Level!")

elif choice==4:
        print("\n--- General Fitness & Wellness Journey ---")
        fitness_days=int(input("Enter Number of Days: "))
        daily_time=int(input("How many minutes can you workout daily?: "))
        
        if daily_time < 45:
            print(f"\nDuration: {fitness_days} Days | Daily Time: {daily_time} Mins (Short Routine)")
            print("\nYOGA & PRANAYAM : 10 Mins Anulom Vilom & Surya Namaskar")
            print("ACTIVITY        : 15 Mins Brisk Walking")
            print("MEAL            : Balanced Homemade Food (Kam Tel/Cheeni)")
            print("SELF & SKINCARE : 8 Hours Sleep + Hydration + Basic Moisturizer & Sunscreen")
            
        else:
            print(f"\nDuration: {fitness_days} Days | Daily Time: {daily_time} Mins (Full Routine)")
            print("\nYOGA & PRANAYAM : 15 Mins Kapalbhati, Anulom Vilom & Deep Stretching")
            print("ACTIVITY        : 30 Mins Power Walking or Light Jogging")
            print("MEAL            : High-fiber Veggies + Fruits + Curd + Dal Khichdi")
            print("SELF & SKINCARE : Meditating 5 Mins + Cleanser, Toner & Moisturizer Routine")
else:
    print("Invalid Choice")


