# ■ Vancouver AI Hackathon Round 3: BC AI Survey Data

Survey data from 1,001 British Columbians on artificial intelligence.

## What's In The Box

### The Dataset 
- 1,001 complete responses from across British Columbia
- 17 core questions covering AI experience, attitudes, and concerns
- Rich demographics: Age, location, education, income, family status
- 5,000+ text responses with sentiment analysis
- Geographic spread: Vancouver (76.6%), Victoria (13.7%), rural BC (9.7%)

### Question Categories
- AI Experience: Usage levels, comfort, learning
- Job Impact: Economic fears, opportunities, displacement
- Creative Impact: Authenticity, artistic value, human expression  
- Sector Applications: Healthcare, education, government, environment
- Governance: Regulation, trust, democratic participation
- Future Vision: Hopes, concerns, advice for leaders

## Quick Start Guide

### 1. Explore the Data

```bash
# Clone this repository
git clone https://github.com/WalksWithASwagger/vanai-hackathon-003.git
cd vanai-hackathon-003

# Open the main dataset
open "Hackathon round 3 with demos[48].csv"
```

### 2. Key Data Files
- `Hackathon round 3 with demos[48].csv` - Main survey dataset (1,001 responses)
- `BC_AI_Survey_Updated[5].docx` - Survey methodology and question details

### 3. Data Structure At-A-Glance
```
Row = One person's complete survey response
Columns = 100+ fields including:
├── Demographics (Age, Location, Education, Income)
├── AI Experience (Q1_Experience_with_AI)
├── Sentiment (Q3_AI_affecting_society_feeling) 
├── Job Impact (Q9_Jobs_in_BC_AI_Influence)
├── Open Responses (*_OE columns)
└── Sentiment Scores (*_sentiment_percentage)
```

## Technical Quick Start

### Python
```python
import pandas as pd

# Load the data
df = pd.read_csv('Hackathon round 3 with demos[48].csv')

# Quick exploration
print(f"Total responses: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Find open-ended responses
oe_columns = [col for col in df.columns if '_OE' in col]
print(f"Open-ended questions: {len(oe_columns)}")

# Look at sentiment distribution
sentiment_cols = [col for col in df.columns if 'sentiment' in col and 'percentage' in col]
for col in sentiment_cols[:3]:
    print(f"\n{col}:")
    print(df[col].describe())
```

### R
```r
library(tidyverse)

# Load data
bc_survey <- read_csv("Hackathon round 3 with demos[48].csv")

# Quick look
glimpse(bc_survey)

# Find text responses
text_cols <- bc_survey %>% 
  select(ends_with("_OE")) %>% 
  names()

# Sentiment analysis
sentiment_cols <- bc_survey %>% 
  select(contains("sentiment_percentage")) %>% 
  names()
```

## File Structure

```
vanai-hackathon-003/
├── README.md                              # This guide
├── LICENSE                                # Open source license
├── Hackathon round 3 with demos[48].csv   # Main dataset (1,001 responses)
├── BC_AI_Survey_Updated[5].docx           # Survey methodology
└── .gitignore                             # Keeps personal work private
```

## License & Usage

This dataset is provided for hackathon use. Please respect participant privacy and use data responsibly.