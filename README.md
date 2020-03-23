# Parkinson-Progression-Prediction
Modeling Parkinson Disease Progression using PPMI dataset (https://www.ppmi-info.org/access-data-specimens/download-data/)


## Data Exploration
The UPDRS scale refers to Unified Parkinson Disease Rating Scale, 
and it is a rating tool used to gauge the course of Parkinson’s 
disease in patients. It has four parts, and each part has multiple
points that are individually scored. Please refer to the following
table for details.  

| Part 1: Intellectual function, mood, behavior | Availabel in current dataset | Part 2: Activities of daily living | Availabel in current dataset | Part 3:Motor examination | Availabel in current dataset |  Part 4:Motor complications | Availabel in current dataset |
| --- | --- | --- |--- |--- |--- |--- |--- |
| Forgetfulness, disorientation in time and space | hi | Speech: difficulty being understood  |
| Vivid dreaming | 586 | Salivation and drooling  |
| Hallucinations  | 564 | Chewing and swallowing  |
| Delusions and paranoia  | 512 | Cutting food |
| Depressed mood | 525 | Small handwriting |
| Anxious mood  | 852 | Needing help with getting dressed, buttons, arms in sleeves  |
| Apathy | 714 | Requires assistance with bathing, brushing teeth  |
| Features of dopamine dysregulation syndrome | 360 | Trouble doing hobbies and other activities  |
| Nighttime sleep problems | 714 | Difficulties with turning in bed |
| Daytime sleepiness | 714 | Tremor impact on activities |
| Pain and other sensations  | 714 | Getting in and out of bed  |
| Urinary problems | 714 | Walking, balance, falling |
| Constipation problems | 714 | Freezing |
| Lightheadedness on standing | 714 |  |
| Fatigue | 714 |  |


Totally 4784 samples, 1674 patients

| visit_times | samples_num | patients_num |
| --- | --- | --- |
| 1 | 671 | 671 |
| 2 | 586 | 293 |
| 3 | 564 | 188 |
| 4 | 512 | 128 |
| 5 | 525 | 105 |
| 6 | 852 | 142 |
| 7 | 714 | 102 |
| 8 | 360 | 45  |
| Totally  | 4784 | 1674 |
