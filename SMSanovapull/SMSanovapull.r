
# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

y   = c(9,11,10,12,7,11,12,10,11,13,10,15,11,15,15,13,7,15,13,10,18,14,17,9,14,17,16,14,17,15)
x   = factor(rep(1:3,each=10))   # factor variable for 3 strategies and 30 observations
lm1 = lm(y~x)                    # linear model

anova(lm1)                       # anova table
summary(lm1)                     # regression summary
