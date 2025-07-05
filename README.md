# 🚀 Vancouver AI Hackathon Round 3: BC AI Survey Data Storytelling

> **Transform 1,001 British Columbian voices into compelling data stories**

Welcome to the ultimate data storytelling challenge! This repository contains rich survey data from 1,001 British Columbians sharing their hopes, fears, and perspectives on artificial intelligence.

## 🎯 **The Challenge**

How can we transform raw survey data into engaging, insightful narratives that help BC leaders, businesses, and communities understand public sentiment about AI?

**Your mission**: Create innovative data storytelling experiences that reveal the human stories hidden in the numbers.

---

## 📊 **What's In The Box**

### **The Dataset** 
- **1,001 complete responses** from across British Columbia
- **17 core questions** covering AI experience, attitudes, and concerns
- **Rich demographics**: Age, location, education, income, family status
- **5,000+ text responses** with sentiment analysis
- **Geographic spread**: Vancouver (76.6%), Victoria (13.7%), rural BC (9.7%)

### **Question Categories**
- 🤖 **AI Experience**: Usage levels, comfort, learning
- 💼 **Job Impact**: Economic fears, opportunities, displacement
- 🎨 **Creative Impact**: Authenticity, artistic value, human expression  
- 🏥 **Sector Applications**: Healthcare, education, government, environment
- 🏛️ **Governance**: Regulation, trust, democratic participation
- 🌱 **Future Vision**: Hopes, concerns, advice for leaders

---

## 🚀 **Quick Start Guide**

### **1. Explore the Data** (Start Here!)

```bash
# Clone this repository
git clone https://github.com/WalksWithASwagger/vanai-hackathon-003.git
cd vanai-hackathon-003

# Open the main dataset
open "Hackathon round 3 with demos[48].csv"
```

### **2. Key Data Files**
- **`Hackathon round 3 with demos[48].csv`** - Main survey dataset (1,001 responses)
- **`BC_AI_Survey_Updated[5].docx`** - Survey methodology and question details

### **3. Data Structure At-A-Glance**
```
Row = One person's complete survey response
Columns = 100+ fields including:
├── Demographics (Age, Location, Education, Income)
├── AI Experience (Q1_Experience_with_AI)
├── Sentiment (Q3_AI_affecting_society_feeling) 
├── Job Impact (Q9_Jobs_in_BC_AI_Influence)
├── Open Responses (*_OE columns - the gold mine!)
└── Sentiment Scores (*_sentiment_percentage)
```

---

## 💡 **Data Storytelling Ideas**

### **🎭 Persona Development**
Turn response patterns into relatable characters:
- The "Healthcare Optimist" (sees AI as medical breakthrough)
- The "Job Protector" (fears economic displacement)
- The "Creative Defender" (protects human authenticity)
- The "Democratic Skeptic" (distrusts institutions)

### **🗺️ Geographic Stories**
- **Vancouver vs Rural BC**: Urban nuance vs binary positions
- **Island Differences**: Victoria government workers vs mainland perspectives
- **Northern Voices**: How do smaller communities view AI differently?

### **📈 Sentiment Journeys**
- **Age Reversal**: Why are 18-34 year-olds most negative about AI?
- **Experience Paradox**: Do people who use AI trust it more or less?
- **Healthcare Hope**: The one area where optimism dominates

### **🎨 Creative Formats**
- **Interactive personas** you can "talk" to
- **Sentiment heat maps** across demographics
- **Quote collections** that capture authentic voices
- **Contradiction engines** showing internal tensions
- **Policy poetry** turning advice into art

---

## 🔍 **Data Exploration Tips**

### **Find The Human Stories**
```
Look for columns ending in "_OE" (Open Ended)
These contain actual quotes like:
• "People need to survive" 
• "AI cannot make art without stealing"
• "Listen to the people"
```

