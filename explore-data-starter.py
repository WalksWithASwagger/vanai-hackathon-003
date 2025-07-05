#!/usr/bin/env python3
"""
BC AI Survey Data Explorer - Hackathon Starter Script
=====================================================

A friendly introduction to the BC AI Survey dataset.
Perfect for getting started with data exploration!

Usage:
    python explore-data-starter.py

Requirements:
    pip install pandas

"""

import pandas as pd
import sys
from pathlib import Path

def explore_bc_ai_survey():
    """Explore the BC AI Survey data with helpful guidance"""
    
    # Find the data file
    data_file = "Hackathon round 3 with demos[48].csv"
    if not Path(data_file).exists():
        print(f"■ Data file not found: {data_file}")
        print("Make sure you're running this script from the repository root directory.")
        return
    
    print("■ BC AI Survey Data Explorer")
    print("=" * 50)
    
    try:
        # Load the data
        print("■ Loading survey data...")
        df = pd.read_csv(data_file)
        print(f"■ Loaded {len(df)} responses with {len(df.columns)} columns")
        print()
        
        # Basic overview
        print("■ Dataset Overview:")
        print(f"   • Total responses: {len(df):,}")
        print(f"   • Total columns: {len(df.columns):,}")
        print(f"   • Response rate: ~{len(df)} out of 1,001 target")
        print()
        
        # Find key column types
        oe_columns = [col for col in df.columns if '_OE' in col and 'sentiment' not in col]
        sentiment_columns = [col for col in df.columns if 'sentiment_percentage' in col]
        demo_columns = ['AgeRollup_Broad', 'Q1_Location_in_BC', 'Q1_Experience_with_AI']
        
        print("■ Column Categories:")
        print(f"   • Open-ended responses (_OE): {len(oe_columns)}")
        print(f"   • Sentiment scores: {len(sentiment_columns)}")
        print(f"   • Demographic fields: {len(demo_columns)}")
        print()
        
        # Demographics snapshot
        print("■ Demographics Snapshot:")
        if 'AgeRollup_Broad' in df.columns:
            age_dist = df['AgeRollup_Broad'].value_counts()
            for age, count in age_dist.items():
                pct = (count / len(df)) * 100
                print(f"   • {age}: {count} ({pct:.1f}%)")
        print()
        
        if 'Q1_Location_in_BC' in df.columns:
            print("■ Geographic Distribution:")
            location_dist = df['Q1_Location_in_BC'].value_counts().head(5)
            for location, count in location_dist.items():
                pct = (count / len(df)) * 100
                print(f"   • {location}: {count} ({pct:.1f}%)")
        print()
        
        # AI Experience levels
        if 'Q1_Experience_with_AI' in df.columns:
            print("■ AI Experience Levels:")
            exp_dist = df['Q1_Experience_with_AI'].value_counts()
            for exp, count in exp_dist.items():
                pct = (count / len(df)) * 100
                print(f"   • {exp}: {count} ({pct:.1f}%)")
        print()
        
        # Sample some interesting quotes
        print("■ Sample Quotes (Open-Ended Responses):")
        print("   (These are the storytelling goldmines!)")
        print()
        
        # Q17 Advice to leaders
        if 'Q17_Advice_BC_Leaders_text_OE' in df.columns:
            q17_responses = df['Q17_Advice_BC_Leaders_text_OE'].dropna()
            print("   ■ Advice to BC Leaders (Q17):")
            for i, response in enumerate(q17_responses.head(3)):
                if len(response.strip()) > 10:
                    preview = response[:80] + "..." if len(response) > 80 else response
                    print(f"      {i+1}. \"{preview}\"")
            print(f"      ... and {len(q17_responses)-3:,} more responses!")
            print()
        
        # Sentiment patterns
        print("■ Sentiment Patterns:")
        sample_sentiment_col = [col for col in sentiment_columns if 'Q17' in col]
        if sample_sentiment_col:
            col = sample_sentiment_col[0]
            sentiment_scores = pd.to_numeric(df[col], errors='coerce').dropna()
            avg_sentiment = sentiment_scores.mean()
            print(f"   • Average sentiment (Q17): {avg_sentiment:.2f} (0=negative, 1=positive)")
            
            # Find extreme sentiments
            very_negative = sentiment_scores[sentiment_scores < 0.1]
            very_positive = sentiment_scores[sentiment_scores > 0.9]
            print(f"   • Very negative responses (<0.1): {len(very_negative)}")
            print(f"   • Very positive responses (>0.9): {len(very_positive)}")
        print()
        
        # Next steps guidance
        print("■ Ready to Dive Deeper?")
        print()
        print("   ■ Hot Tips for Exploration:")
        print("   1. Focus on open-ended columns (*_OE) for authentic quotes")
        print("   2. Cross-reference sentiment with demographics")
        print("   3. Look for patterns in AI experience vs attitudes")
        print("   4. Hunt for geographic differences (Vancouver vs rural)")
        print("   5. Find the extreme voices (99%+ positive/negative sentiment)")
        print()
        
        print("   ■ Suggested Next Steps:")
        print("   • Load data: df = pd.read_csv('Hackathon round 3 with demos[48].csv')")
        print("   • Explore quotes: df['Q17_Advice_BC_Leaders_text_OE'].dropna()")
        print("   • Check sentiment: df['Q17_Advice_BC_Leaders_text_OE_sentiment_percentage']")
        print("   • Filter by demographics: df[df['AgeRollup_Broad'] == '18-34']")
        print("   • Find patterns: df.groupby('Q1_Experience_with_AI')['sentiment_col'].mean()")
        print()
        
        print("■ Happy Data Storytelling!")
        print("   Remember: Every row is a real British Columbian's voice.")
        print("   Your job is to help those voices be heard!")
        
    except Exception as e:
        print(f"■ Error loading data: {e}")
        print("Make sure pandas is installed: pip install pandas")

if __name__ == "__main__":
    explore_bc_ai_survey()