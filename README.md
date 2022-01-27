# Medical Cost Prediction project
1. 출처 : [Kaggle Data set - Medical Cost Personal Datasets](https://www.kaggle.com/mirichoi0218/insurance)

2. Data fields
    - Age: 피보험자의 나이  

    - Sex: 피보험자의 성별  

    - BMI: 피보험자의 체질량 지수 ( 체중(kg) / 키(m)^2 )

    - Children: 피보험자의 자녀의 수  

    - Smoker: 흡연 여부 (yes / no)  

    - Region: 피보험자가 거주하는 지역 (Southeast / Southwest / Northeast / Northwest)  

    - Charges: 보험료  

Contents
-------------------
[프로젝트 과정 NOTE](https://github.com/ADGGi/InsuranceBill/blob/master/pred_insurance_bill/EDA_Modeling/EDA_ML_Model_result.ipynb)
1. EDA 및 데이터 전처리
2. 변수 분석
3. Modeling
    - Linear Regression
    - Random Forest Regression
    - XGB Regression
    - Ridge Regression
    - KNN Regression
    - Gradient Boosting Regression

|ML Models|	Score|
|-------|--------|
Gradient Boosting Regression|	0.915826|
XGBRegression|	0.914670|
RandomForestRegression|	0.911131|
KNN Regression|	0.837118|
LinearRegression|	0.828913|
RidgeRegression|	0.828171|

4. 하이퍼파라미터 튜닝 (GridsearchCV)

- min_sample_leaf = 5
- n_estimators = 90



최종모델
----------------------
- 하이퍼 파라미터 튜닝한 Gradient Boosting Regression 모델
- Score
    - r_square score :  약 0.918
    - MAE : 약 0.163
    - MSE : 약 0.071
    - RMSE : 약 0.266

![rsquare](https://user-images.githubusercontent.com/86307300/151042025-9af77993-77cf-40d6-ba36-66d73679273d.png)

flask web
-------------------
![ezgif-7-3924c4facc](https://user-images.githubusercontent.com/86307300/150835198-cc2df496-196e-4ed5-86c5-71f3791bf0f8.gif)
