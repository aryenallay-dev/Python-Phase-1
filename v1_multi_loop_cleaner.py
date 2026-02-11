raw_data = [
    {"name": "Aryen", "score": 85},
    {"name": "Sunil", "score": "92"},  # String!
    {"name": "Beta", "score": -10},    # Negative!
    {"name": "Gamma", "score": None},  # Missing!
    {"name": "Alpha", "score": 100}
]

def clean_data(raw_list):
    number_score = []    #Stored only the scores of all the score keys
    for numbeers in raw_list:
        number_score.append(numbeers['score'])

    str_score = list(map(str, number_score))    #converted scores into str and removed all the char values
    for letters_remove in str_score:
        if letters_remove.isalpha():
            str_score.remove(letters_remove)
    
    int_score = list(map(int, str_score))   #Converted back into integers and then removed all the negative values
    for neg_remove in int_score:
        if neg_remove < 0:
            int_score.remove(neg_remove)
    

    
    str_score_again = list(map(str, int_score))   #Converted the values back to str to clean the original data
    for scores in raw_list:                       #Converts all 'score' values of the original data to string to clean
        scores['score'] = str(scores['score'])

    final_list = []                #Checks if the original data 'score' consists of any of the values fromthe score_list
    for integers in raw_list:      #If it exists then those dict are appended to a final_list
        if integers['score'] in str_score_again:
            final_list.append(integers)
    
    for last in final_list:   #converts the 'score' values back to int in the new clean final list
        last['score'] = int(last['score'])
    
    return final_list


def analyze_results(scores_list):
    number_score = []
    for numbeers in scores_list:
        number_score.append(numbeers['score'])

    str_score = list(map(str, number_score))
    for letters_remove in str_score:
        if letters_remove.isalpha():
            str_score.remove(letters_remove)
    
    int_score = list(map(int, str_score))
    for neg_remove in int_score:
        if neg_remove < 0:
            int_score.remove(neg_remove)
    total = sum(int_score)
    average = sum(int_score) / len(int_score)
    lowest = min(int_score)
    highest = max(int_score)

    return f'Total:{total}, Average: {average}, Lowest_value: {lowest}, Highest_value: {highest}'

cleaned_Score = clean_data(raw_data)     #Consist of the raw_data after being cleaned
analyzed_result = analyze_results(raw_data)    #Consists of total, avf, highest and lowest values

print(cleaned_Score)
print(analyzed_result)






