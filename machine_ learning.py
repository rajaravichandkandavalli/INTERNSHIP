#!/usr/bin/env python
# coding: utf-8

# 1.Which of the following methods do we use to find the best fit line for data in Linear Regression?

# Least square error

# 2.Which of the following statement is true about outliers in linear regression?

# Linear regression is sensitive to outliers

# 3.A line falls from left to right if a slope is ______?

# Positive

# 4.Which of the following will have symmetric relation between dependent variable and independent variable?

#  Regression

# 5.Which of the following is the reason for over fitting condition?
# 

# High bias and high variance

# 6.If output involves label then that model is called as

# Descriptive model ,Predictive modal ,Reinforcement learning.

# 7.Lasso and Ridge regression techniques belong to _________?

# Removing outliers

# 8.To overcome with imbalance dataset which technique can be used?

# SMOTE

# 9.The AUC Receiver Operator Characteristic (AUCROC) curve is an evaluation metric for binary classification problems. It uses _____ to make graph?

# Sensitivity and Specificity

# 10.In AUC Receiver Operator Characteristic (AUCROC) curve for the better model area under the curve should be less.

# False

# 11. Pick the feature extraction from below:

#  Construction bag of words from a email

# 12.Which of the following is true about Normal Equation used to compute the coefficient of the Linear Regression?

# It becomes slow when number of features is very large.  We need to iterate.

# 13. Explain the term regularization?

# Regularization
# This is a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards zero. In other words, this technique discourages learning a more complex or flexible model, so as to avoid the risk of overfitting.
# A simple relation for linear regression looks like this. Here Y represents the learned relation and β represents the coefficient estimates for different variables or predictors(X).
# Y ≈ β0 + β1X1 + β2X2 + …+ βpXp
# The fitting procedure involves a loss function, known as residual sum of squares or RSS. The coefficients are chosen, such that they minimize this loss function.
# 
# Now, this will adjust the coefficients based on your training data. If there is noise in the training data, then the estimated coefficients won’t generalize well to the future data. This is where regularization comes in and shrinks or regularizes these learned estimates towards zero.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# 14. Which particular algorithms are used for regularization?

# Techniques of Regularization
# Mainly, there are two types of regularization techniques, which are given below:
# 
#  
# 
# Ridge Regression
# Lasso Regression
# 
# This article was published as a part of the Data Science Blogathon
# 
# Introduction
# One of the most common problems every Data Science practitioner faces is Overfitting. Have you tackled the situation where your machine learning model performed exceptionally well on the train data but was not able to predict on the unseen data or you were on the top of the competition in the public leaderboard, but your ranking drops by hundreds of places in the final rankings?
# 
# Well – this is the article for you!
# 
# Avoiding overfitting can single-handedly improve our model’s performance.
# 
# In this article, we will understand how regularization helps in overcoming the problem of overfitting and also increases the model interpretability.
# 
# This article is written under the assumption that you have a basic understanding of Regression models including Simple and Multiple linear regression, etc.
# 
# Table of Contents
# 👉 Why Regularization?
# 👉 What is Regularization?
# 👉 How does Regularization work?
# 👉 Techniques of Regularization
# Ridge Regression
# Lasso Regression
# 👉 Key differences between Ridge and Lasso Regression
# 👉 Mathematical Formulation of Regularization Techniques
# 👉 What does Regularization Achieve?
# Why Regularization?
# Sometimes what happens is that our Machine learning model performs well on the training data but does not perform well on the unseen or test data. It means the model is not able to predict the output or target column for the unseen data by introducing noise in the output, and hence the model is called an overfitted model.
# 
# Let’s understand the meaning of “Noise” in a brief manner:
# 
# By noise we mean those data points in the dataset which don’t really represent the true properties of your data, but only due to a random chance.
# 
# So, to deal with the problem of overfitting we take the help of regularization techniques.
# 
# What is Regularization?
# 👉 It is one of the most important concepts of machine learning. This technique prevents the model from overfitting by adding extra                      information to it.
# 👉 It is a form of regression that shrinks the coefficient estimates towards zero. In other words, this technique forces us not to learn a more            complex or flexible model, to avoid the problem of overfitting.
# 👉 Now, let’s understand the “How flexibility of a model is represented?”
#     For regression problems, the increase in flexibility of a model is represented by an increase in its coefficients, which are calculated              from the regression line.
# 👉 In simple words, “In the Regularization technique, we reduce the magnitude of the independent variables by keeping the same                number of variables”. It maintains accuracy as well as a generalization of the model.
# How does Regularization Work?
# Regularization works by adding a penalty or complexity term or shrinkage term with Residual Sum of Squares (RSS) to the complex model.
# 
# Let’s consider the Simple linear regression equation:
# 
# Here Y represents the dependent feature or response which is the learned relation. Then,
# 
# Y is approximated to β0 + β1X1 + β2X2 + …+ βpXp
# 
# Here, X1, X2, …Xp are the independent features or predictors for Y, and
# 
# β0, β1,…..βn represents the coefficients estimates for different variables or predictors(X), which describes the weights or magnitude attached to the features, respectively.
# 
# In simple linear regression, our optimization function or loss function is known as the residual sum of squares (RSS).
# 
# We choose those set of coefficients, such that the following loss function is minimized:
# 
# Regularization
# 
# Fig. Cost Function For Simple Linear Regression
# 
# Image Source: link
# 
# Now, this will adjust the coefficient estimates based on the training data. If there is noise present in the training data, then the estimated coefficients won’t generalize well and are not able to predict the future data.
# 
# This is where regularization comes into the picture, which shrinks or regularizes these learned estimates towards zero, by adding a loss function with optimizing parameters to make a model that can predict the accurate value of Y.
# 
# Techniques of Regularization
# Mainly, there are two types of regularization techniques, which are given below:
# 
#  
# 
# Ridge Regression
# Lasso Regression
#  
# Ridge Regression
#  
# 
# 👉 Ridge regression is one of the types of linear regression in which we introduce a small amount of bias, known as Ridge regression penalty so that we can get better long-term predictions.
# 
# 👉 In Statistics, it is known as the L-2 norm.
# 
# 👉 In this technique, the cost function is altered by adding the penalty term (shrinkage term), which multiplies the lambda with the squared weight of each individual feature. Therefore, the optimization function(cost function) becomes:
# 
# ![1*CiqZ8lhwxi5c4d1nV24w4g.png](attachment:1*CiqZ8lhwxi5c4d1nV24w4g.png)
#  

