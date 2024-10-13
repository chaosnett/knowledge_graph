% dataProcessor.m
% MATLAB Script for Processing Economic Data
% Author: Your Name
% Date: YYYY-MM-DD
% Description: This script performs data cleaning, normalization, and statistical
%              analysis on the economic simulation results.

%% Initialization
clc;
clear all;
close all;

% Load simulation data
data = readtable('EconomicSimulationResults.csv');

%% Data Cleaning
% Handle missing values by interpolation
data = fillmissing(data, 'linear');

% Remove outliers using Z-score method
numericVars = {'GDP_BillionUSD', 'Inflation_Percent', 'UnemploymentRate_Percent', 'TradeBalance_BillionUSD'};
for i = 1:length(numericVars)
    var = data.(numericVars{i});
    z = zscore(var);
    data(z > 3 | z < -3, numericVars{i}) = median(var, 'omitnan');
end

%% Data Normalization
% Normalize data between 0 and 1
for i = 1:length(numericVars)
    var = data.(numericVars{i});
    data.([numericVars{i}, '_Normalized']) = (var - min(var)) / (max(var) - min(var));
end

%% Statistical Analysis
% Correlation Matrix
correlationMatrix = corr(table2array(data(:, numericVars)), 'Type', 'Pearson');

% Principal Component Analysis (PCA)
[coeff, score, latent, tsquared, explained] = pca(table2array(data(:, numericVars)));

% Save analysis results
save('EconomicDataAnalysis.mat', 'correlationMatrix', 'coeff', 'score', 'latent', 'explained');

%% Visualization
% Heatmap of Correlation Matrix
figure('Name', 'Correlation Matrix Heatmap', 'NumberTitle', 'off');
heatmap(numericVars, numericVars, correlationMatrix, 'Colormap', jet, 'Colorbar', true);
title('Correlation Matrix of Economic Parameters');
xlabel('Economic Metrics');
ylabel('Economic Metrics');
saveas(gcf, 'CorrelationMatrixHeatmap.png');

% PCA Biplot
figure('Name', 'PCA Biplot', 'NumberTitle', 'off');
biplot(coeff(:,1:2), 'Scores', score(:,1:2), 'VarLabels', numericVars);
title('PCA Biplot of Economic Parameters');
xlabel('Principal Component 1');
ylabel('Principal Component 2');
saveas(gcf, 'PCA_Biplot.png');
