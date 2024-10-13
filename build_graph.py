import pandas as pd
import json
import math
import string
import random

MAX_PRODUCTS = 7

def generate_graph_data(import_csv_file, export_csv_file, output_nodes_file, output_edges_file):
    df_import = pd.read_csv(import_csv_file)
    df_export = pd.read_csv(export_csv_file)

    df_import = df_import.head(MAX_PRODUCTS)
    df_export = df_export.head(MAX_PRODUCTS)

    nodes = []
    edges = []

    home_country = "USA"

    node_id_counter = 1
    node_ids = {} 

    home_node = {
        "id": str(node_id_counter),
        "position": {"x": 0, "y": 0},
        "data": {"label": home_country}
    }
    nodes.append(home_node)
    node_ids[home_country] = str(node_id_counter)
    node_id_counter += 1

    node_id_counter = process_trade_data(
        df_import,
        nodes,
        edges,
        node_ids,
        node_id_counter,
        home_country,
        trade_type='Import'
    )

    node_id_counter = process_trade_data(
        df_export,
        nodes,
        edges,
        node_ids,
        node_id_counter,
        home_country,
        trade_type='Export'
    )

    node_id_counter = add_industry_nodes(nodes, edges, node_ids, node_id_counter)

    node_id_counter = add_tariff_nodes(nodes, edges, node_ids, node_id_counter)

    node_id_counter = add_policy_nodes(nodes, edges, node_ids, node_id_counter)

    assign_positions(nodes)

    with open(output_nodes_file, 'w') as f:
        json.dump(nodes, f, indent=2)

    with open(output_edges_file, 'w') as f:
        json.dump(edges, f, indent=2)

    print(f"Graph data generated and saved to '{output_nodes_file}' and '{output_edges_file}'.")

def process_trade_data(df, nodes, edges, node_ids, node_id_counter, home_country, trade_type='Import'):
    country_columns = [col for col in df.columns if col.startswith(f'Total {trade_type} from') or col.startswith(f'Total {trade_type} to')]

    countries = [col.replace(f'Total {trade_type} from ', '').replace(f'Total {trade_type} to ', '').strip() for col in country_columns]

    for country in countries:
        if country not in node_ids:
            node = {
                "id": str(node_id_counter),
                "position": {"x": 0, "y": 0},
                "data": {"label": country.replace("(in USD)", "")}
            }
            nodes.append(node)
            node_ids[country] = str(node_id_counter)
            node_id_counter += 1

    for index, row in df.iterrows():
        product_code = str(row['Product Code'])
        product_label = str(row['Product Label'])

        trade_node_label = f"{trade_type} {product_label} ({product_code})"

        simplified_label = " ".join([a.strip(string.punctuation) for a in trade_node_label.split(" ")[0:2]])

        if trade_node_label not in node_ids:
            node = {
                "id": str(node_id_counter),
                "position": {"x": 0, "y": 0},
                "data": {
                    "label": simplified_label,
                    "product_code": product_code,
                    "product_label": product_label
                }
            }
            nodes.append(node)
            node_ids[trade_node_label] = str(node_id_counter)
            node_id_counter += 1

        if trade_type == 'Import':
            edge_id = f"e{node_ids[home_country]}-{node_ids[trade_node_label]}"
            edges.append({
                "id": edge_id,
                "source": node_ids[home_country],
                "target": node_ids[trade_node_label],
                "value": None,
                "tradeType": trade_type.lower()
            })
        else:
            edge_id = f"e{node_ids[trade_node_label]}-{node_ids[home_country]}"
            edges.append({
                "id": edge_id,
                "source": node_ids[trade_node_label],
                "target": node_ids[home_country],
                "value": None,
                "tradeType": trade_type.lower()
            })

        for country_column in country_columns:
            country = country_column.replace(f'Total {trade_type} from ', '').replace(f'Total {trade_type} to ', '').strip()
            amount = row[country_column]
            if pd.notna(amount) and amount > 0:
                if trade_type == 'Import':
                    edge_id = f"e{node_ids[trade_node_label]}-{node_ids[country]}"
                    edges.append({
                        "id": edge_id,
                        "source": node_ids[trade_node_label],
                        "target": node_ids[country],
                        "value": amount,
                        "tradeType": trade_type.lower()
                    })
                else:
                    edge_id = f"e{node_ids[country]}-{node_ids[trade_node_label]}"
                    edges.append({
                        "id": edge_id,
                        "source": node_ids[country],
                        "target": node_ids[trade_node_label],
                        "value": amount,
                        "tradeType": trade_type.lower()
                    })

    return node_id_counter

def add_industry_nodes(nodes, edges, node_ids, node_id_counter):
    industries = [
        "Pharmaceuticals",
        "Agriculture",
        "Textiles",
        "Electronics",
        "Food & Beverage",
        "Chemical and Chemical Products",
        "Telecommunications",
        "Mining & Metals",
        "Logistics & Transportation",
        "Financial Services"
        ]
    
    product_nodes = [node for node in nodes if 'product_label' in node['data']]
    for product_node in product_nodes:
        industry = random.choice(industries)
        industry_node_label = f"Industry: {industry}"
        if industry_node_label not in node_ids:
            node = {
                "id": str(node_id_counter),
                "position": {"x": 0, "y": 0},
                "data": {"label": industry_node_label}
            }
            nodes.append(node)
            node_ids[industry_node_label] = str(node_id_counter)
            node_id_counter += 1

        edge_id = f"e{product_node['id']}-{node_ids[industry_node_label]}"
        edges.append({
            "id": edge_id,
            "source": product_node['id'],
            "target": node_ids[industry_node_label],
            "value": None,
            "tradeType": "industry"
        })

    return node_id_counter

