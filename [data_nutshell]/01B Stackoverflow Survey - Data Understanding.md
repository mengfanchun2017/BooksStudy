# 01B Stackoverflow Survey - Data Understanding

> For my project engineer 

_*Series Content List*_
1. Business Understanding
2. **Data Understanding**
3. Prepare Data
4. Data Modeling
5. Evaluate the Results
6. Deploy

---

_*Index*_

[TOC]

---

## / data files
There are 9 years data total, with this 3 files with largest size and more detailed information:
- developer_survey_2019, 18.7MB
- developer_survey_2018, 20MB
- developer_survey_2017, 9.6MB

## / data selecting
There are serveral (>80) features in the 2019 data, after a day's compare I found that there only 17 columns are the same compare 2019 to 2018, and only 3 columns compare 2019 to 2017. So I will finish my work first on 2019's data.

So I take many time read the survey and check the data feature by featrue , and get featrues under blow for my analysis. I also post my feature check log at the bottom if you want to more information.  Features I select is 39, and I restructure it into 4 subdomain.

- Basic Information (9)
    1. MainBranch - [cat6] why are you learning coding?
    2. OpenSourcer - [cat4] how often do you contribute to open source?
    3. OpenSource - [cat3] how do you feel about the quality of open source software (OSS)
    4. Employment - [cat7] which of the following best describe your current employment status?
    5. Age
    6. Student - [cat4] are you a student, and which type of student?
    7. EdLevel - [cat9] highest level of formal education.
    8. UndergradMajor - [cat12] main of most important field of study?
    9. EduOther - [cat10_mul] which of the following types of non-degree education have you used or participated in?
- Your Education, Work, and Career (12)
    1. OrgSize - [cat10] how many people are employed at your company
    2. DevType - [catn] which role do you play at work?
    3. YearsCode - [cat_int] how manyyear have you been coding?
    4. CareerSat - [cat5] overall, how satistied are you with your career thus far?
    5. JobSeek - [cat3] which of the following best describes your current job-seeking status?
    6. JobFactors - [cat10_mul] with same job income, of the following factors, which are most important to you?
    7. ConvertedComp - [cat_int], salary converted to annual USD, need to alter to 10 or less buckets.
    8. WorkWeekHrs - [cat_int], need to alter to 10 or less buckets.
    9. WorkPlan - [cat3], how structured or planned is your work?
    10. WorkChallenge - [cat9_mul], what are your greatest challenges to productivity as a developer? select up to 3
    11. WorkRemote - [cat7], how often do you work remotely?
    12. ImpSyn - [cat5], how do you rate your own level of competence?
- Technology and Tech Culture (7)
    1. LanguageWorkedWith - [catn_mul], which language do you use (maybe use isin for a filter solve)
    2. LanguageDesireNextYear - [catn_mul], which language do you want to learn next year?
    3. DatabaseWorkedWith - [catn_mul]
    4. DatabaseDesireNextYear - [catn_mul]
    5. DevEnviron - [cat_mul], which develop envirment do you use primary.
    6. OpSys - [cat4] what is the primary operating system in which you work?
    7. BetterLife - [cat2] do you think people born today will have a better life than their parents?
- Stack Overflow Usage + Community (11)
    1. SOVisitFreq - [cat6]
    2. SOVisitTo - [cat6_mul] recommend
    3. SOFindAnswer - [cat5]same with SOVisitFreq
    4. SOTimeSaved - [cat5] as well as the last time you solved a problem using SO, compare with other resource, which was faster?
    5. SOHowMuchTime - [cat4] how much time do you saved
    6. SOPartFreq - [cat6] how frequently would you participate in Q&A?
    7. SOJobs - [cat3] have you ever used or visited SO Jobs?
    8. EntTeams - [cat3] have you ever used SO Enterprise or Teams?
    9. SOComm - [cat6] do you consider yourself a member of the SOCommunity?
    10. WelcomeChange -[cat6] compared to last year, how welcome do you feel on SO?
    11. SONewContent - [cat5_mul] would you like to see any of the following on SO?

Also I am going to pass any feature that omit more than 20% (ConvertedComp, WorkChallenge, WorkWeekHrs, DatabaseDesireNextYear is important,keep) which are WorkRemote, WorkPlan, SOHowMuchTime, SONewContent

```python
# check null value
## 0.2 count
round(df.shape[0] * 0.2)
>>> 17777
```

