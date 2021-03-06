# Parkinson-Progression-Prediction
Modeling Parkinson Disease Progression using PPMI dataset (https://www.ppmi-info.org/access-data-specimens/download-data/)


## Data Exploration
### 1. Feature Selection
We select features based on UPDRS criterion, which refers to Unified 
Parkinson Disease Rating Scale, 
and it is a rating tool used to gauge the course of Parkinson’s 
disease in patients. It has four parts, and each part has multiple
points that are individually scored. Please refer to the following
table for details.  


| Part 1: Intellectual function, mood, behavior | Available in current dataset | Part 2: Activities of daily living | Available in current dataset | Part 3:Motor examination | Available in current dataset |  Part 4:Motor complications | Available in current dataset |
| --- | --- | --- |--- |--- |--- |--- |--- |
| Forgetfulness, disorientation in time and space |  | <div style="width: 200pt"> Speech: difficulty being understood</div>  | Yes | Speech – volume, diction | Yes | Dyskinesia, including time spent with dyskinesia, functional impact of dyskinesia, and painful off-state dystonia | Yes|
| Vivid dreaming | Yes | Salivation and drooling  |  | Reduced facial expressions | Yes|  Motor fluctuations, including time spent in the off state, functional impact of fluctuations, and complexity of motor fluctuations | Yes |
| Hallucinations  | Yes | Chewing and swallowing  | Yes | Rigidity |Yes | | | 
| Delusions and paranoia  |  | Cutting food |  | Finger tapping |Yes | | |
| Depressed mood | Yes | Small handwriting | Yes | Slowed hand movements |Yes | | |
| Anxious mood  | Yes | Needing help with getting dressed, buttons, arms in sleeves  | Yes | Rapid alternating movements of hands (pronation-supination) | Yes | | |
| Apathy | Yes | Requires assistance with bathing, brushing teeth  |  | Toe tapping | Yes | | |
| Features of dopamine dysregulation syndrome | Yes | Trouble doing hobbies and other activities  | Yes | Leg agility – when tapping heel on the ground, is it slowed, early fatiguing | Yes | | |
| Nighttime sleep problems |  | Difficulties with turning in bed | Yes | Arising from a chair – degree of difficulty | Yes | | |
| Daytime sleepiness |  | Tremor impact on activities | Yes | Gait – shuffling, walking with difficulty | Yes | | |
| Pain and other sensations  |  | Getting in and out of bed  | Yes | Freezing of gait | Yes | | |
| Urinary problems | Yes | Walking, balance, falling | Yes | Postural stability – difficulty recovering balance | Yes | | |
| Constipation problems |  | Freezing | Yes | Posture – stooped | Yes | | |
| Lightheadedness on standing | Yes |  |  | Global spontaneity of movement (body bradykinesia) – slowness of movement, lack of movement | Yes | | |
| Fatigue |  |  |  | Tremor at rest |Yes | | |


（**This table is updated in real time based on the collected features**）

### 2. Data Summary

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


| stage_category | samples_num | 
| --- | --- |
| 0 | 1227 |  
| 1 | 865 |  
| 2 | 2386 |  
| 3 | 246 |  
| 4 | 47 | 
| 5 | 13 |  
| Totally  | 4784 | 



| stage_category | first_visit(patients_num) |  last_visit(patients_num) |
| --- | --- |--- |
| 0 | 685 |  |
| 1 | 359 |  |
| 2 | 543 |  |
| 3 | 66 |  |
| 4 | 18 | |
| 5 | 3 |  |
| Totally  | 1674 | |

### 3. True Label: Hoehn and Yahr scale
The Hoehn and Yahr scale is a commonly used system for describing how the 
symptoms of Parkinson's disease progress. Each sample (equal to each visit) in this dataset is
assigned with Hoehn and Yahr scale value ranging from 0 to 5 as a true label.

STAGE 0: NO SIGN OF DISEASE

STAGE 1: UNILATERAL DISEASE

STAGE 2: BILATERAL DISEASE, WITHOUT BALANCE IMPAIRMENT

STAGE 3: MILD TO MODERATE BILATERAL DISEASE, SOME POSTURAL INSTABILITY. 

STAGE 4: SEVERE DISABILITY, STILL ABLE TO WALK AND STAND UNASSISTED.

STAGE 5: WHEELCHAIR BOUND OR BEDRIDDEN


## Modeling
### 1. Baselines
Data selection: choose patients as input with more than 4 total visit times.

**Input**: the first three visits (Vt-2, Vt-1, Vt) and each visit with around 370 features

**Output**: **Hoehn and Yahr scale** of the next visit (Vt+1)

For example: assuming one patient has 6 total visit times, then samples of this 
patient should be 3:

Input: V1, V2, V3 Output: V4

Input: V2, V3, V4 Output: V5

Input: V3, V4, V5 Output: V6

| visit_times | patients_num | input_samples_num |
| --- | --- |--- |
| 4 | 128 | 128 |
| 5 | 105 | 210 |
| 6 | 142 | 426 |
| 7 | 102 | 408 |
| 8 | 45  | 225 |
| Totally  | 522 patients | 1397 input samples |

#### a) Linear Regression
<img src="IMG/linear_regression.png" width="600" height="400">


    Mean squared error: 2.58
    Variance score: -14.08
  
#### b) Logistic Regression
    Five times cross validation: CV score Logistic Regression:(array([0.64539007, 0.71785714, 0.70967742, 0.76702509, 0.75812274]), 0.7196144932844025)

#### c) Random Forest
    Five times cross validation: CV score RF:(array([0.57446809, 0.79285714, 0.78853047, 0.80645161, 0.79061372]), 0.750584205045625)

#### d) XGBoost
    Five times cross validation: CV score XGB:(array([0.37943262, 0.79285714, 0.78494624, 0.81362007, 0.80144404]), 0.714460023707129)



