% graphHandler.m
% MATLAB Function for Handling Graph Operations
% Author: Your Name
% Date: YYYY-MM-DD
% Description: This function manages graph creation, manipulation, and visualization
%              for the economic simulation data.

function graphHandler(economicDataPath)
    %% Load Data
    data = readtable(economicDataPath);
    
    %% Create Graph Object
    G = digraph();
    
    % Define nodes
    nodes = {'GDP', 'Inflation', 'Unemployment Rate', 'Trade Balance'};
    G = addnode(G, nodes);
    
    % Define edges with weights based on correlations
    correlations = [0.85, -0.65, -0.75;  % GDP correlations
                    -0.65, 0.90, 0.50;  % Inflation correlations
                    -0.75, 0.50, 0.80;  % Unemployment correlations
                    0.65, -0.50, -0.80]; % Trade Balance correlations
    
    % Add edges
    for i = 1:length(nodes)
        for j = 1:length(nodes)
            if i ~= j
                weight = correlations(i,j);
                G = addedge(G, nodes{i}, nodes{j}, weight);
            end
        end
    end
    
    %% Plot Graph
    figure('Name', 'Economic Graph', 'NumberTitle', 'off');
    p = plot(G, 'Layout', 'force', 'EdgeLabel', G.Edges.Weight, ...
             'NodeColor', 'c', 'MarkerSize', 7, 'LineWidth', 1.5);
    title('Economic Parameters Correlation Graph');
    xlabel('Economic Metrics');
    ylabel('Correlation Strength');
    grid on;
    
    % Save graph plot
    saveas(gcf, 'EconomicGraph.png');
    
    %% Graph Metrics
    fprintf('Graph Metrics:\n');
    fprintf('Number of Nodes: %d\n', numnodes(G));
    fprintf('Number of Edges: %d\n', numedges(G));
    fprintf('Average Degree: %.2f\n', mean(degree(G)));
    fprintf('Density: %.4f\n', graphdensity(G));
    
    %% Shortest Path Example
    src = 'GDP';
    tgt = 'Unemployment Rate';
    [path, pathWeights] = shortestpath(G, src, tgt, 'Method', 'positive');
    fprintf('Shortest path from %s to %s:\n', src, tgt);
    disp(path);
    disp('Edge Weights Along Path:');
    disp(pathWeights);
    
    %% Save Graph Object
    save('EconomicGraphObject.mat', 'G');
end
