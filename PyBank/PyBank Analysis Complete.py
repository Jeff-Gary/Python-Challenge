#This is my PyBank Analysis 

#Import Required Libraries 
import pandas as pd

#Import CSV File into a Dataframe
df = pd.read_csv('budget_data.csv')

#Total Unique Months / Sum of Profit and Losses
total_months = df['Date'].nunique()
total_profit = df['Profit/Losses'].sum()

#Calculate Changes and find the Average Change
df['Change'] = df['Profit/Losses'].diff()
average_change = df['Change'].mean()

#Finding the Greatest Increase and Decrease
greatest_increase = df['Change'].max()
greatest_decrease = df['Change'].min()

#Find the Corresponding Dates
greatest_increase_date = df.loc[df['Change']== greatest_increase, 'Date'].item()
greatest_decrease_date= df.loc[df['Change'] == greatest_decrease, 'Date'].item()

#Print Analysis

results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
with open('financial_analysis.txt', 'w') as f:
    f.write(results)


