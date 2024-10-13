% simulationModel.m
% MATLAB Script for Economic Simulation Model
% Author: Your Name
% Date: YYYY-MM-DD
% Description: This script models the economic impact of various parameters
%              such as GDP, inflation, and trade balance on a simulated economy.

%% Initialization
clc;
clear all;
close all;

% Define simulation parameters
simulationDuration = 100; % in quarters
time = linspace(1, simulationDuration, simulationDuration);

% Initialize variables
GDP = zeros(1, simulationDuration);
Inflation = zeros(1, simulationDuration);
UnemploymentRate = zeros(1, simulationDuration);
TradeBalance = zeros(1, simulationDuration);

% Initial conditions
GDP(1) = 1000; % in billion USD
Inflation(1) = 2.0; % in %
UnemploymentRate(1) = 5.0; % in %
TradeBalance(1) = 50; % in billion USD

%% Simulation Loop
for t = 2:simulationDuration
    % GDP Growth Calculation
    GDPGrowthRate = 0.03 - 0.002 * Inflation(t-1) + 0.0015 * TradeBalance(t-1);
    GDP(t) = GDP(t-1) * (1 + GDPGrowthRate);
    
    % Inflation Adjustment
    Inflation(t) = Inflation(t-1) + 0.5 * (GDPGrowthRate - 0.02) + 0.1 * randn;
    
    % Unemployment Rate Dynamics
    UnemploymentRate(t) = UnemploymentRate(t-1) - 0.5 * GDPGrowthRate + 0.2 * randn;
    UnemploymentRate(t) = max(UnemploymentRate(t), 0.5); % Prevent negative unemployment
    
    % Trade Balance Fluctuations
    TradeBalance(t) = TradeBalance(t-1) + 2 * GDPGrowthRate - 1.5 * Inflation(t);
end

%% Results Compilation
economicData = table(time', GDP', Inflation', UnemploymentRate', TradeBalance', ...
    'VariableNames', {'Quarter', 'GDP_BillionUSD', 'Inflation_Percent', ...
                      'UnemploymentRate_Percent', 'TradeBalance_BillionUSD'});

% Save simulation results
writetable(economicData, 'EconomicSimulationResults.csv');

%% Plotting Results
figure('Name', 'Economic Simulation Results', 'NumberTitle', 'off');
subplot(2,2,1);
plot(time, GDP, 'LineWidth', 2);
title('GDP Over Time');
xlabel('Quarter');
ylabel('GDP (Billion USD)');
grid on;

subplot(2,2,2);
plot(time, Inflation, 'r', 'LineWidth', 2);
title('Inflation Rate Over Time');
xlabel('Quarter');
ylabel('Inflation (%)');
grid on;

subplot(2,2,3);
plot(time, UnemploymentRate, 'g', 'LineWidth', 2);
title('Unemployment Rate Over Time');
xlabel('Quarter');
ylabel('Unemployment Rate (%)');
grid on;

subplot(2,2,4);
plot(time, TradeBalance, 'm', 'LineWidth', 2);
title('Trade Balance Over Time');
xlabel('Quarter');
ylabel('Trade Balance (Billion USD)');
grid on;

% Save plots
saveas(gcf, 'EconomicSimulationPlots.png');
