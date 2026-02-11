raw_data = [
    {"name": "Aryen", "score": 85},
    {"name": "Sunil", "score": "92"},  # String!
    {"name": "Beta", "score": -10},    # Negative!
    {"name": "Gamma", "score": None},  # Missing!
    {"name": "Alpha", "score": 100}
]

def clean_data(raw_list):
    number_score = []
    for numbeers in raw_list:
        number_score.append(numbeers['score'])

    str_score = list(map(str, number_score))
    for letters_remove in str_score:
        if letters_remove.isalpha():
            str_score.remove(letters_remove)
    
    int_score = list(map(int, str_score))
    for neg_remove in int_score:
        if neg_remove < 0:
            int_score.remove(neg_remove)
    

    
    str_score_again = list(map(str, int_score))
    for scores in raw_list:
        scores['score'] = str(scores['score'])

    final_list = []
    for integers in raw_list:
        if integers['score'] in str_score_again:
            final_list.append(integers)
    
    for last in final_list:
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

print(clean_data(raw_data))
print(analyze_results(raw_data))