# 👉 Usage of Ridge Regression:
# 
# When we have the independent variables which are having high collinearity (problem of multicollinearity) between them, at that time general linear or polynomial regression will fail so to solve such problems, Ridge regression can be used.
# If we have more parameters than the samples, then Ridge regression helps to solve the problems.
# 
# 👉 Limitation of Ridge Regression:
# 
#  
# 
# Not helps in Feature Selection: It decreases the complexity of a model but does not reduce the number of independent variables since it never leads to a coefficient being zero rather only minimizes it. Hence, this technique is not good for feature selection.
# Model Interpretability: Its disadvantage is model interpretability since it will shrink the coefficients for least important predictors, very close to zero but it will never make them exactly zero. In other words, the final model will include all the independent variables, also known as predictors.
# 
# This article was published as a part of the Data Science Blogathon
# 
# Introduction
# One of the most common problems every Data Science practitioner faces is Overfitting. Have you tackled the situation where your machine learning model performed exceptionally well on the train data but was not able to predict on the unseen data or you were on the top of the competition in the public leaderboard, but your ranking drops by hundreds of places in the final rankings?
# 
# Well – this is the article for you!
# 
# Avoiding overfitting can single-handedly improve our model’s performance.
# 
# In this article, we will understand how regularization helps in overcoming the problem of overfitting and also increases the model interpretability.
# 
# This article is written under the assumption that you have a basic understanding of Regression models including Simple and Multiple linear regression, etc.
# 
# Table of Contents
# 👉 Why Regularization?
# 👉 What is Regularization?
# 👉 How does Regularization work?
# 👉 Techniques of Regularization
# Ridge Regression
# Lasso Regression
# 👉 Key differences between Ridge and Lasso Regression
# 👉 Mathematical Formulation of Regularization Techniques
# 👉 What does Regularization Achieve?
# Why Regularization?
# Sometimes what happens is that our Machine learning model performs well on the training data but does not perform well on the unseen or test data. It means the model is not able to predict the output or target column for the unseen data by introducing noise in the output, and hence the model is called an overfitted model.
# 
# Let’s understand the meaning of “Noise” in a brief manner:
# 
# By noise we mean those data points in the dataset which don’t really represent the true properties of your data, but only due to a random chance.
# 
# So, to deal with the problem of overfitting we take the help of regularization techniques.
# 
# What is Regularization?
# 👉 It is one of the most important concepts of machine learning. This technique prevents the model from overfitting by adding extra                      information to it.
# 👉 It is a form of regression that shrinks the coefficient estimates towards zero. In other words, this technique forces us not to learn a more            complex or flexible model, to avoid the problem of overfitting.
# 👉 Now, let’s understand the “How flexibility of a model is represented?”
#     For regression problems, the increase in flexibility of a model is represented by an increase in its coefficients, which are calculated              from the regression line.
# 👉 In simple words, “In the Regularization technique, we reduce the magnitude of the independent variables by keeping the same                number of variables”. It maintains accuracy as well as a generalization of the model.
# How does Regularization Work?
# Regularization works by adding a penalty or complexity term or shrinkage term with Residual Sum of Squares (RSS) to the complex model.
# 
# Let’s consider the Simple linear regression equation:
# 
# Here Y represents the dependent feature or response which is the learned relation. Then,
# 
# Y is approximated to β0 + β1X1 + β2X2 + …+ βpXp
# 
# Here, X1, X2, …Xp are the independent features or predictors for Y, and
# 
# β0, β1,…..βn represents the coefficients estimates for different variables or predictors(X), which describes the weights or magnitude attached to the features, respectively.
# 
# In simple linear regression, our optimization function or loss function is known as the residual sum of squares (RSS).
# 
# We choose those set of coefficients, such that the following loss function is minimized:
# 
# Regularization
# 
# Fig. Cost Function For Simple Linear Regression
# 
# Image Source: link
# 
# Now, this will adjust the coefficient estimates based on the training data. If there is noise present in the training data, then the estimated coefficients won’t generalize well and are not able to predict the future data.
# 
# This is where regularization comes into the picture, which shrinks or regularizes these learned estimates towards zero, by adding a loss function with optimizing parameters to make a model that can predict the accurate value of Y.
# 
# Techniques of Regularization
# Mainly, there are two types of regularization techniques, which are given below:
# 
#  
# 
# Ridge Regression
# Lasso Regression
#  
# Ridge Regression
#  
# 
# 👉 Ridge regression is one of the types of linear regression in which we introduce a small amount of bias, known as Ridge regression penalty so that we can get better long-term predictions.
# 
# 👉 In Statistics, it is known as the L-2 norm.
# 
# 👉 In this technique, the cost function is altered by adding the penalty term (shrinkage term), which multiplies the lambda with the squared weight of each individual feature. Therefore, the optimization function(cost function) becomes:
# 
# ridge Regularization
# 
#  
# 
#  
# 
# Fig. Cost Function for Ridge Regression
# 
#  
# 
#  
# 
# Image Source: link
# 
# In the above equation, the penalty term regularizes the coefficients of the model, and hence ridge regression reduces the magnitudes of the coefficients that help to decrease the complexity of the model.
# 
#  
# 
# 👉 Usage of Ridge Regression:
# 
# When we have the independent variables which are having high collinearity (problem of multicollinearity) between them, at that time general linear or polynomial regression will fail so to solve such problems, Ridge regression can be used.
# If we have more parameters than the samples, then Ridge regression helps to solve the problems.
#  
# 
# 👉 Limitation of Ridge Regression:
# 
#  
# 
# Not helps in Feature Selection: It decreases the complexity of a model but does not reduce the number of independent variables since it never leads to a coefficient being zero rather only minimizes it. Hence, this technique is not good for feature selection.
# Model Interpretability: Its disadvantage is model interpretability since it will shrink the coefficients for least important predictors, very close to zero but it will never make them exactly zero. In other words, the final model will include all the independent variables, also known as predictors.
#  
# 
#  
# 
# Lasso Regression
# 👉 Lasso regression is another variant of the regularization technique used to reduce the complexity of the model. It stands for Least Absolute and Selection Operator.
# 
# 👉 It is similar to the Ridge Regression except that the penalty term includes the absolute weights instead of a square of weights. Therefore, the optimization function becomes:
# 
# ![1*tHJ4sSPYV0bDr8xxEdiwXA.png](attachment:1*tHJ4sSPYV0bDr8xxEdiwXA.png)
#  
#  

