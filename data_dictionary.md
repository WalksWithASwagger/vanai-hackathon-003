# BC AI Survey Data Dictionary

## Overview
**File**: `Hackathon round 3 with demos[48].csv`  
**Total Records**: 1,231 (including header)  
**Total Columns**: 121  
**Purpose**: Survey dataset capturing British Columbia residents' perceptions, experiences, and attitudes toward AI technology

---

## Column Definitions

### Survey Metadata (Columns 1-10)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `S. No` | Integer | Sequential participant number | 1, 2, 3... |
| `participant_id` | String | Unique participant identifier (UUID format) | "9f8e7d6c-5b4a-3c2d..." |
| `distribution_type` | String | Method of survey distribution | "Link" |
| `distribution_name` | String | Source of survey distribution | "ARF" |
| `engagement_id` | String | Unique engagement session identifier | UUID format |
| `engagement_started_EDT` | DateTime | Timestamp when survey started (EDT) | "2024-01-15 10:30:00" |
| `engagement_completed_EDT` | DateTime | Timestamp when survey completed (EDT) | "2024-01-15 10:45:00" |
| `engagement_participation_status` | String | Survey completion status | "Completed" |
| `BrokerPanelId` | String | Panel provider identifier | Alphanumeric code |
| `Overquota_redirect_ARF_return_token` | String | Redirect token for overquota participants | Usually empty |

### Location & Screening (Columns 11-12)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Q1_Location_in_BC` | String | Participant's region within BC | "Vancouver / Lower Mainland", "Prince George", "Kelowna", "Victoria" |
| `DQ_redirect_not_in_BC_return_token` | String | Disqualification token for non-BC residents | Usually empty |

### AI Experience (Columns 13-17)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Q1_Experience_with_AI` | String | Level of AI usage experience | "No experience", "Aware but not a user", "Occasional user", "Regular user" |
| `Q2_Experience_with_AI_animal` | String | Animal metaphor for AI experience | "Chameleon", "Owl", "Tiger", "Snail", "Other" |
| `Q2_Experience_with_AI_animal_other_OE` | String | Custom animal description if "Other" selected | Open text |
| `Q2_Experience_with_AI_animal_other_OE_sentiment` | String | Sentiment analysis of custom animal response | "POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED" |
| `Q2_Experience_with_AI_animal_other_OE_sentiment_percentage` | Float | Confidence score for sentiment analysis | 0.0 to 1.0 |

### AI Impact Perceptions (Columns 18-38)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Q3_AI_affecting_society_feeling` | String | Overall sentiment about AI's societal impact | "Mostly optimistic", "Mostly concerned", "Mixed feelings/neutral", "Not sure" |
| `Q4A_Sector_AI_making_a_positive_impact_1` through `_7` | String | Sectors where AI has positive impact (ranked choices) | "Healthcare and medicine", "Environment and climate", "Arts, culture, and media", "Jobs and the economy", "Government and public services", "None of the above" |
| `Q4B_Sector_AI_making_a_negative_impact_1` through `_7` | String | Sectors where AI has negative impact (ranked choices) | Same options as Q4A |

### Creative & Environmental Views (Columns 39-51)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Q5_Art_vibe_AI` | String | Artistic metaphor for AI perception | "Abstract installation", "Sci-fi epic", "Pop hit", "Classical symphony", "Documentary film" |
| `Q6_AI_role_in_creative_fields_in_BC` | String | Impact of AI on creative industries | "Mostly enhance creativity", "Mostly harm creativity", "Mixed effects", "Little impact", "Not sure" |
| `Q7_AI_and_environment` | String | AI's potential environmental impact | "Very helpful", "Helpful, if used responsibly", "Could be harmful", "Not much impact" |
| `Q7_AI_and_environment_OE` | String | Open-ended environmental impact explanation | Free text |
| `Q7_AI_and_environment_OE_sentiment` | String | Sentiment analysis of environmental response | "POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED" |
| `Q7_AI_and_environment_OE_sentiment_percentage` | Float | Confidence score for sentiment | 0.0 to 1.0 |

### Community Impact & Jobs (Columns 45-56)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Q8_AI_helping_BC_community` | String | Response format choice | "I'll type my answer 📲", "I'll record a video 🤳" |
| `Q8_AI_helping_BC_community_text_OE` | String | Text response about AI helping community | Free text |
| `Q8_AI_helping_BC_community_text_OE_sentiment` | String | Sentiment of community help response | "POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED" |
| `Q8_AI_helping_BC_community_video_OE` | String | Video response identifier | Video file reference |
| `Q9_Jobs_in_BC_AI_Influence` | String | AI's impact on employment | "It'll create more jobs than it takes away", "It'll eliminate more jobs than it creates", "It'll mostly change jobs, not eliminate them", "Not much impact" |
| `Q10_AI_superpower_to_help_community` | String | Desired AI capability for community benefit | "Making public services smarter", "Supporting elders and caregivers", "Solving tough local problems", "Fighting climate change", "Connecting communities together" |

### Trust & Governance (Columns 57-107)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Q11_Gainer_advances_in_AI_1` through `_6` | String | Who benefits from AI advances (ranked) | "Large corporations", "Small businesses", "The general public", "Government and public institutions", "Educational institutions", "None" |
| `Q12_Most_trustworthy_advances_in_AI_1` through `_7` | String | Most trusted entities for AI development (ranked) | Same options as Q11 plus additional choices |
| `Q13_AI_impact_worries` | String | Response format for concerns | "I'll type my answer 📲", "I'll record a video 🤳" |
| `Q13_AI_impact_worries_text_OE` | String | Text response about AI concerns | Free text |
| `Q14_Govt_role_in_managing_AI` | String | Preferred government approach to AI | "Balanced approach", "Strong regulation", "Hands-off promotion", "No special action" |
| `Q15_Matters_most_BC_AI_future_1` through `_7` | String | Priority areas for BC's AI future (ranked) | "Ethical and unbiased AI", "Privacy and data protection", "Economic growth and innovation", "Job training and education", "Healthcare improvements", "Environmental sustainability", "Digital equity" |
| `Q16_Indigenous_communities_involvement_AI` | String | Views on Indigenous involvement in AI | Free text response |
| `Q16_Indigenous_communities_involvement_AI_sentiment` | String | Sentiment of Indigenous involvement response | "POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED" |
| `Q17_Advice_BC_Leaders` | String | Advice for BC leaders on AI | Free text response |
| `Q17_Advice_BC_Leaders_sentiment` | String | Sentiment of leadership advice | "POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED" |

### Demographics (Columns 109-121)

| Column Name | Data Type | Description | Example Values |
|------------|-----------|-------------|----------------|
| `Age` | Integer | Participant age in years | 18-99 |
| `AgeRollup_Broad` | String | Age category grouping | "18-34", "35-54", "55 Plus" |
| `Gender` | String | Participant gender | "Male", "Female" |
| `Year of Birth` | Integer | Birth year | 1925-2006 |
| `Education` | String | Highest education level | "University undergraduate degree", "College/technical diploma", "High school graduate", "Graduate/professional degree" |
| `HH_Income_Fine_23` | String | Household income range | "Less than $25,000", "$25,000-$49,999", "$50,000-$74,999", "$75,000-$99,999", "$100,000-$149,999", "$150,000+" |
| `FirstNation_23` | String | First Nations status | "Yes", "No" |
| `Ethnicity_Roll_23` | String | Ethnic background | "White", "Chinese", "South Asian", "Indigenous", "Filipino", "Other" |
| `Vizmin_23` | String | Visible minority status | "Visible minority", "Not a visible minority" |
| `HH_Comp_23` | String | Household composition | Various household types |
| `KidsinHH_23` | String | Children in household | Number or "None" |
| `HH_Under18_23` | String | Presence of minors | "Yes", "No, no one under 18 here" |
| `Urban/ Rural` | String | Location type | "Urban", "Rural" |

---

## Data Notes

1. **Sentiment Analysis**: Many open-ended questions include automated sentiment analysis with:
   - Classification: POSITIVE, NEGATIVE, NEUTRAL, or MIXED
   - Confidence score: 0.0 to 1.0

2. **Ranked Responses**: Questions marked with "_1" through "_7" represent ranked choices where participants ordered their preferences

3. **Response Formats**: Several questions allow participants to choose between text (📲) or video (🤳) responses

4. **Empty Columns**: Some columns between sections contain no headers or data

5. **Missing Data**: Empty cells may indicate:
   - Questions not applicable to participant
   - Participant chose not to answer
   - Technical issues during survey completion