Note, for the sake of compress csv file, I use gzip. [/Resource/](https://stackoverflow.com/questions/37193157/apply-gzip-compression-to-a-csv-in-python-pandas)

```python
import pandas as pd
# Write a pandas dataframe to disc as gunzip compressed csv
df.to_csv('dfsavename.csv.gz', compression='gzip')

#Read from disc
df = pd.read_csv('dfsavename.csv.gz', compression='gzip')
```

## / data structure
According 2019's survey, I got match with 6 domain question with 85 columns. It is interesting that columns get less every year (2017-154, 2018-129)

1. Basic Information
    1. ~~Respondent~~ - ID
    2. MainBranch - [cat6] why are you learning coding?
    3. ~~Hobbyist~~ - [catb] code for hobby or not (contained in Main Branch)
    4. OpenSourcer - [cat4] how often do you contribute to open source?
    5. OpenSource - [cat3] how do you feel about the quality of open source software (OSS)
    6. Employment - [cat7] which of the following best describe your current employment status?
    7. Location - [catn] which country?
2. Your Education, Work, and Career
    1. Student - [cat4] are you a student, and which type of student?
    2. EdLevel - [cat9] highest level of formal education.
    3. UndergradMajor - [cat12] main of most important field of study?
    4. EduOther - [cat10_mul] which of the following types of non-degree education have you used or participated in?
    5. ~~Industory~~ - missing in schema
    6. OrgSize - [cat10] how many people are employed at your company
    7. DevType - [cat_many] which role do you play at work?
    8. YearsCode - [cat_int] how manyyear have you been coding?
    9. ~~Year1stCode~~ - [cat_int] at what age did you write your fist line code (droped for not so clear standard html vs c, not at the same level)
    10. CareerSat - [cat5] overall, how satistied are you with your career thus far?
    11. ~~JobSat~~ - [cat5] overall, how satistied are you with your current job? (drop for very match CareerSat, can be tried on combine feature)
    12. ~~MgrIdiot~~ - [cat4] how confident are you that your manger knows what they are doing? (Nice title, drop for too subjective)
    13. ~~MgrMonwy~~ - [cat2] do you believe that you need to be a manager to make more money? (drop for less than half)
    14. ~~MgrWant~~ - [cat4] do you want to become a manager? (drop for one third want to)
    15. JobSeek - [cat3] which of the following best describes your current job-seeking status?
    16. LastHireDate - [cat5] when was the last time that you took a job with a new employer?
    17. LastInt - [cat6_mul] in your most recent successful job interview, you were asked to... (check all)?
    18. FizzBuzz - [cat2] have you been asked to solve FizzBuzz in an interview (basic coding)?
    19. JobFactors - [cat10_mul] with same job income, of the following factors, which are most important to you?
    20. ~~ResumeUpdate~~ - [cat6] what is the primary reason that you updated your resume last time? (drop)
    21. ~~CurrencySymbol~~ \ ~~CurrencyDesc~~ - same with country, dorp
    22. ~~CompTotal~~ use ConvertedComp($)
    23. ~~CompFreq~~ dorp
    24. ConvertedComp - [cat_int], need to alter to 10 or less buckets.
    25. WorkWeekHrs - [cat_int], need to alter to 10 or less buckets.
    26. WorkPlan - [cat3], how structured or planned is your work?
    27. WorkChallenge - [cat9_mul], what are your greatest challenges to productivity as a developer? select up to 3
    28. WorkRemote - [cat7], how often do you work remotely?
    29. ~~WorkLoc~~ - [cat3], where would you prefer to work? (drop, same as WorkRemote)
    30. ImpSyn - [cat5], how do you rate your own level of competence?
    31. CodeRev - [cat3], do you review code as part of your work?
    32. ~~CodeRevHrs~~ - [cat_int], how many hours per week do you spend on code review (lack for duration, seems weekly)
    33. UnitTests - [cat4_int], does your company regularly employ unit tests in the development of their products?
    34. PurchaseHow - [cat4], how does your company make decisions about purchasing new technology?
    35. ~~PurchaseWhat~~ - [cat3], (drop for subjective)
3. Technology and Tech Culture
    1. LanguageWorkedWith - [catn_mul], which language do you use (maybe use isin for a filter solve)
    2. LanguageDesireNextYear - [catn_mul], which language do you want to learn next year?
    3. DatabaseWorkedWith - [catn_mul]
    4. DatabaseDesireNextYear - [catn_mul]
    5. PlatformWorkedWith - [catn_mul]
    6. PlatformDesierNextyear - [catn_mul]
    7. WebFrameWorkedWith - [cat_mul]
    8. WebFrameDesireNextYear - [cat_mul]
    9. MiscTechWorkedWith - [cat_mul]
    10. MiscTechDesireNextYear - [cat_mul]
    11. DevEnviron - [cat_mul]
    12. OpSys - [cat4] what is the primary operating system in which you work?
    13. ~~Containers~~ - [cat5] how do you use containers? (drop for too early)
    14. ~~BlockchainOrg~~ - [cat6] drop for too early
    15. ~~Blockchainls~~ - [cat6] drop for too early
    16. BetterLife - [cat2] do you think people born today will have a better life than their parents?
    17. ~~ITperson~~ - [cat4] drop
    18. ~~OffOn~~ - don't get the meaning
    19. ~~SocialMedia~~ - [catn_mul]
4. Stack Overflow Usage + Community
    1. ~~SOVisit1st~~ - drop for so many I don't remember
    2. SOVisitFreq - [cat6]
    3. SOVisitTo - [cat6_mul] recommend
    4. SOFindAnswer - [cat5]same with SOVisitFreq
    5. SOTimeSaved - [cat5] as well as the last time you solved a problem using SO, compare with other resource, which was faster?
    6. SOHowMuchTime - [cat4] how much time do you saved
    7. ~~SOAccount~~ - [catb] do you have a SO account?
    8. SOPartFreq - [cat6] how frequently would you participate in Q&A?
    9. SOJobs - [cat3] have you ever used or visited SO Jobs?
    10. EntTeams - [cat3] have you ever used SO Enterprise or Teams?
    11. SOComm - [cat6] do you consider yourself a member of the SOCommunity?
    12. WelcomeChange -[cat6] compared to last year, how welcome do you feel on SO?
    13. SONewContent - [cat5_mul] would you like to see any of the following on SO?
5. Demographic Information
    1. Age
    2. ~~Gender~~ - [cat3_mul] a bit sensitive
    3. ~~Trans~~ - [cat2] a bit sensitive
    4. ~~Sexuality~~ - [cat4_mul] a bit sensitive
    5. ~~Ethnicity~~ - [catn_mul] a bit sensitive
    6. many of the question are not recorded in data, pass
6. Survey Review
    1. SurveyLength - [cat3] how do you feel about the length of the survey this year?
    2. SurveyEase - [cat3] how easy or difficult was this surey to complete?

## / my experience with stack overflow

As a data newbee, I found myself rely on stack overflow several times per day. If I put my question in English carefully, there is a great chance (>50%) that I will get some hint or coding from it. And mostly with detailed explanation.