#!/usr/bin/env python3
import csv
import json
from collections import Counter, defaultdict
import re

def analyze_open_responses():
    """Extract and analyze all open-ended responses from the BC AI Survey"""
    
    # Read the CSV file
    with open('/Users/kk/Downloads/ai-hackathon-3/Hackathon round 3 with demos[48].csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    print(f"=== BC AI Survey - Open-Ended Response Analysis ===")
    print(f"Total Responses: {len(data)}")
    print()
    
    # Find all open-ended response columns
    oe_columns = [col for col in data[0].keys() if '_OE' in col and '_sentiment' not in col]
    print(f"Open-ended question columns found: {len(oe_columns)}")
    for col in oe_columns:
        print(f"  - {col}")
    print()
    
    # Analyze each open-ended question
    all_responses = {}
    
    for column in oe_columns:
        responses = []
        sentiments = []
        
        # Get corresponding sentiment column
        sentiment_col = f"{column}_sentiment"
        sentiment_score_col = f"{column}_sentiment_percentage"
        
        for row in data:
            if row[column] and row[column].strip():
                response_data = {
                    'text': row[column].strip(),
                    'sentiment': row.get(sentiment_col, ''),
                    'sentiment_score': row.get(sentiment_score_col, ''),
                    'age_group': row.get('AgeRollup_Broad', ''),
                    'location': row.get('Q1_Location_in_BC', ''),
                    'ai_experience': row.get('Q1_Experience_with_AI', '')
                }
                responses.append(response_data)
                if row.get(sentiment_col):
                    sentiments.append(row[sentiment_col])
        
        all_responses[column] = responses
        
        print(f"\n=== {column} ===")
        print(f"Total responses: {len(responses)}")
        
        if sentiments:
            sentiment_counts = Counter(sentiments)
            print("Sentiment breakdown:")
            for sentiment, count in sentiment_counts.most_common():
                percentage = (count / len(sentiments)) * 100
                print(f"  {sentiment}: {count} ({percentage:.1f}%)")
        
        # Show sample responses
        print(f"\nSample responses:")
        for i, resp in enumerate(responses[:5]):
            print(f"  {i+1}. \"{resp['text'][:100]}{'...' if len(resp['text']) > 100 else ''}\"")
            print(f"     Sentiment: {resp['sentiment']}, Age: {resp['age_group']}, Experience: {resp['ai_experience'][:30]}...")
        print()
    
    # Analyze Q2 Animal Comparisons
    print("\n=== Q2: AI Animal Comparisons Analysis ===")
    animal_responses = []
    for row in data:
        if row['Q2_Experience_with_AI_animal']:
            animal_responses.append(row['Q2_Experience_with_AI_animal'])
    
    animal_counts = Counter(animal_responses)
    print(f"Total animal comparison responses: {len(animal_responses)}")
    for animal, count in animal_counts.most_common(10):
        percentage = (count / len(animal_responses)) * 100
        print(f"  {animal}: {count} ({percentage:.1f}%)")
    
    # Look for interesting patterns in responses
    print("\n=== Pattern Analysis ===")
    
    # Find extremely negative responses
    print("\n--- Most Negative Responses ---")
    negative_responses = []
    for column, responses in all_responses.items():
        for resp in responses:
            if resp['sentiment'] == 'NEGATIVE' and resp['sentiment_score']:
                try:
                    score = float(resp['sentiment_score'])
                    if score > 0.95:  # Very negative
                        negative_responses.append((resp['text'], score, column))
                except:
                    pass
    
    negative_responses.sort(key=lambda x: x[1], reverse=True)
    for text, score, question in negative_responses[:10]:
        print(f"  Score {score:.3f}: \"{text[:150]}{'...' if len(text) > 150 else ''}\" ({question})")
    
    # Find extremely positive responses
    print("\n--- Most Positive Responses ---")
    positive_responses = []
    for column, responses in all_responses.items():
        for resp in responses:
            if resp['sentiment'] == 'POSITIVE' and resp['sentiment_score']:
                try:
                    score = float(resp['sentiment_score'])
                    if score > 0.95:  # Very positive
                        positive_responses.append((resp['text'], score, column))
                except:
                    pass
    
    positive_responses.sort(key=lambda x: x[1], reverse=True)
    for text, score, question in positive_responses[:10]:
        print(f"  Score {score:.3f}: \"{text[:150]}{'...' if len(text) > 150 else ''}\" ({question})")
    
    # Find unique/interesting responses
    print("\n--- Unusual/Creative Animal Comparisons ---")
    unique_animals = []
    for row in data:
        if row['Q2_Experience_with_AI_animal_other_OE']:
            unique_animals.append(row['Q2_Experience_with_AI_animal_other_OE'])
    
    for animal in unique_animals[:15]:
        print(f"  \"{animal}\"")
    
    # Demographic patterns
    print("\n=== Demographic Patterns in Open Responses ===")
    
    # Analyze by age group
    age_sentiments = defaultdict(lambda: defaultdict(int))
    for column, responses in all_responses.items():
        for resp in responses:
            if resp['age_group'] and resp['sentiment']:
                age_sentiments[resp['age_group']][resp['sentiment']] += 1
    
    print("\nSentiment by Age Group:")
    for age_group in ['18-34', '35-54', '55 Plus']:
        if age_group in age_sentiments:
            total = sum(age_sentiments[age_group].values())
            print(f"  {age_group} (total responses: {total}):")
            for sentiment, count in age_sentiments[age_group].items():
                percentage = (count / total) * 100
                print(f"    {sentiment}: {count} ({percentage:.1f}%)")
    
    return all_responses

if __name__ == "__main__":
    responses = analyze_open_responses()