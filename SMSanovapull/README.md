
[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSanovapull** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMSanovapull

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'performes a linear regression and an analysis of variance (ANOVA) for three
marketing strategies. A company decides to compare the effect of three marketing strategies: 1.
advertisement in local newspaper 2. presence of sales assistant 3. special presentation in shop
windows, on the sales of their portfolio in 30 shops. The 30 shops were divided into 3 groups of 10
shops. The sales using the strategies 1, 2, and 3 were y1 = (9, 11, 10, 12, 7, 11, 12, 10, 11, 13)
y2 = (10, 15, 11, 15, 15, 13, 7, 15, 13, 10) and y3 = (18, 14, 17, 9, 14, 17, 16, 14, 17, 15)
respectively. A null hypothesis of equality of means of the three groups is tested. The standard
approach of using ANOVA leads to an F-test. The alternative proposition is to use a linear factor
model using the strategies as regression variables to build curve that corresponds to the
alternative hypothesis of the ANOVA with three horizontal lines, each for one strategy. The F-test
of testing equality of the coefficients to zero corresponds to the null of testing the marketing
strategies having no effect. The output shows rejection of the null hypothesis. For more
information see Exercise 3.20.'

Keywords : 'regression, analysis, variance, factor-model, linear-model, F-test, F-statistic, mean,
heteroskedasticity, test, Testing'

See also : SMScovbank, SMSdete2pull, SMSdeterpull, SMSlinregpull, SMSscabank45

Author[r] : Dana Chromikova

Author[m] : Awdesch Melzer

Datafile[r] : pullover.rda

Datafile[m] : pullover.dat

Output : Summary statistics for linear regression and ANOVA and boxplot.

```

![Picture1](SMSanovapull.png)

![Picture2](SMSanovapull1.png)


### MATLAB Code:
```matlab

clear all
close all
clc

y   = [9,11,10,12,7,11,12,10,11,13,10,15,11,15,15,13,7,15,13,10,18,14,17,9,14,17,16,14,17,15]';
x   = [1*ones(10,1);2*ones(10,1);3*ones(10,1)]; % factor variable for the strategies
X   = [ones(30,1),x];                           % regression variable matrix
[b,bint,r,rint,stats] = regress(y,X)            % regression and summary
[p,table,stats]       = anova1(y,x)             % anova table

set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold');

```

### R Code:
```r

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

y   = c(9,11,10,12,7,11,12,10,11,13,10,15,11,15,15,13,7,15,13,10,18,14,17,9,14,17,16,14,17,15)
x   = factor(rep(1:3,each=10))   # factor variable for 3 strategies and 30 observations
lm1 = lm(y~x)                    # linear model

anova(lm1)                       # anova table
summary(lm1)                     # regression summary

```