def add_tariff_nodes(nodes, edges, node_ids, node_id_counter):
    tariffs = [
        {"name": "US Steel Tariff (25%)", "percentage": 25},
        {"name": "EU Aluminum Tariff (10%)", "percentage": 10},
        {"name": "China Import Tariff on Automobiles (15%)", "percentage": 15},
        {"name": "India Import Tariff on Electronics (20%)", "percentage": 20},
        {"name": "Japan Import Tariff on Agricultural Products (12%)", "percentage": 12}
    ]    
    tariff_nodes = []

    for tariff in tariffs:
        tariff_node_label = tariff['name']
        tariff_percentage = tariff['percentage']
        tariff_node_id = f"tariff_{node_id_counter}"
        # Add tariff node
        node = {
            "id": tariff_node_id,
            "position": {"x": 0, "y": 0},
            "data": {"label": tariff_node_label}
        }
        nodes.append(node)
        node_ids[tariff_node_label] = tariff_node_id
        node_id_counter += 1

    product_nodes = [node for node in nodes if 'product_label' in node['data']]
    country_nodes = [node for node in nodes if node['data']['label'] != "USA" and 'product_label' not in node['data'] and not node['data']['label'].startswith("Industry:") and not node['data']['label'].startswith("Policy:") and not node['data']['label'].startswith("Tariff")]

    for tariff_node_id, tariff_node_label in tariff_nodes:
        num_products = random.randint(1, len(product_nodes))
        selected_products = random.sample(product_nodes, num_products)
        for product_node in selected_products:
            edge_id = f"e{tariff_node_id}-{product_node['id']}"
            edges.append({
                "id": edge_id,
                "source": tariff_node_id,
                "target": product_node['id'],
                "value": float(tariff_node_label.split()[1].strip('%')),
                "tradeType": "tariff"
            })

        num_countries = random.randint(1, len(country_nodes))
        selected_countries = random.sample(country_nodes, num_countries)
        for country_node in selected_countries:
            edge_id = f"e{tariff_node_id}-{country_node['id']}"
            edges.append({
                "id": edge_id,
                "source": tariff_node_id,
                "target": country_node['id'],
                "value": None,
                "tradeType": "tariff"
            })

    return node_id_counter

def add_policy_nodes(nodes, edges, node_ids, node_id_counter):
    policies = [
        "NAFTA (North American Free Trade Agreement)",
        "Paris Climate Agreement",
        "Common Agricultural Policy (EU)",
        "Sanctions on Iran",
        "Corporate Tax Reform Act (USA)",
        "Fair Labor Standards Act (USA)",
        "R&D Tax Credit (USA)",
        "Generalized System of Preferences (GSP)",
        "World Trade Organization (WTO) Trade Facilitation Agreement",
        "Digital Services Tax (EU)"
    ]

    policy_nodes = []
    for policy in policies:
        policy_node_label = f"Policy: {policy}"
        policy_node_id = f"policy_{node_id_counter}"
        node = {
            "id": policy_node_id,
            "position": {"x": 0, "y": 0},
            "data": {"label": policy_node_label}
        }
        nodes.append(node)
        node_ids[policy_node_label] = policy_node_id
        node_id_counter += 1
        policy_nodes.append((policy_node_id, policy_node_label))

    industry_nodes = [node for node in nodes if node['data']['label'].startswith("Industry:")]
    country_nodes = [node for node in nodes if node['data']['label'] != "USA" and 'product_label' not in node['data'] and not node['data']['label'].startswith("Industry:") and not node['data']['label'].startswith("Policy:") and not node['data']['label'].startswith("Tariff")]

    for policy_node_id, policy_node_label in policy_nodes:
        if industry_nodes:
            num_industries = random.randint(1, len(industry_nodes))
            selected_industries = random.sample(industry_nodes, num_industries)
            for industry_node in selected_industries:
                edge_id = f"e{policy_node_id}-{industry_node['id']}"
                edges.append({
                    "id": edge_id,
                    "source": policy_node_id,
                    "target": industry_node['id'],
                    "value": None,
                    "tradeType": "policy"
                })

        if country_nodes:
            num_countries = random.randint(1, len(country_nodes))
            selected_countries = random.sample(country_nodes, num_countries)
            for country_node in selected_countries:
                edge_id = f"e{policy_node_id}-{country_node['id']}"
                edges.append({
                    "id": edge_id,
                    "source": policy_node_id,
                    "target": country_node['id'],
                    "value": None,
                    "tradeType": "policy"
                })

    return node_id_counter

def assign_positions(nodes):
    num_nodes = len(nodes)
    radius = 500
    center_x = 0
    center_y = 0
    angle_step = (2 * math.pi) / num_nodes

    for index, node in enumerate(nodes):
        angle = index * angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        node['position'] = {'x': x, 'y': y}

if __name__ == "__main__":
    import_csv_file = 'data/imports/usa/combined_import.csv' 
    export_csv_file = 'data/exports/usa/combined_export.csv'
    output_nodes_file = 'nodes.json'
    output_edges_file = 'edges.json'
    generate_graph_data(import_csv_file, export_csv_file, output_nodes_file, output_edges_file)
