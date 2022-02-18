#Habit Tracker (Final Project)
#Written by Evan Fuccio

"""
My 4 Topics:
1. Tuples
2. files
3. for loop
4. if...elif...else

Program Description
My program generates a file that allows someone to create a new habit by making sure that they finish their task everyday. This is because it is widely known that a task, when repeated for a whole month, will start to become a habit. Because this information is written to a file called a "Habit Schedule" the user is able to update it by running the program once per day. At the end of the month, they will see their overall score which is increased when the user does the task and is reduced when they fail to. The user will attempt to get the highest score possible to create a new good habit.

My Program:
"""
#create tuples of the months and their corresponding length
THIRTY_ONE_DAY_MONTHS = ('January', 'january', 'March', 'march', 'May', 'may', 'July', 'july', 'August', 'august', "October", "october", "December", "december")
THIRTY_DAY_MONTHS = ('April', 'april', 'June', 'june', 'September', 'september', 'November', 'november')
TWENTY_EIGHT_DAY_MONTHS = ('February', 'february')


def calendar_maker(month): #creates calendar file

  habit_schedule = open('Habit Schedule', 'w') #opens a new file called habit_schedule for writing to
  i = 1 #sets i to one so that day 0 doesn't have completed 

  if month in THIRTY_ONE_DAY_MONTHS:
    #creates a file with 31 days
    habit_schedule.write(f'Habit Tracker for the month of {month}\n')
    for i in range(0,31):
      habit_schedule.write(f'Day {i+1}: \n')
    habit_schedule.write('YOUR SCORE IS 500\n') #writes the initial score of 500
    habit_schedule.close()

  elif month in THIRTY_DAY_MONTHS:
    #creates a file with 30 days
    habit_schedule.write(f'Habit Tracker for the month of {month}\n')
    for i in range(0,30):
      habit_schedule.write(f'Day {i+1}: \n')
    habit_schedule.write('YOUR SCORE IS 500\n') #writes the initial score of 500
    habit_schedule.close()

  elif month in TWENTY_EIGHT_DAY_MONTHS:
    #creates a file with 28 days
    habit_schedule.write(f'Habit Tracker for the month of {month}\n')
    for i in range(0,28):
      habit_schedule.write(f'Day {i+1}: \n')
    habit_schedule.write('YOUR SCORE IS 500\n') #writes the initial score of 500
    habit_schedule.close()

  else:
    print('Error: month entered not valid. Please try again.\n')
  
def task_checker():

  day = input('What day of the month is it? ') #asks the user the day of the month
  day = int(day.strip(' stndrh')) #removes any st nd rd extentions from the day and make it an integer

  if day > 31: #checks if the user inputs an inproper day
    print('Error: That day is not valid')
  else:
    task_complete = input('Have you completed your task today? ')
    if task_complete == 'yes':
      

      schedule_file = open("Habit Schedule", "r") #opens the file

      list_of_lines = schedule_file.readlines() #assigns the file content to list_of_lines

      list_of_lines[day] = f"Day {day}: Task Completed!\n" #changes the content of the selected day to say that the task has been completed


      a_file = open("Habit Schedule", "w") #open file for writing

      a_file.writelines(list_of_lines) #write the updated content to the file

      a_file.close()

      update_score = True
      return update_score #returns update_score as True to tell the score_updater function to change the score
    else:
      schedule_file = open("Habit Schedule", "r") #opens the file

      list_of_lines = schedule_file.readlines() #assigns the file content to list_of_lines

      list_of_lines[day] = f"Day {day}: Task NOT Completed!\n" #changes the content of the selected day to say that the task has been completed


      a_file = open("Habit Schedule", "w") #open file for writing

      a_file.writelines(list_of_lines) #write the updated content to the file

      a_file.close()

      update_score = False
      return update_score

    


def score_updater():

  if task_checker() == True: #If the task has been completed as indicated by task_checker function
    #read file and assign lines to score_line
    habit_schedule = open ('Habit Schedule', 'r')
    score_line = habit_schedule.readlines()

    #remove 'YOUR SCORE IS' and newline from the last line
    score = score_line[-1].replace('YOUR SCORE IS', '')
    score = int(score.strip('\n!')) +100 #add 100 to the score

    score_line[-1] = f'YOUR SCORE IS {score}!' #update the score line

    #write the new updated score_line and close file
    update_score_line = open('Habit Schedule', 'w')
    update_score_line.writelines(score_line)
    update_score_line.close()

  else: #if task checker is false aka the task was not completed minus 100 from the score
    habit_schedule = open ('Habit Schedule', 'r')
    score_line = habit_schedule.readlines()

    score = score_line[-1].replace('YOUR SCORE IS', '')
    score = int(score.strip('\n!')) -100 #minus 100 to the score

    score_line[-1] = f'YOUR SCORE IS {score}!'
    update_score_line = open('Habit Schedule', 'w')
    update_score_line.writelines(score_line)
    update_score_line.close()



def main():
  #asks the user if this is the first time running the program and gets month
  new_check = input('Is this the first time you have opened this program? ')
  
  if new_check == 'y' or new_check == 'Y' or new_check == 'yes' or new_check == 'Yes':
    month = input("What month is it? ")
    #if the inputted month is within the lists pass the month to the calendar_maker function and update the score
    if month in THIRTY_DAY_MONTHS or month in THIRTY_ONE_DAY_MONTHS or month in TWENTY_EIGHT_DAY_MONTHS:
      calendar_maker(month) #generate calendar file
      score_updater() #update the score
    else:
      print('Error: Try again and enter a correct month.')
  elif new_check == 'n' or new_check == 'N' or new_check == 'no' or new_check == 'No':
    score_updater() #update the score
  else:
    print("Error: Try again and respond with yes or no.")
  
main()

