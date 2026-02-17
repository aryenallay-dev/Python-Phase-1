import copy

raw_data = [
    {"name": "Aryen", "score": 85},
    {"name": "Sunil", "score": "92"},  # String!
    {"name": "Beta", "score": -10},    # Negative!
    {"name": "Gamma", "score": None},  # Missing!
    {"name": "Alpha", "score": 100}
]

def clean_data(raw_list):
    new_list = []
    new_list = copy.deepcopy(raw_list)
    final_list = []
    for items in new_list:
        try:
            items['score'] = int(items['score'])
            if not items['score'] < 0:
                final_list.append(items)
        except:
            ValueError
            continue

    return final_list


def analyze_results(scores_list):
    new_scores = []
    new_scores = copy.deepcopy(scores_list)
    final_scores = []
    for scores in new_scores:
        try:
            scores['score'] = int(scores['score'])
            if not scores['score'] < 0:
                final_scores.append(scores['score'])
        except:
            ValueError

    total = sum(final_scores)
    avg = total / len(final_scores)
    highest = max(final_scores)
    lowest = min(final_scores)

    return f'Total: {total} \nAverage: {avg} \nHighest value: {highest} \nLowest value: {lowest}'

cleaned = clean_data(raw_data)
results = analyze_results(raw_data)

print(cleaned)
print(results)