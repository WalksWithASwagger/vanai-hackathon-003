#!/usr/bin/env python3
import csv
import json
from collections import Counter, defaultdict

def analyze_bc_ai_survey():
    """Analyze the BC AI Survey data systematically"""
    
    # Read the CSV file
    with open('/Users/kk/Downloads/ai-hackathon-3/Hackathon round 3 with demos[48].csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    print(f"=== BC AI Survey Analysis ===")
    print(f"Total Responses: {len(data)}")
    print()
    
    # Q1: AI Experience Levels
    print("=== Q1: AI Experience Levels ===")
    ai_experience = Counter(row['Q1_Experience_with_AI'] for row in data if row['Q1_Experience_with_AI'])
    for exp, count in ai_experience.most_common():
        percentage = (count / len(data)) * 100
        print(f"{exp}: {count} ({percentage:.1f}%)")
    print()
    
    # Q3: Overall AI Sentiment  
    print("=== Q3: AI Impact on Society Sentiment ===")
    ai_sentiment = Counter(row['Q3_AI_affecting_society_feeling'] for row in data if row['Q3_AI_affecting_society_feeling'])
    for sentiment, count in ai_sentiment.most_common():
        percentage = (count / len(data)) * 100
        print(f"{sentiment}: {count} ({percentage:.1f}%)")
    print()
    
    # Q9: Job Impact
    print("=== Q9: AI Impact on Jobs ===")
    job_impact = Counter(row['Q9_Jobs_in_BC_AI_Influence'] for row in data if row['Q9_Jobs_in_BC_AI_Influence'])
    for impact, count in job_impact.most_common():
        percentage = (count / len(data)) * 100
        print(f"{impact}: {count} ({percentage:.1f}%)")
    print()
    
    # Demographics: Age Groups
    print("=== Demographics: Age Groups ===")
    age_groups = Counter(row['AgeRollup_Broad'] for row in data if row['AgeRollup_Broad'])
    for age, count in age_groups.most_common():
        percentage = (count / len(data)) * 100
        print(f"{age}: {count} ({percentage:.1f}%)")
    print()
    
    # Demographics: Location
    print("=== Demographics: Location in BC ===")
    locations = Counter(row['Q1_Location_in_BC'] for row in data if row['Q1_Location_in_BC'])
    for location, count in locations.most_common():
        percentage = (count / len(data)) * 100
        print(f"{location}: {count} ({percentage:.1f}%)")
    print()
    
    # Q14: Government Role
    print("=== Q14: Government Role in Managing AI ===")
    gov_role = Counter(row['Q14_Govt_role_in_managing_AI'] for row in data if row['Q14_Govt_role_in_managing_AI'])
    for role, count in gov_role.most_common():
        percentage = (count / len(data)) * 100
        print(f"{role}: {count} ({percentage:.1f}%)")
    print()

if __name__ == "__main__":
    analyze_bc_ai_survey()