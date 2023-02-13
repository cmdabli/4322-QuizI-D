'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

def main():

#open the file
    infile = open('employee_data.csv', 'r')
    reader = csv.reader(infile)
    next(reader)

#create an empty dictionary
    employeeData = {}


#use a loop to iterate through the csv file
    for row in reader:
        name = row[1]
        salary = row[5]
        title = row[4]
        department = row[3]


    #check if the employee fits the search criteria
        if title == 'CSR' and department == 'marketing':
            new_salary = str(int(salary) * 1.10)

            employeeData[name] = new_salary
#close the file
    infile.close()


#iterate through the dictionary and print out the key and value as per printout
    for name, new_salary in employeeData.items():
        print(f'{name}: ${new_salary}')


main()    
        

        
    
