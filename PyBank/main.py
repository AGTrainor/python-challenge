import csv
import os

#function to count days
def count_days(file):
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None)

        days = 0
        for row in reader:
            days += 1
        return days

#function to calculate total profit 
def total_profit(csvfile, column_name):
    total = 0

    with open(csvfile, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = float(row[column_name])
            total += value

    return total

#function to count the average change in the data
def average_change(csvfile, column_name):
    with open(csvfile, 'r') as file:
        reader = csv.DictReader(file)
        previous_value = None
        total_change = 0
        count = 0
        max_change = 0
        max_date = ""
        min_change = 0
        min_date = ""

        for row in reader:
            current_value = float(row[column_name])
            if previous_value is not None:
                daily_change = current_value - previous_value
                total_change += daily_change
                count += 1
                if daily_change > max_change:
                    max_change = daily_change
                    max_date = row['Date']
                if daily_change < min_change:
                    min_change = daily_change
                    min_date = row['Date']
            previous_value = current_value

    average = total_change / count if count > 0 else 0
    return average, max_change, max_date, min_change, min_date

#variales for the program 
basefolder = os.path.dirname(os.getcwd())
csvfile = os.path.join(basefolder, "pybank", "Resources", "budget_data.csv")
column_name = "Profit/Losses"
days = count_days(csvfile)
column_sum = total_profit(csvfile, column_name)
formatted_sum = "${:.0f}".format(round(column_sum))
average, max_change, max_date, min_change, min_date = average_change(csvfile, column_name)
formatted_avg = "${:.2f}".format(round(average, 2))
formatted_max_change = "${:.0f}".format(round(max_change,0))
formatted_min_change = "${:.0f}".format(round(min_change,0))

#print output to terminal
print("\nFinancial Analysis\n")
print("-----------------------------\n")
print(f"Total Months: {days}\n")
print(f"Total: {formatted_sum}\n")
print(f"Average Change: {formatted_avg}\n")
print(f"Greatest Increase in Profits: {max_date} ({formatted_max_change})\n")
print(f"Greatest Decrease in Profits: {min_date} ({formatted_min_change})\n")

#print output to new file
output_file = os.path.join(basefolder, "pybank", "analysis", "results.txt")

with open(output_file, "w") as f:
    print("\nFinancial Analysis\n", file=f)
    print("-----------------------------\n", file=f)
    print(f"Total Months: {days}\n", file=f)
    print(f"Total: {formatted_sum}\n", file=f)
    print(f"Average Change: {formatted_avg}\n", file=f)
    print(f"Greatest Increase in Profits: {max_date} ({formatted_max_change})\n", file=f)
    print(f"Greatest Decrease in Profits: {min_date} ({formatted_min_change})\n", file=f)