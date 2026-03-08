from data_processor import*

# List 1: Influencers (The Profile Data)
profiles = [
    {"user": "Aryen", "followers": 5000, "category": "Tech"},
    {"user": "Sunil", "followers": "12000", "category": "Finance"}, # String!
    {"user": "Beta", "followers": -500, "category": "Gaming"}      # Invalid!
]

# List 2: Engagement (The Performance Data)
posts = [
    {"user": "Aryen", "likes": 200, "comments": 50},
    {"user": "Sunil", "likes": 600, "comments": 150},
    {"user": "Gamma", "likes": 100, "comments": 20} # Missing Profile!
]

cleaned = merge_and_clean(profiles, posts)
cleaned_data_copy = copy.deepcopy(cleaned)
scores = calculate_metrics(cleaned_data_copy)
final = generate_report(scores)

print(cleaned)
print(scores)
print(final)
