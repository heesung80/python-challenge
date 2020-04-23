import os
import csv

output_path = os.path.join('.','Analysis','election_final.txt')
with open(output_path,"w") as datafile:
#The total number of votes cast

    Pollpath = os.path.join('.','Resources','election_data.csv')
    with open(Pollpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader, None)
        csvlist = list(csvreader)
        number_of_votes = len(csvlist)
        print ("Election Results")
        datafile.write("Election Results\n")
        print ("----------------------------------")
        datafile.write("----------------------------------\n")
        print("Total Votes:" + str(number_of_votes))
        datafile.write("Total Votes:" + str(number_of_votes) + "\n")
        print ("----------------------------------")
        datafile.write("----------------------------------\n")
    
#A complete list of candidates who received votes
        csvfile.seek(0)
        next(csvreader, None)
        d = dict()
        for row in csvreader:
            name =row[2]
            if not name in d:
                d[name]=1
            else:
                d[name]=d[name]+1
    
#The percentage of votes each candidate won
#The total number of votes each candidate won
        name_list = list(d)
        vote_list = []
        percent_list =[]
    
        for name in name_list:
            vote_list.append(d[name])
            percent = int(d[name])/int(number_of_votes)*100
            decimal_percent = "%.3f"% percent
            percent_list.append(decimal_percent)
    
        for i in range(len(name_list)):
            print(name_list[i]+": "+ str( percent_list[i])+"% ("+ str(vote_list[i])+")")
            datafile.write(name_list[i]+": "+ str( percent_list[i])+"% ("+ str(vote_list[i])+")\n")
        print ("----------------------------------")
        datafile.write("----------------------------------\n")
#The winner of the election based on popular vote.
        winner = 0
        for p in vote_list:
            if winner < int(p):
                winner = int(p)
                location = vote_list.index(p)
        print("Winner: " + name_list[location])
        datafile.write ("Winner: " + name_list[location])
    

       
    

