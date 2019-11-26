import random
import csv


# Read the data, every raw as a single member's votes.
def read_data_file(file_name):
    elections = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            member_votes = []
            for vote in row:
                member_votes.append(vote)
            elections.append(member_votes)
    return elections


# Select the rows that will be used for data training (Randomly).
def select_data_for_training(elections_data, training_percentage):
    selected_data = []
    # To get some data using the percentage,
    # so we will do ==> size of data * percentage we need.
    for i in range(int(len(elections_data) * training_percentage)):
        # Select the row randomly
        r = int(random.uniform(0, len(elections_data)))
        selected_data.append(elections_data[r])
        # Remove it from the list to not be selected again.
        elections_data.pop(r)
    return selected_data


# We need to predict the political_party
# The headers of data
def make_header(elections_data):
    header = ['political_party']
    # Get the number of issues(16) and make a header for him/her.
    for i in range(1, len(elections_data[0])):
        header.append('v' + str(i))
    return header


# Get the Unique values for each column, from its index in the data.
def unique_values(elections_data, col):
    return set(row[col] for row in elections_data)


elections_data = read_data_file('../../ML-Assi1-2/Problem1 Dataset/house-votes-84.data.txt')

header = make_header(elections_data)

political_party_unique_values = unique_values(elections_data, 0)
votes_unique_values = unique_values(elections_data, 1)

print(select_data_for_training(elections_data, .25))