### **Sentiment Gold Mines**
```
High sentiment scores (>0.9) reveal passionate voices:
• Q17_Advice_BC_Leaders_text_OE_sentiment_percentage
• Q13_Worried_about_AI_impact_OE_sentiment_percentage
• Q5_Creative_fields_vibe_OE_sentiment_percentage
```

### **Demographic Patterns**
```
Cross-reference responses with:
• AgeRollup_Broad (18-34, 35-54, 55 Plus)
• Q1_Location_in_BC (geographic insights)
• Q1_Experience_with_AI (usage vs sentiment)
```

---

## 🛠️ **Technical Quick Start**

### **For Python Explorers**
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

### **For R Enthusiasts**
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

---

## 🎪 **Hackathon Success Tips**

### **🔥 What Judges Love**
- **Human Connection**: Make data feel personal and relatable
- **Visual Innovation**: Fresh approaches to data visualization  
- **Actionable Insights**: Clear implications for policy/business
- **Technical Creativity**: Novel use of tools and techniques
- **Storytelling**: Compelling narratives that stick with people

### **💎 Hidden Gems To Explore**
- **Q2 Animal Comparisons**: "Chameleon" was most popular - why?
- **Q17 Advice Responses**: 1,000+ raw pieces of citizen advice
- **Extreme Sentiments**: Find the 99%+ positive/negative responses
- **Geographic Patterns**: Rural vs urban AI attitudes
- **Job Displacement Data**: 54.1% expect more jobs lost than created

### **⚡ Quick Win Strategies**
1. **Quote Collections**: Curate powerful representative quotes
2. **Persona Cards**: Create "trading cards" for different BC voices  
3. **Sentiment Maps**: Visualize emotional geography of BC
4. **Contradiction Engines**: Show internal tensions in responses
5. **Policy Poetry**: Transform citizen advice into compelling formats

---

## 🏆 **Previous Success Stories**

Looking for inspiration? Check out how others have transformed survey data:
- **Interactive persona experiences** where you "meet" different respondent types
- **Sentiment journey maps** showing how attitudes evolve
- **Geographic storytelling** revealing regional AI perspectives
- **Quote visualization** making individual voices heard
- **Policy recommendation engines** based on citizen input

---

## 🤝 **Getting Help**

### **Stuck? Try This:**
1. **Start simple**: Pick one question, explore one demographic slice
2. **Find patterns**: Look for age/location/experience correlations  
3. **Hunt for quotes**: The open-ended responses are storytelling gold
4. **Think personas**: Group similar responses into character types
5. **Ask "So what?"**: What do these patterns mean for BC's future?

### **Community Resources**
- **Hackathon Discord**: Connect with other teams
- **Data Questions**: Ask mentors about specific columns or patterns
- **Technical Support**: Get help with tools and analysis
- **Presentation Tips**: Guidance on storytelling and demo formats

---

## 📋 **File Structure**

```
vanai-hackathon-003/
├── README.md                              # This guide
├── LICENSE                                # Open source license
├── Hackathon round 3 with demos[48].csv   # Main dataset (1,001 responses)
├── BC_AI_Survey_Updated[5].docx           # Survey methodology
└── .gitignore                             # Keeps personal work private
```

---

## 🌟 **Ready to Start?**

1. **🔍 Explore**: Open the CSV, browse the columns, get familiar
2. **🎯 Focus**: Pick one angle that excites you (personas, geography, sentiment)
3. **📊 Analyze**: Find patterns, correlations, surprising insights
4. **🎨 Create**: Build something that makes the data come alive
5. **📢 Share**: Present a story that helps people understand BC's AI future

---

## 📄 **License & Usage**

This dataset is provided for hackathon use. Please respect participant privacy and use data responsibly for insights and storytelling that benefit BC communities.

---

**Let's transform 1,001 voices into stories that matter! 🚀**

*Questions? Stuck? Need inspiration? Reach out to mentors or check the hackathon Discord.*