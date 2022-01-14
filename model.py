# import libraries
import pandas as pd # for data manupulation or analysis
import numpy as np # for numeric calculation
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for data visualization
import category_encoders as ce

def result(breast_density,breast,image,abnormality,massShape,massMargins,assessment,subtlety):
    cancer_df=pd.read_csv('mass_case_description_train_set.csv')
    data=[[breast_density,breast,image,abnormality,massShape,massMargins,assessment,subtlety]]
    X_test=pd.DataFrame(data, columns = ['breast_density', 'left or right breast','image view','abnormality id','mass shape','mass margin','assessment','subtlety'])
    cancer_df=cancer_df.dropna(subset=['mass shape','mass margins'])

    #input Variable
    X=cancer_df.drop(['patient_id','image file path','cropped image file path','ROI mask file path','pathology'], axis = 1)
    y=cancer_df["pathology"]
    ce_OHE=ce.OneHotEncoder(cols=['pathology'])
    y.replace(to_replace=['MALIGNANT', 'BENIGN', 'BENIGN_WITHOUT_CALLBACK'], value=[1, 2, 3], inplace=True)
    y.unique()
    X["left or right breast"].replace(to_replace=['LEFT', 'RIGHT'], value=[0,1], inplace=True)
    X["image view"].replace(to_replace=['CC', 'MLO'], value=[0,1], inplace=True)
    X=X.drop(["abnormality type"],axis=1)

    X["mass shape"].replace(to_replace=['IRREGULAR-ARCHITECTURAL_DISTORTION', 'ARCHITECTURAL_DISTORTION','OVAL', 'IRREGULAR', 'LYMPH_NODE', 'LOBULATED-LYMPH_NODE','LOBULATED', 'FOCAL_ASYMMETRIC_DENSITY', 'ROUND','LOBULATED-ARCHITECTURAL_DISTORTION', 'LOBULATED-IRREGULAR','OVAL-LYMPH_NODE', 'ASYMMETRIC_BREAST_TISSUE', 'LOBULATED-OVAL','ROUND-OVAL', 'IRREGULAR-FOCAL_ASYMMETRIC_DENSITY','ROUND-IRREGULAR-ARCHITECTURAL_DISTORTION', 'ROUND-LOBULATED'], value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], inplace=True)

    X["mass margins"].replace(to_replace=['SPICULATED', 'ILL_DEFINED', 'CIRCUMSCRIBED','ILL_DEFINED-SPICULATED', 'OBSCURED', 'OBSCURED-ILL_DEFINED','MICROLOBULATED', 'MICROLOBULATED-ILL_DEFINED-SPICULATED','MICROLOBULATED-SPICULATED', 'CIRCUMSCRIBED-ILL_DEFINED','MICROLOBULATED-ILL_DEFINED', 'CIRCUMSCRIBED-OBSCURED','OBSCURED-SPICULATED', 'OBSCURED-ILL_DEFINED-SPICULATED','CIRCUMSCRIBED-MICROLOBULATED'], value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], inplace=True)




    from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier

    adb_classifier = AdaBoostClassifier(DecisionTreeClassifier(criterion = 'entropy', random_state = 0),n_estimators=100,learning_rate=0.1,algorithm='SAMME.R',random_state=0,)
    adb_classifier.fit(X, y)
    y_pred_adb = adb_classifier.predict(X_test)
    if y_pred_adb[0]==1:
            return "MALIGNANT"
    elif y_pred_adb[0]==2:
            return "BENIGN"
    else:
            return "BENIGN_WITHOUT_CALLBACK"


