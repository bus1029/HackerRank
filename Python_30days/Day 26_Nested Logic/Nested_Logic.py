r_day, r_month, r_year = list(map(int, input().split()))
d_day, d_month, d_year = list(map(int, input().split()))
fine = 0

# Book is returned on or before the expected return date
# No fine will be charged.
if r_year < d_year:
    print(str(fine))
elif r_year == d_year:
    if r_month < d_month:
        print(str(fine))
    elif r_month == d_month:
        if r_day <= d_day:
            print(str(fine))
        # Book is returned after the expected return day but still within the same calendar and year
        else:
            fine += 15 * (r_day - d_day)
            print(str(fine))
    # Book is returned after the expected return month but still within the same calendar year
    # as the expected return date
    else:
        fine += 500 * (r_month - d_month)
        print(str(fine))
# Book is returned after the calendar year in which it was expected
else:
    fine = 10000
    print(str(fine))


