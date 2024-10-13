% visualizationTools.m
% MATLAB Class for Advanced Visualization Tools
% Author: Your Name
% Date: YYYY-MM-DD
% Description: This class provides methods for creating advanced visualizations
%              such as interactive dashboards, 3D plots, and animated simulations
%              based on economic simulation data.

classdef VisualizationTools
    properties
        DataTable
    end
    
    methods
        function obj = VisualizationTools(dataPath)
            % Constructor: Loads data from the specified path
            if nargin > 0
                obj.DataTable = readtable(dataPath);
            else
                error('Data path must be provided.');
            end
        end
        
        function plot3DScatter(obj, xVar, yVar, zVar)
            % Method to create a 3D scatter plot
            figure('Name', '3D Scatter Plot', 'NumberTitle', 'off');
            scatter3(obj.DataTable.(xVar), obj.DataTable.(yVar), obj.DataTable.(zVar), ...
                     36, obj.DataTable.(zVar), 'filled');
            colorbar;
            colormap(jet);
            title(sprintf('3D Scatter Plot: %s vs %s vs %s', xVar, yVar, zVar));
            xlabel(xVar);
            ylabel(yVar);
            zlabel(zVar);
            grid on;
            saveas(gcf, '3D_ScatterPlot.png');
        end
        
        function createInteractiveDashboard(obj)
            % Method to create an interactive dashboard
            import matlab.ui.*
            fig = uifigure('Name', 'Economic Dashboard', 'Position', [100 100 800 600]);
            
            % Dropdown for selecting metric
            dd = uidropdown(fig, 'Position', [50 550 150 30], ...
                           'Items', {'GDP_BillionUSD', 'Inflation_Percent', ...
                                     'UnemploymentRate_Percent', 'TradeBalance_BillionUSD'}, ...
                           'ValueChangedFcn', @(dd,event) updatePlot(dd.Value));
            
            % Axes for plotting
            ax = uiaxes(fig, 'Position', [50 50 700 450]);
            title(ax, 'Economic Parameter Over Time');
            xlabel(ax, 'Quarter');
            ylabel(ax, 'Value');
            grid(ax, 'on');
            
            % Initial Plot
            plot(ax, obj.DataTable.Quarter, obj.DataTable.GDP_BillionUSD, 'LineWidth', 2);
            legend(ax, 'GDP');
            
            function updatePlot(selectedMetric)
                cla(ax);
                plot(ax, obj.DataTable.Quarter, obj.DataTable.(selectedMetric), 'LineWidth', 2);
                title(ax, sprintf('%s Over Time', strrep(selectedMetric, '_', ' ')));
                ylabel(ax, strrep(selectedMetric, '_', ' '));
                legend(ax, strrep(selectedMetric, '_', ' '));
                grid(ax, 'on');
            end
        end
        
        function animateSimulation(obj, metric)
            % Method to create an animated plot of a selected metric
            figure('Name', 'Simulation Animation', 'NumberTitle', 'off');
            h = plot(NaN, NaN, 'LineWidth', 2);
            title(sprintf('Animated Simulation: %s Over Time', strrep(metric, '_', ' ')));
            xlabel('Quarter');
            ylabel(strrep(metric, '_', ' '));
            grid on;
            hold on;
            ylim([min(obj.DataTable.(metric)) * 0.9, max(obj.DataTable.(metric)) * 1.1]);
            xlim([1, max(obj.DataTable.Quarter)]);
            
            for t = 1:height(obj.DataTable)
                set(h, 'XData', obj.DataTable.Quarter(1:t), ...
                       'YData', obj.DataTable.(metric)(1:t));
                drawnow;
                pause(0.1); % Adjust speed as needed
            end
            hold off;
            saveas(gcf, sprintf('Animation_%s.gif', metric));
        end
    end
end
