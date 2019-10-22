# Program 4-10 Tuition Inrease
# Shaun Hayworth
# CIS 2
# 10-22-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-10-Tuition-Increase

# Calculates a recurring 3% per year increase in tuition over 5 years, given an initial tuition cost
# of $8000.00.


# Initialize the INCREASE_MULTIPLIER constant at 1.03
# Change this value for different rates of increase.
INCREASE_MULTIPLIER = 1.03

# Initialize the tuition variable with a value of $8000
# Change this value for different starting costs.
tuition = 8000.0

# Initialize the years variable with a value of 5
# Change this to calculate different spans of time.
years = 5

# Initialize header string
header = '''
Year	 Projected Tuition (per Semester)
-----------------------------------------
'''

# Print header
print(header) 
# Loop calculation once for each year.
for time in range (1, years + 1):
    
    # Calculate the current tuition
    tuition *= INCREASE_MULTIPLIER

    # Print the year and current tuition.
    print(f'{time:<10.0f}{tuition:>15.2f}')