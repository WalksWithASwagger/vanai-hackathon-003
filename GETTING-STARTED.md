# 🎯 Getting Started with BC AI Survey Data

Welcome, data storytellers! This guide will get you exploring the dataset in under 5 minutes.

## 🚀 **Fastest Path to Insights**

### **Step 1: Quick Look**
```bash
# Open the main dataset in your favorite tool
open "Hackathon round 3 with demos[48].csv"
# or
python explore-data-starter.py
```

### **Step 2: Find Your Angle**
Pick one of these starting points based on your interests:

#### 🎭 **"I want to understand different types of people"**
Look for patterns in:
- `Q1_Experience_with_AI` (novice vs expert perspectives)
- `AgeRollup_Broad` (generational differences)
- `Q1_Location_in_BC` (urban vs rural attitudes)

#### 💬 **"I want to find great quotes and stories"**
Dive into these columns:
- `Q17_Advice_BC_Leaders_text_OE` (1,000+ pieces of citizen advice)
- `Q13_Worried_about_AI_impact_OE` (fears and concerns)
- `Q5_Creative_fields_vibe_OE` (attitudes toward AI in arts)

#### 📊 **"I want to analyze sentiment and emotions"**
Explore these patterns:
- `*_sentiment_percentage` columns (0-1 scale, 0=negative, 1=positive)
- Cross-reference high/low sentiment with demographics
- Find the 99%+ positive and negative responses

#### 🗺️ **"I want to explore geographic patterns"**
Compare responses across:
- Vancouver vs Victoria vs rural BC
- Different age groups in different locations
- Urban nuance vs rural binary positions

---

## 💡 **Data Storytelling Inspiration**

### **Real Quotes to Get You Started**
> *"People need to survive"* - Economic anxiety theme

> *"AI cannot make art without stealing content from others"* - Creative protection theme

> *"Listen to the people. It's not totally their decision to make."* - Democratic participation theme

### **Surprising Patterns**
- **Age Reversal**: 18-34 year-olds are most negative about AI (not what you'd expect!)
- **Healthcare Hope**: The one area where optimism dominates across all groups
- **Chameleon Province**: "Always adapting" was the most popular AI animal comparison

### **Quick Win Ideas**
1. **Persona Cards**: Create character profiles for different response types
2. **Quote Walls**: Beautiful visualizations of citizen voices
3. **Sentiment Journey**: Show how attitudes change with AI experience
4. **Geographic Story Map**: BC's emotional landscape around AI
5. **Contradiction Engine**: Highlight internal tensions in responses

---

## 🛠️ **Technical Quick Start**

### **Python + Pandas (Recommended)**
```python
import pandas as pd

# Load the data
df = pd.read_csv('Hackathon round 3 with demos[48].csv')

# Quick exploration
print(f"📊 {len(df)} responses, {len(df.columns)} columns")

# Find the storytelling gold (open-ended responses)
quote_columns = [col for col in df.columns if '_OE' in col and 'sentiment' not in col]
print(f"💬 {len(quote_columns)} open-ended question types")

# Look at advice to leaders
advice = df['Q17_Advice_BC_Leaders_text_OE'].dropna()
print(f"📝 {len(advice)} pieces of advice to BC leaders")

# Sample quotes
for quote in advice.head(3):
    print(f"   \"{quote[:100]}...\"")
```

### **R + Tidyverse**
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

### **Excel/Google Sheets (No Code Needed!)**
1. Open `Hackathon round 3 with demos[48].csv`
2. Use filters to explore:
   - Column `AgeRollup_Broad` for age groups
   - Column `Q1_Location_in_BC` for geography
   - Any column ending in `_OE` for quotes
3. Sort by sentiment columns to find extreme responses
4. Create pivot tables to find patterns

---

## 🎯 **Finding Your Story**

### **Start With Questions Like:**
- "What do different generations think about AI?"
- "How do Vancouver residents differ from rural BC?"
- "What are people most worried about?"
- "Where do we see the most optimism?"
- "What contradictions exist in public opinion?"

### **Then Ask:**
- "What does this mean for BC's future?"
- "How should leaders respond to these insights?"
- "What policies would address these concerns?"
- "How can we build on the optimism while addressing the fears?"

---

## 🏆 **Success Metrics**

Great hackathon projects often have:
- ✅ **Clear insights** that surprise or enlighten
- ✅ **Human connection** - real quotes from real people
- ✅ **Visual appeal** - beautiful, engaging presentation
- ✅ **Actionable outcomes** - clear implications for policy/business
- ✅ **Technical innovation** - creative use of tools and methods

---

## 🤝 **Need Help?**

### **Stuck on Data?**
- Run `python explore-data-starter.py` for a guided tour
- Check the main README.md for detailed column explanations
- Ask mentors about specific patterns or correlations

### **Stuck on Ideas?**
- Look at the "Hidden Gems" section in README.md
- Browse the open-ended responses for inspiration
- Think about what would help BC leaders make better AI decisions

### **Stuck on Technical?**
- Start simple - even Excel can create powerful insights
- Focus on one demographic slice at a time
- Remember: Good storytelling beats complex analysis

---

**Ready to transform 1,001 voices into stories that matter? Let's go! 🚀**