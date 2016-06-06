
clear all
close all
clc

y   = [9,11,10,12,7,11,12,10,11,13,10,15,11,15,15,13,7,15,13,10,18,14,17,9,14,17,16,14,17,15]';
x   = [1*ones(10,1);2*ones(10,1);3*ones(10,1)]; % factor variable for the strategies
X   = [ones(30,1),x];                           % regression variable matrix
[b,bint,r,rint,stats] = regress(y,X)            % regression and summary
[p,table,stats]       = anova1(y,x)             % anova table

set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold');
