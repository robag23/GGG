# Get the times for swimming, cycling, and running in minutes:

swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

# Calculate the total time:

total_time = swimming_time + cycling_time + running_time

# Determine the award based on the total time:

if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

# Display the result:
    
print(f"\nTotal time taken: {total_time} minutes")
print("Award:", award)