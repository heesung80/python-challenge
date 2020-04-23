import os
import csv
output_path = os.path.join('.','Analysis','bank_final.txt')
with open(output_path,"w") as datafile:
#The total number of months included in the dataset
    budgetpath = os.path.join('.','Resources','budget_data.csv')
    with open(budgetpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter = ',')
        next(csvreader, None)
        csvlist = list(csvreader)
        number_of_months = len(csvlist)
        print ("Financial Analysis")
        datafile.write ("Financial Analysis\n")
        print ("-------------------------------------")
        datafile.write ("-------------------------------------\n")
        print("Total Months:" + str(number_of_months))
        datafile.write ("Total Months:" + str(number_of_months)+"\n")
#The net total amount of "Profit/Losses" over the entire period
        total_amount = 0
        csvfile.seek(0)
        next(csvreader, None)
        for row in csvreader:
            amount = row[1]
            total_amount += int(amount)
        print("Total: $"+str(total_amount))
        datafile.write ("Total: $"+str(total_amount)+"\n")

#The average of the changes in "Profit/Losses" over the entire period
        csvfile.seek(0)
        next(csvreader, None)
        csvlist = list(csvreader)
    #print(csvlist)
    #print(len(csvlist))
        total_change = 0
        max_change = 0
        min_change = 0
        for i in range(1,number_of_months) :
            before = csvlist[i-1][1]
            after = csvlist[i][1]
            change = int(after) - int(before)
            total_change += int(change)
            average = int(total_change) / (int(number_of_months)-1)
            average_decimal = ("%.2f"% average)
        
#The greatest increase in profits (date and amount) over the entire period
            if max_change < change:
                max_change = change
                max_date = csvlist[i][0]
            
#The greatest decrease in losses (date and amount) over the entire period
            elif min_change > change:
                min_change = change
                min_date = csvlist[i][0]

        print("Average Change: $" + str(average_decimal))
        datafile.write("Average Change: $" + str(average_decimal)+"\n")
        print("Greatest Increase in Profits: " + max_date+ " ($"+str(max_change)+")")
        datafile.write ("Greatest Increase in Profits: " + max_date+ " ($"+str(max_change)+")\n")
        print("Greatest Decrease in Profits: " + min_date+ " ($"+str(min_change)+")")
        datafile.write ("Greatest Decrease in Profits: " + min_date+ " ($"+str(min_change)+")")
