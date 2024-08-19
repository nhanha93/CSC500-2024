years = int(input("Enter the number of year(s): "))

total_rain = 0
total_months = 0

for year in range(1, years + 1):
    print(f"Year {year}")

    for month in range(1, 13):
        rainfall = float(input(f"  Enter the amount of rain for month {month}: "))
        total_rain += rainfall
        total_months += 1

average_rain = total_rain / total_months

print(f"\nNumber of months: {total_months}")
print(f"Total amount of rain: {total_rain:.2f}")
print(f"Average rain amount per month: {average_rain:.2f} inches")
