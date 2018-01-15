import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Simulate building_walk() 'number_of_participants' times and 'error_rate' factor
def building_walk(number_of_participants, error_rate):
    group_total = []
    names = []

    for i in range(number_of_participants) :
        name = ["Participant: " + str(i)]
        individual_walk = [0]
        for x in range(100) :
            move = individual_walk[-1]
            dice = np.random.randint(1,7)
            if dice <= 2:
                move = max(0, move - 1)
            elif dice <= 5:
                move = move + 1
            else:
                move = move + np.random.randint(1,7)
            if np.random.rand() <= error_rate :
                move = 0
            individual_walk.append(move)
        group_total.append(individual_walk)
        names.append(str(name))
    combo = dict(zip(names, group_total))
    df = pd.DataFrame(combo)
    return df

#Obtain last row in each column(final position of each participant)
def get_final_positions(raw_results):
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


#Testing
GroupA = building_walk(500, 0.001)
GroupB = building_walk(500, 0.01)
GroupC = building_walk(500, 0.1)

ResultsA = get_final_positions(GroupA)
ResultsB = get_final_positions(GroupB)
ResultsC = get_final_positions(GroupC)

compare_boxplots(ResultsA, ResultsB, ResultsC)
