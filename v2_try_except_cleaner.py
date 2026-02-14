raw_data = [
    {"name": "Aryen", "score": 85},
    {"name": "Sunil", "score": "92"},  # String!
    {"name": "Beta", "score": -10},    # Negative!
    {"name": "Gamma", "score": None},  # Missing!
    {"name": "Alpha", "score": 100}
]

def clean_data(raw_list):
    new_list = []     #appended everything to a new list of dict, just to be safe :D
    for items in raw_list:
        new_list.append(items)

    new_list2 = []    #created another list and appended every item if it converts to int, or else skip it
    for scores in new_list:
        try:
            scores['score'] = int(scores['score'])
            new_list2.append(scores)
        except:
            ValueError
            continue

    new_list3 = []     #A new list again but this time if the 'score' of the items is not below 0 we append those files
    for negative in new_list2:
        if not negative['score'] < 0:
            new_list3.append(negative)
        
    return new_list3    #returned only those with proper cleaned and which consist of positive int scores


def analyze_results(scores_list):   # A new function to use simulataniously with the first one
    only_scores = []      #Another new list to store only 'score' keyvalues 
    for scores in scores_list:
        only_scores.append(scores['score'])

    only_scores2 = []     #another list to check if those 'score' are an integer and store them in here
    for number in only_scores:
        try:
            number = int(number)
            only_scores2.append(number)
        except:
            ValueError
            continue
    
    only_scores3 = []   #sighhh another list to store all 'score' values from previous list, only if they are positive numbers
    for negative in only_scores2:
        if not negative < 0:
            only_scores3.append(negative)

    total = sum(only_scores3)   #total of the scores
    avg = total / len(only_scores3)  #average 
    highest = max(only_scores3)   #highest value
    lowest = min(only_scores3)     #lowest value

    return f'Total: {total} \nAverage: {avg} \nHighest value: {highest} \nLowest value: {lowest}'

cleaned = clean_data(raw_data)
results = analyze_results(raw_data)

print(cleaned)
print(results)