# 15. Explain the term error present in linear regression equation?

# Error Term
# An error term is a residual variable produced by a statistical or mathematical model, which is created when the model does not fully represent the actual relationship between the independent variables and the dependent variables. As a result of this incomplete relationship, the error term is the amount at which the equation may differ during empirical analysis.
# 
# The error term is also known as the residual, disturbance, or remainder term, and is variously represented in models by the letters e, ε, or u.
# 
# An error term appears in a statistical model, like a regression model, to indicate the uncertainty in the model.
# The error term is a residual variable that accounts for a lack of perfect goodness of fit.
# Heteroskedastic refers to a condition in which the variance of the residual term, or error term, in a regression model varies widely.
# 
# Understanding an Error Term
# An error term represents the margin of error within a statistical model; it refers to the sum of the deviations within the regression line, which provides an explanation for the difference between the theoretical value of the model and the actual observed results. The regression line is used as a point of analysis when attempting to determine the correlation between one independent variable and one dependent variable.
# 
# 
# Error Term Use in a Formula
# An error term essentially means that the model is not completely accurate and results in differing results during real-world applications. For example, assume there is a multiple linear regression function that takes the following form: 
# 
# Y
# =
# α
# X
# +
# β
# ρ
# +
# ϵ
# where:
# α
# ,
# β
# =
# Constant parameters
# X
# ,
# ρ
# =
# Independent variables
# ϵ
# =
# Error term
#  
# ​	  
# Y=αX+βρ+ϵ
# where:
# α,β=Constant parameters
# X,ρ=Independent variables
# ϵ=Error term
# ​	 
# 
# Linear Regression, Error Term, and Stock Analysis
# Linear regression is a form of analysis that relates to current trends experienced by a particular security or index by providing a relationship between a dependent and independent variables, such as the price of a security and the passage of time, resulting in a trend line that can be used as a predictive model.
# 
# A linear regression exhibits less delay than that experienced with a moving average, as the line is fit to the data points instead of based on the averages within the data. This allows the line to change more quickly and dramatically than a line based on numerical averaging of the available data points.
# 
# 
# The Difference Between Error Terms and Residuals
# Although the error term and residual are often used synonymously, there is an important formal difference. An error term is generally unobservable and a residual is observable and calculable, making it much easier to quantify and visualize. In effect, while an error term represents the way observed data differs from the actual population, a residual represents the way observed data differs from sample population data.

# In[ ]:




