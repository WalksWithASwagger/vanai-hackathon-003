# ■ Getting Started with BC AI Survey Data

Quick guide to exploring the dataset.

## Quick Look

```bash
# Open the main dataset in your favorite tool
open "Hackathon round 3 with demos[48].csv"
# or
python explore-data-starter.py
```

## Technical Quick Start

### Python + Pandas
```python
import pandas as pd

# Load the data
df = pd.read_csv('Hackathon round 3 with demos[48].csv')

# Quick exploration
print(f"{len(df)} responses, {len(df.columns)} columns")

# Find open-ended responses
quote_columns = [col for col in df.columns if '_OE' in col and 'sentiment' not in col]
print(f"{len(quote_columns)} open-ended question types")

# Look at advice to leaders
advice = df['Q17_Advice_BC_Leaders_text_OE'].dropna()
print(f"{len(advice)} pieces of advice to BC leaders")

# Sample quotes
for quote in advice.head(3):
    print(f"   \"{quote[:100]}...\"")
```

### R + Tidyverse
```r
library(tidyverse)

# Load data
bc_survey <- read_csv("Hackathon round 3 with demos[48].csv")

# Quick overview
glimpse(bc_survey)

# Find text responses
text_columns <- bc_survey %>% 
  select(ends_with("_OE")) %>% 
  names()

# Look at advice responses
advice <- bc_survey %>% 
  select(Q17_Advice_BC_Leaders_text_OE) %>% 
  filter(!is.na(Q17_Advice_BC_Leaders_text_OE))

print(paste(nrow(advice), "advice responses"))
```

### Excel/Google Sheets
1. Open `Hackathon round 3 with demos[48].csv`
2. Use filters to explore:
   - Column `AgeRollup_Broad` for age groups
   - Column `Q1_Location_in_BC` for geography
   - Any column ending in `_OE` for quotes
3. Sort by sentiment columns to find extreme responses
4. Create pivot tables to find patterns