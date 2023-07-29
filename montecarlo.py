import pandas as pd
import numpy as np
from pulp import *
import random
import matplotlib.pyplot as plt
def montecarlo():
    random.seed(1447)
    # Import Costs
    manvar_costs = pd.read_excel('./data/variable costs.xlsx', index_col=0)
    # Import Costs
    freight_costs = pd.read_excel('./data/freight costs.xlsx', index_col=0)
    # Factory + Freight Variable Costs
    var_cost = freight_costs / 1000 + manvar_costs
    # Factory Fixed Costs
    fixed_costs = pd.read_excel('./data/fixed cost.xlsx', index_col=0)
    # Two types of plants: Low Capacity and High Capacity Plant
    cap = pd.read_excel('./data/capacity.xlsx', index_col=0)
    # Demand by Market
    demand = pd.read_excel('./data/demand.xlsx', index_col=0)
    # Define Decision Variables
    loc = ['USA', 'GERMANY', 'JAPAN', 'BRAZIL', 'INDIA']
    size = ['LOW', 'HIGH']
    plant_name = [(i, s) for s in size for i in loc]
    prod_name = [(i, j) for i in loc for j in loc]

    # Initialize Class
    model = LpProblem("Capacitated Plant Location Model", LpMinimize)

    # Create Decision Variables
    x = LpVariable.dicts("production_", prod_name,
                         lowBound=0, upBound=None, cat='continuous')
    y = LpVariable.dicts("plant_",
                         plant_name, cat='Binary')

    # Define Objective Function
    model += (lpSum([fixed_costs.loc[i, s] * y[(i, s)] * 1000 for s in size for i in loc])
              + lpSum([var_cost.loc[i, j] * x[(i, j)] for i in loc for j in loc]))

    # Add Constraints
    for j in loc:
        model += lpSum([x[(i, j)] for i in loc]) == demand.loc[j, 'Demand']
    for i in loc:
        model += lpSum([x[(i, j)] for j in loc]) <= lpSum([cap.loc[i, s] * y[(i, s)] * 1000
                                                           for s in size])

    # Solve Model
    model.solve()

    # Results Plant (Boolean)
    df_bool = pd.DataFrame(data=[y[plant_name[i]].varValue for i in range(len(plant_name))],
                           index=[i + '-' + s for s in size for i in loc],
                           columns=['Plant Opening'])
    print(df_bool)
    dfi.export(df_bool, "../app/src/image/stage1.png", table_conversion="matplotlib")

    def optimization_model(fixed_costs, var_cost, demand, demand_col, cap):
        '''Build the optimization based on input parameters'''
        # Define Decision Variables
        loc = ['USA', 'GERMANY', 'JAPAN', 'BRAZIL', 'INDIA']
        size = ['LOW', 'HIGH']
        plant_name = [(i, s) for s in size for i in loc]
        prod_name = [(i, j) for i in loc for j in loc]

        # Initialize Class
        model = LpProblem("Capacitated Plant Location Model", LpMinimize)

        # Create Decision Variables
        x = LpVariable.dicts("production_", prod_name,
                             lowBound=0, upBound=None, cat='continuous')
        y = LpVariable.dicts("plant_",
                             plant_name, cat='Binary')

        # Define Objective Function
        model += (lpSum([fixed_costs.loc[i, s] * y[(i, s)] * 1000 for s in size for i in loc])
                  + lpSum([var_cost.loc[i, j] * x[(i, j)] for i in loc for j in loc]))

        # Add Constraints
        for j in loc:
            model += lpSum([x[(i, j)] for i in loc]) == demand.loc[j, demand_col]
        for i in loc:
            model += lpSum([x[(i, j)] for j in loc]) <= lpSum([cap.loc[i, s] * y[(i, s)] * 1000
                                                               for s in size])
        # Solve Model
        model.solve()

        # Results
        status_out = LpStatus[model.status]
        objective_out = pulp.value(model.objective)
        plant_bool = [y[plant_name[i]].varValue for i in range(len(plant_name))]
        fix = sum([fixed_costs.loc[i, s] * y[(i, s)].varValue * 1000 for s in size for i in loc])
        var = sum([var_cost.loc[i, j] * x[(i, j)].varValue for i in loc for j in loc])
        plant_prod = [x[prod_name[i]].varValue for i in range(len(prod_name))]
        return status_out, objective_out, y, x, fix, var

    # Normal Distribution
    N = 50
    df_demand = pd.DataFrame({'scenario': np.array(range(1, N + 1))})
    data = demand.reset_index()
    # Demand
    CV = 0.5
    markets = data['(Units/month)'].values
    for col, value in zip(markets, data['Demand'].values):
        sigma = CV * value
        df_demand[col] = np.random.normal(value, sigma, N)
        df_demand[col] = df_demand[col].apply(lambda t: t if t >= 0 else 0)

    # Add Initial Scenario
    COLS = ['scenario'] + list(demand.index)
    VALS = [0] + list(demand['Demand'].values)
    df_init = pd.DataFrame(dict(zip(COLS, VALS)), index=[0])

    # Concat
    df_demand = pd.concat([df_init, df_demand])
    df_demand.to_excel('./data/stage2.xlsx')
    figure, axes = plt.subplots(len(markets), 1)
    colors = ['tab:green', 'tab:red', 'black', 'tab:blue', 'tab:orange']
    for i in range(len(markets)):
        df_demand.plot(figsize=(20, 12), xlim=[0, N], x='scenario', y=markets[i], ax=axes[i], grid=True,
                       color=colors[i])
        axes[i].axhline(df_demand[markets[i]].values[0], color=colors[i], linestyle="--")
    plt.xlabel('Scenario')
    plt.ylabel('(Units)')
    plt.xticks(rotation=90)
    plt.savefig('../app/src/image/stage3.png')
    # Record results per scenario
    list_scenario, list_status, list_results, list_totald, list_fixcost, list_varcost = [], [], [], [], [], []
    # Initial Scenario
    status_out, objective_out, y, x, fix, var = optimization_model(fixed_costs, var_cost, demand, 'Demand', cap)

    # Add results
    list_scenario.append('INITIAL')
    total_demand = demand['Demand'].sum()
    list_totald.append(total_demand)
    list_status.append(status_out)
    list_results.append(objective_out)
    list_fixcost.append(fix)
    list_varcost.append(var)
    # Dataframe to record the solutions
    df_bool = pd.DataFrame(data=[y[plant_name[i]].varValue for i in range(len(plant_name))],
                           index=[i + '-' + s for s in size for i in loc],
                           columns=['INITIAL'])
    dfi.export(df_bool, "../app/src/image/stage4.png", table_conversion="matplotlib")
    # Simulate all scenarios
    demand_var = df_demand.drop(['scenario'], axis=1).T

    # Loop
    for i in range(1, 50):  # 0 is the initial scenario
        # Calculations
        status_out, objective_out, y, x, fix, var = optimization_model(fixed_costs, var_cost, demand_var, i, cap)

        # Append results
        list_status.append(status_out)
        list_results.append(objective_out)
        df_bool[i] = [y[plant_name[i]].varValue for i in range(len(plant_name))]
        list_fixcost.append(fix)
        list_varcost.append(var)
        total_demand = demand_var[i].sum()
        list_totald.append(total_demand)
        list_scenario.append(i)
    # Final Results
    # Boolean
    df_bool = df_bool.astype(int)
    plt.figure(figsize=(20, 4))
    plt.pcolor(df_bool, cmap='Blues', edgecolors='k', linewidths=0.5)  #
    plt.xticks([i + 0.5 for i in range(df_bool.shape[1])], df_bool.columns, rotation=90, fontsize=12)
    plt.yticks([i + 0.5 for i in range(df_bool.shape[0])], df_bool.index, fontsize=12)
    plt.savefig('../app/src/image/stage5.png')
    # Unique combinations
    df_unique = df_bool.T.drop_duplicates().T
    df_unique.columns = ['INITIAL'] + ['C' + str(i) for i in range(1, len(df_unique.columns))]
    plt.figure(figsize=(12, 4))
    plt.pcolor(df_unique, cmap='Blues', edgecolors='k', linewidths=0.5)  #
    plt.xticks([i + 0.5 for i in range(df_unique.shape[1])], df_unique.columns, rotation=90, fontsize=12)
    plt.yticks([i + 0.5 for i in range(df_unique.shape[0])], df_unique.index, fontsize=12)
    plt.savefig("../app/src/image/stage6.png")
    # Number of columns
    COL_NAME, COL_NUMBER = [], []
    for col1 in df_unique.columns:
        count = 0
        COL_NAME.append(col1)
        for col2 in df_bool.columns:
            if (df_bool[col2] != df_unique[col1]).sum() == 0:
                count += 1
        COL_NUMBER.append(count)
    df_comb = pd.DataFrame({'column': COL_NAME, 'count': COL_NUMBER})
    my_circle = plt.Circle((0, 0), 0.8, color='white')
    df_comb.plot.pie(figsize=(8, 8), x='column', y='count', legend=False, pctdistance=0.7,
                     autopct='%1.0f%%', labeldistance=1.05,
                     wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
    plt.xlabel('Business Vertical')
    # plt.title('{:.2f} M€ Budget Applications in 9 Vertical Markets'.format(df_p['TOTAL'].sum()/1e6))
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.axis('off')
    plt.savefig('../app/src/image/stage7.png')


montecarlo()