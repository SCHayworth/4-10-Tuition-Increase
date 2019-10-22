# Scope
At one college, the tuition for a full-time student is $8,000 per semester. It has been announced that the tuition will increase by 3 percent each year for the next five years. Write a program with a loop that displays the projected semester tuition amount for the next five years.


### Sample Run

    Year	 Projected Tuition (per Semester)
    -----------------------------------------
    1 	                $ 8240.00
    2 	                $ 8487.20
    3 	                $ 8741.82
    4 	                $ 9004.07
    5 	                $ 9274.19

# Pseudocode
    START
    Set increase multiplier constant to 1.03
    Set tuition to 8,000
    Print header string:
        Year	 Projected Tuition (per Semester)
    -----------------------------------------
    FOR each year starting at 1 and ending at 5
        Calculate the new tuition
            tuition * increase multiplier
        set tuition to the result
        print current year and projected tuition
    END
