'''
Author: Ashutosh
Last edit: June 15, 2024 at 15:08
Location: Ambikapur, CG
'''
'''
This is a simple marks telling program that takes the roll no as input and returns the marks for that roll no. If the roll no. does not exist, it is added for a temporary time till the time the program is being running. Once the program is closed, the added record gets deleted. The program will be modified afterwards so as to keep the added record permanently. Also deleting and changing any record will be possible in future.
'''

# Pre-existing records
Roll_no = [1, 2, 3, 4]
name = ['Ashu', 'Aditya', 'Tezas', 'Dhairya']
marks = [89, 80, 78, 90]

# Defining a module for running the main program again and again.
def tMarks():
    # Input is taken for doing further action.
    q = input('Hello! Welcome to our result data source.\nDo you want to see your result data or wanted to add your new result?(y/n)')

    if q == 'y':
        # If the user's answer is yes than the main program runs and asks for roll no.
        a = int(input('Enter your Roll Number: '))

        if a not in Roll_no:
            # If roll no does not exist, it asks whether to add it or not.
            n = input('Sorry that record does not exist.\n Do you want to add new record?(y/n)')

            if n == 'y':
                # If user wanted to add the data, it asks name and marks, and adds the roll no which was given earlier
                Roll_no.append(a)
                nName = input('Enter your name: ')
                nMarks = input('Enter your marks: ')
                name.append(nName)
                marks.append(nMarks)
                print('Your data has been added. You could now see your result by entering your data.')
                return tMarks() # after the data has been added, the user is asked again, if he/she wanted to see the record.
            
            elif n == 'n':
                # If user don't wanted to add a new record, program gets over.
                print('OK. You are now exiting our data soure.')

        elif a in Roll_no:
            # If the roll no provided in starting is present in the record, the program returns name and marks of that particular roll no and the main program runs again.
            b = Roll_no.index(a)
            print("Marks for", name[b], 'is', marks[b])
            return tMarks()
    
    elif q == 'n':
        # If user do not wanted to see the result the main program gets over.
        print('OK. You are now exiting our data soure.')
                
tMarks()