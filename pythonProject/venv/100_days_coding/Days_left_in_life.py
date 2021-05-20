current_age = int(input("Enter your age :"))
expected_life_span = int(input("Enter your expected life span :"))
remaining = expected_life_span - current_age
print(remaining)                                #-------------------------------------
month_remaining = remaining * 12                # 12 month 52 weak 365 days in a year-
weak_remaining = remaining * 52                 #-------------------------------------
days_remaining = remaining * 365
print(f"You have {month_remaining} months {weak_remaining} weak & {days_remaining} days in your life ")
