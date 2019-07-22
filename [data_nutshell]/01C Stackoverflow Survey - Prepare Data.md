# 01C Stackoverflow Survey - Prepare Data

_*Series Content List*_
1. Business Understanding
2. Data Understanding
3. **Prepare Data**
4. Data Modeling
5. Evaluate the Results
6. Deploy

---

_*Index*_

[TOC]

---

## / featrue selection
There are 80+ features in the 2019's data. According to last post, I decide only take 35 of them, code is like this:

```python
select_list_updated = ['MainBranch','OpenSourcer','OpenSource','Employment','Age','Student','EdLevel','UndergradMajor','EduOther',
              'OrgSize','DevType','YearsCode','CareerSat','JobSeek','JobFactors','ConvertedComp','WorkWeekHrs','WorkChallenge','ImpSyn',
              'LanguageWorkedWith','LanguageDesireNextYear','DatabaseWorkedWith','DatabaseDesireNextYear','DevEnviron','OpSys','BetterLife',
              'SOVisitFreq','SOVisitTo','SOFindAnswer','SOTimeSaved','SOPartFreq','SOJobs','EntTeams','SOComm','WelcomeChange']
df = df2019d[select_list_updated]
```

## / persistence
The survey data is around 100MB, for github have limit, so I get a bit work on how to persistence about the data files. I tried csv-gzip, pickle, pickle-gzip, pickle-xz. And found the result:
- for file more than 100m, need zip for git upload
- csv_gzip take good compression (18M)
- pickle get more efficiency (Read is much faster than csv, for pickle save more info than csv, read is many time faster)
- use gzip(quick) or xz(max comp) to store file
- finally, I store 35 feature pickle xz file only for 2.7MB, and read three time fast than csv (drawback is it thake longest time to write)

```python
df.to_pickle('2019_35featrue.pickle.xz', compression='xz')

dfcheck = pd.read_pickle('2019_35featrue.pickle.xz', compression='xz')
dfcheck.head(3)
```