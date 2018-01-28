import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Simulate building_walk() 'number_of_participants' times and 'error_rate' factor
def building_walk(number_of_participants, error_rate):
    #Create empty lists for group totals and each participant
    group_total = []
    names = []
    #For each in range of total participant numbers
    for i in range(number_of_participants) :
        #Set name to Participant #i
        name = ["Participant: " + str(i)]
        #Set first step to 0
        individual_walk = [0]
        #For each x in range of 100
        for x in range(100) :
            #Assign move to last position in individual walk
            move = individual_walk[-1]
            #Dice = random roll from 1-7
            dice = np.random.randint(1,7)
            #If random roll lte, go down a floor
            if dice <= 2:
                move = max(0, move - 1)
            #Else if rand roll 3-5, move up a floor
            elif dice <= 5:
                move = move + 1
            #Else if roll 6-7, roll again and move up that value
            else:
                move = move + np.random.randint(1,7)
            #Apply error rate, if accessed reset to 0
            if np.random.rand() <= error_rate :
                move = 0
            #Add move to individual's record
            individual_walk.append(move)
        #Append individual's record to a larger group record
        group_total.append(individual_walk)
        #Add Participant to record by name
        names.append(str(name))
    #Combine names and movement records, move into DataFrame
    combo = dict(zip(names, group_total))
    df = pd.DataFrame(combo)
    return df

#Obtain last row in each column(final position of each participant)
def get_final_positions(raw_results):
    #Slice using index location, return final position for all participants
    sliced = raw_results.iloc[100:101, :]
    return sliced

#Transpose data and return summary statistics
def get_summary_statistics(sliced_results):
    sliced = sliced_results
    summary_stats = sliced.T.describe()
    return summary_stats

# Plot variable number of boxplots of final positions
def compare_boxplots(*args):
    plt.clf()
    plt.boxplot(args)
    plt.show()


#Testing logic/code
GroupA = building_walk(500, 0.001)
GroupB = building_walk(500, 0.01)
GroupC = building_walk(500, 0.1)

ResultsA = get_final_positions(GroupA)
ResultsB = get_final_positions(GroupB)
ResultsC = get_final_positions(GroupC)

#Generate a boxplot
compare_boxplots(ResultsA, ResultsB, ResultsC)
