# Parkinson-Progression-Prediction
Modeling Parkinson Disease Progression using PPMI dataset (https://www.ppmi-info.org/access-data-specimens/download-data/)


## Data Exploration
The UPDRS scale refers to Unified Parkinson Disease Rating Scale, 
and it is a rating tool used to gauge the course of Parkinson’s 
disease in patients. It has four parts, and each part has multiple
points that are individually scored. Please refer to the following
table for details.  


| Part 1: Intellectual function, mood, behavior | Available in current dataset | Part 2: Activities of daily living | Available in current dataset | Part 3:Motor examination | Available in current dataset |  Part 4:Motor complications | Available in current dataset |
| --- | --- | --- |--- |--- |--- |--- |--- |
| Forgetfulness, disorientation in time and space |  | Speech: difficulty being understood  | 23 | Speech – volume, diction | 24 | Dyskinesia, including time spent with dyskinesia, functional impact of dyskinesia, and painful off-state dystonia | 25|
| Vivid dreaming | Yes | Salivation and drooling  | 23 | Reduced facial expressions | 24|  Motor fluctuations, including time spent in the off state, functional impact of fluctuations, and complexity of motor fluctuations |
| Hallucinations  | Yes | Chewing and swallowing  | 23 | Rigidity | | | | 
| Delusions and paranoia  | 512 | Cutting food | 23 | Finger tapping | | | |
| Depressed mood | Yes | Small handwriting | 23 | Slowed hand movements | | | |
| Anxious mood  | Yes | Needing help with getting dressed, buttons, arms in sleeves  | 23 | Rapid alternating movements of hands (pronation-supination) | | | |
| Apathy | Yes | Requires assistance with bathing, brushing teeth  | 23 | Toe tapping | | | |
| Features of dopamine dysregulation syndrome | Yes | Trouble doing hobbies and other activities  | 23 | Leg agility – when tapping heel on the ground, is it slowed, early fatiguing | | | |
| Nighttime sleep problems |  | Difficulties with turning in bed | 23 | Arising from a chair – degree of difficulty | | | |
| Daytime sleepiness |  | Tremor impact on activities | 23 | Gait – shuffling, walking with difficulty | | | |
| Pain and other sensations  |  | Getting in and out of bed  | 23 | Freezing of gait | | | |
| Urinary problems | Yes | Walking, balance, falling | 23 | Postural stability – difficulty recovering balance | | | |
| Constipation problems |  | Freezing | 23 | Posture – stooped | | | |
| Lightheadedness on standing |  |  | 23 | Global spontaneity of movement (body bradykinesia) – slowness of movement, lack of movement | | | |
| Fatigue |  |  | 23 | Tremor at rest | | | |


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
