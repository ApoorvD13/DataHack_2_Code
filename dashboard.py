# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd

# # Your list of cities
# cities = [
#     "hyderabad", "delhi", "delhi", "kolkata", "bangalore", "bangalore", "hyderabad", "kolkata",
#     "hyderabad", "chennai", "bangalore", "kolkata", "kolkata", "hyderabad", "delhi", "kolkata",
#     "hyderabad", "mumbai", "delhi", "chennai", "chennai", "bangalore", "mumbai", "hyderabad",
#     "delhi", "delhi", "kolkata", "chennai", "kolkata", "kolkata", "hyderabad", "kolkata",
#     "hyderabad", "hyderabad", "mumbai", "mumbai", "chennai", "hyderabad", "mumbai", "delhi",
#     "kolkata", "kolkata", "hyderabad", "chennai", "kolkata", "hyderabad", "hyderabad", "kolkata",
#     "chennai", "hyderabad", "hyderabad", "delhi", "kolkata", "kolkata", "kolkata", "hyderabad",
#     "hyderabad", "hyderabad", "hyderabad", "hyderabad", "chennai", "hyderabad", "chennai",
#     "bangalore", "kolkata", "bangalore", "mumbai", "kolkata", "hyderabad", "hyderabad", "hyderabad",
#     "hyderabad", "delhi", "bangalore", "kolkata", "hyderabad", "bangalore", "chennai", "kolkata",
#     "hyderabad", "hyderabad", "mumbai", "kolkata", "mumbai", "chennai", "hyderabad", "hyderabad",
#     "mumbai", "kolkata", "kolkata", "hyderabad", "hyderabad", "chennai", "kolkata", "hyderabad",
#     "hyderabad", "hyderabad", "chennai", "hyderabad", "mumbai", "kolkata", "chennai", "kolkata",
#     "kolkata", "delhi", "delhi", "bangalore", "chennai", "hyderabad", "bangalore", "mumbai",
#     "bangalore", "hyderabad", "delhi", "delhi", "kolkata", "chennai", "kolkata", "kolkata",
#     "hyderabad", "hyderabad", "hyderabad", "mumbai", "chennai", "delhi", "chennai", "hyderabad",
#     "mumbai", "chennai", "chennai", "kolkata", "chennai", "kolkata", "hyderabad", "mumbai",
#     "kolkata", "chennai", "kolkata", "kolkata", "delhi", "delhi", "delhi", "delhi", "bangalore",
#     "bangalore", "hyderabad", "mumbai", "bangalore", "delhi", "delhi", "chennai", "kolkata",
#     "mumbai", "bangalore", "kolkata", "kolkata", "hyderabad", "bangalore", "bangalore", "bangalore",
#     "bangalore", "delhi", "kolkata", "kolkata", "delhi", "kolkata", "bangalore", "mumbai",
#     "hyderabad", "hyderabad", "kolkata", "mumbai", "hyderabad", "mumbai", "chennai", "kolkata",
#     "delhi", "delhi", "mumbai", "kolkata", "bangalore", "delhi", "bangalore"
# ]

# # Create a DataFrame from the list of cities
# df_cities = pd.DataFrame(cities, columns=["City"])

# df_laws = pd.DataFrame(data, columns=["Rating", "Laws"])

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div([
#     html.H1("City Distribution Pie Chart"),
#     dcc.Graph(id='city-pie-chart'),

#     html.H1("Rating Distribution by Laws"),
#     dcc.Graph(id='law-bar-chart')
# ])

# # Callback to update the pie chart
# @app.callback(
#     Output('city-pie-chart', 'figure'),
#     Input('city-pie-chart', 'relayoutData')
# )
# def update_pie_chart(relayoutData):
#     # Create a pie chart
#     fig = px.pie(df_cities, names='City', title='City Distribution')
#     return fig

# # Callback to update the bar chart
# @app.callback(
#     Output('law-bar-chart', 'figure'),
#     Input('law-bar-chart', 'relayoutData')
# )
# def update_bar_chart(relayoutData):
#     # Create a bar chart
#     fig = px.bar(df_laws, x='Laws', y='Rating', title='Rating Distribution by Laws')
#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)










import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import random  # Import the random module for generating sample data



# Your dataset for the pie chart
cities = [
    "hyderabad", "delhi", "delhi", "kolkata", "bangalore", "bangalore", "hyderabad", "kolkata",
    "hyderabad", "chennai", "bangalore", "kolkata", "kolkata", "hyderabad", "delhi", "kolkata",
    "hyderabad", "mumbai", "delhi", "chennai", "chennai", "bangalore", "mumbai", "hyderabad",
    "delhi", "delhi", "kolkata", "chennai", "kolkata", "kolkata", "hyderabad", "kolkata",
    "hyderabad", "hyderabad", "mumbai", "mumbai", "chennai", "hyderabad", "mumbai", "delhi",
    "kolkata", "kolkata", "hyderabad", "chennai", "kolkata", "hyderabad", "hyderabad", "kolkata",
    "chennai", "hyderabad", "hyderabad", "delhi", "kolkata", "kolkata", "kolkata", "hyderabad",
    "hyderabad", "hyderabad", "hyderabad", "hyderabad", "chennai", "hyderabad", "chennai",
    "bangalore", "kolkata", "bangalore", "mumbai", "kolkata", "hyderabad", "hyderabad", "hyderabad",
    "hyderabad", "delhi", "bangalore", "kolkata", "hyderabad", "bangalore", "chennai", "kolkata",
    "hyderabad", "hyderabad", "mumbai", "kolkata", "mumbai", "chennai", "hyderabad", "hyderabad",
    "mumbai", "kolkata", "kolkata", "hyderabad", "hyderabad", "chennai", "kolkata", "hyderabad",
    "hyderabad", "hyderabad", "chennai", "hyderabad", "mumbai", "kolkata", "chennai", "kolkata",
    "kolkata", "delhi", "delhi", "bangalore", "chennai", "hyderabad", "bangalore", "mumbai",
    "bangalore", "hyderabad", "delhi", "delhi", "kolkata", "chennai", "kolkata", "kolkata",
    "hyderabad", "hyderabad", "hyderabad", "mumbai", "chennai", "delhi", "chennai", "hyderabad",
    "mumbai", "chennai", "chennai", "kolkata", "chennai", "kolkata", "hyderabad", "mumbai",
    "kolkata", "chennai", "kolkata", "kolkata", "delhi", "delhi", "delhi", "delhi", "bangalore",
    "bangalore", "hyderabad", "mumbai", "bangalore", "delhi", "delhi", "chennai", "kolkata",
    "mumbai", "bangalore", "kolkata", "kolkata", "hyderabad", "bangalore", "bangalore", "bangalore",
    "bangalore", "delhi", "kolkata", "kolkata", "delhi", "kolkata", "bangalore", "mumbai",
    "hyderabad", "hyderabad", "kolkata", "mumbai", "hyderabad", "mumbai", "chennai", "kolkata",
    "delhi", "delhi", "mumbai", "kolkata", "bangalore", "delhi", "bangalore"
]

# Create a DataFrame from the list of cities
df_cities = pd.DataFrame(cities, columns=["City"])

# Your dataset for the bar chart
data = [
    (5, "Corporate Law, Consumer Protection Law, Labor Law"),
    (2, "Intellectual Property Law, Criminal Law, Tax Law"),
    (5, "Human Rights Law, Civil Law, Family Law"),
    # ... (paste the entire dataset here)
]

# Create a DataFrame from the dataset
df_laws = pd.DataFrame(data, columns=["Rating", "Laws"])

# Your dataset for the bar chart

data = [
    (5, "Corporate Law, Consumer Protection Law, Labor Law"),
    (2, "Intellectual Property Law, Criminal Law, Tax Law"),
    (5, "Human Rights Law, Civil Law, Family Law"),
    (2, "Constitutional Law, Media and Entertainment Law, Real Estate Law"),
    (2, "Human Rights Law, Constitutional Law"),
    (2, "Medical Law, Immigration Law, Constitutional Law"),
    (4, "Labor Law, Media and Entertainment Law, Civil Law"),
    (4, "Labor Law, Consumer Protection Law, Criminal Law"),
    (5, ""),
    (0, "Banking and Finance Law, Environmental Law, Civil Law"),
    (5, "Immigration Law, Medical Law"),
    (4, "Family Law, Real Estate Law, Media and Entertainment Law"),
    (1, "Environmental Law, Banking and Finance Law, Real Estate Law"),
    (1, "Labor Law, Intellectual Property Law, Medical Law"),
    (5, "Constitutional Law, Banking and Finance Law, Media and Entertainment Law"),
    (4, "Corporate Law, Intellectual Property Law, Medical Law"),
    (4, "Environmental Law, Corporate Law, Criminal Law"),
    (2, "Consumer Protection Law, Media and Entertainment Law, Labor Law"),
    (3, "Human Rights Law, Labor Law, Banking and Finance Law"),
    (0, "Labor Law, Consumer Protection Law, Immigration Law"),
    (0, "Corporate Law, Environmental Law"),
    (3, "Labor Law, Banking, Finance Law, Media and Entertainment Law"),
    (5, "Family Law, Civil Law"),
    (4, "Consumer Protection Law, Media and Entertainment Law, Constitutional Law"),
    (5, "Tax Law, Criminal Law, Environmental Law"),
    (3, "Labor Law, Medical Law, Human Rights Law"),
    (4, "Medical Law, Human Rights Law, Family Law"),
    (1, "Constitutional Law, Civil Law, Corporate Law"),
    (5, "Labor Law, Immigration Law, Banking and Finance Law"),
    (0, "Immigration Law, Tax Law"),
    (4, "Environmental Law, Banking and Finance Law, Criminal Law"),
    (5, "Immigration Law, Environmental Law, Civil Law"),
    (5, "Tax Law, Criminal Law, Media and Entertainment Law"),
    (3, "Family Law, Criminal Law, Civil Law"),
    (2, "Human Rights Law, Medical Law, Media and Entertainment Law"),
    (4, "Immigration Law, Real Estate Law, Criminal Law"),
    (5, ""),
    (0, "Family Law, Constitutional Law, Labor Law"),
    (5, "Immigration Law, Intellectual Property Law, Family Law"),
    (5, "Human Rights Law, Consumer Protection Law, Banking and Finance Law"),
    (3, "Media and Entertainment Law, Labor Law, Corporate Law"),
    (2, "Real Estate Law, Medical Law, Tax Law"),
    (4, "Criminal Law, Medical Law, Immigration Law"),
    (5, "Corporate Law, Labor Law"),
    (5, "Criminal Law, Banking and Finance Law, Real Estate Law"),
    (1, "Consumer Protection Law, Family Law, Criminal Law"),
    (4, "Environmental Law, Tax Law, Real Estate Law"),
    (0, "Medical Law, Criminal Law, Intellectual Property Law"),
    (4, "Immigration Law, Family Law"),
    (2, "Real Estate Law, Immigration Law, Banking and Finance Law"),
    (5, "Media and Entertainment Law, Real Estate Law, Human Rights Law"),
    (5, "Civil Law, Real Estate Law, Criminal Law"),
    (5, "Immigration Law, Labor Law, Real Estate Law"),
    (5, "Tax Law, Environmental Law, Intellectual Property Law"),
    (5, "Banking and Finance Law, Constitutional Law, Human Rights Law"),
    (5, "Real Estate Law, Intellectual Property Law, Medical Law"),
    (1, "Family Law, Criminal Law, Tax Law"),
    (0, "Real Estate Law, Family Law, Tax Law"),
    (5, "Media and Entertainment Law, Intellectual Property Law, Banking and Finance Law"),
    (3, "Consumer Protection Law, Environmental Law, Real Estate Law"),
    (5, "Family Law, Medical Law"),
    (4, "Constitutional Law, Medical Law, Banking and Finance Law"),
    (5, "Corporate Law, Media and Entertainment Law, Labor Law"),
    (2, "Labor Law, Human Rights Law, Immigration Law"),
    (1, "Human Rights Law, Tax Law, Constitutional Law"),
    (4, "Real Estate Law, Immigration Law, Labor Law"),
    (4, "Human Rights Law, Banking and Finance Law, Tax Law"),
    (0, "Intellectual Property Law, Immigration Law"),
    (5, "Tax Law, Intellectual Property Law, Banking and Finance Law"),
    (1, "Immigration Law, Intellectual Property Law, Criminal Law"),
    (4, "Tax Law, Banking, Finance Law, Environmental Law"),
    (4, "Human Rights Law, Intellectual Property Law, Media and Entertainment Law"),
    (2, "Immigration Law, Environmental Law, Civil Law"),
    (5, "Tax Law, Criminal Law, Media and Entertainment Law"),
    (5, "Family Law, Criminal Law, Civil Law"),
    (5, "Human Rights Law, Medical Law, Media and Entertainment Law"),
    (5, "Immigration Law, Real Estate Law, Criminal Law"),
    (5, "Immigration Law, Intellectual Property Law"),
    (5, "Family Law, Constitutional Law, Labor Law"),
    (1, "Immigration Law, Intellectual Property Law, Family Law"),
    (0, "Human Rights Law, Consumer Protection Law, Banking and Finance Law"),
    (5, "Media and Entertainment Law, Labor Law, Corporate Law"),
    (2, "Real Estate Law, Medical Law, Tax Law"),
    (5, "Criminal Law, Medical Law, Immigration Law"),
    (4, "Corporate Law, Labor Law"),
    (5, "Criminal Law, Banking and Finance Law, Real Estate Law"),
    (5, "Consumer Protection Law, Family Law, Criminal Law"),
    (3, "Environmental Law, Tax Law, Real Estate Law"),
    (1, "Medical Law, Criminal Law, Intellectual Property Law"),
    (5, "Immigration Law, Family Law"),
    (0, "Real Estate Law, Immigration Law, Banking and Finance Law"),
    (5, "Media and Entertainment Law, Real Estate Law, Human Rights Law"),
    (2, "Civil Law, Real Estate Law, Criminal Law"),
    (2, "Immigration Law, Labor Law, Real Estate Law"),
    (4, "Tax Law, Environmental Law, Intellectual Property Law"),
    (3, "Banking and Finance Law, Constitutional Law, Human Rights Law"),
    (4, "Real Estate Law, Intellectual Property Law, Medical Law"),
    (5, "Family Law, Criminal Law, Tax Law"),
    (1, "Real Estate Law, Family Law, Tax Law"),
    (4, "Media and Entertainment Law, Intellectual Property Law, Banking and Finance Law"),
    (0, "Consumer Protection Law, Environmental Law, Real Estate Law"),
    (4, "Family Law, Medical Law"),
    (2, "Constitutional Law, Medical Law, Banking and Finance Law"),
    (5, "Intellectual Property Law, Civil Law, Immigration Law"),
    (5, "Immigration Law, Corporate Law, Consumer Protection Law"),
    (5, "Malayalam"),
    (5, "Intellectual Property Law, Tax Law, Real Estate Law"),
    (5, "Medical Law, Family Law, Intellectual Property Law"),
    (5, "Family Law, Media and Entertainment Law, Criminal Law"),
    (1, "Criminal Law, Human Rights Law, Tax Law"),
    (0, "Civil Law, Corporate Law, Real Estate Law"),
    (5, "Civil Law, Tax Law, Intellectual Property Law"),
    (3, "Tax Law, Criminal Law, Labor Law"),
    (5, "Environmental Law, Immigration Law, Banking and Finance Law"),
    (4, "Tax Law, Banking and Finance Law, Environmental Law"),
    (5, "Banking and Finance Law, Medical Law, Media and Entertainment Law"),
    (1, "Family Law, Consumer Protection Law, Environmental Law"),
    (3, "Family Law, Immigration Law, Human Rights Law"),
    (3, "Criminal Law, Consumer Protection Law, Family Law"),
    (2, "Tax Law, Environmental Law"),
    (5, "Constitutional Law, Civil Law"),
    (1, "Medical Law, Real Estate Law, Intellectual Property Law"),
    (2, "Constitutional Law, Corporate Law, Family Law"),
    (4, "Criminal Law, Constitutional Law"),
    (0, "Consumer Protection Law, Civil Law"),
    (1, "Environmental Law, Medical Law"),
    (3, "Empty"),
    (1, "Labor Law, Human Rights Law, Consumer Protection Law"),
    (3, "Banking and Finance Law, Corporate Law, Immigration Law"),
    (5, "Real Estate Law, Human Rights Law, Civil Law"),
    (3, "Criminal Law, Medical Law, Labor Law"),
    (4, "Criminal Law, Family Law, Environmental Law"),
    (3, "Corporate Law, Environmental Law, Medical Law"),
    (4, "Medical Law, Real Estate Law, Labor Law"),
    (0, "Banking and Finance Law, Human Rights Law, Intellectual Property Law"),
    (5, "Immigration Law, Criminal Law, Tax Law"),
    (1, "Media and Entertainment Law, Corporate Law, Intellectual Property Law"),
    (4, "Immigration Law, Consumer Protection Law, Corporate Law"),
    (4, "Labor Law, Family Law, Criminal Law"),
    (2, "Tax Law, Constitutional Law, Media and Entertainment Law"),
    (2, "Banking and Finance Law, Intellectual Property Law, Civil Law"),
    (2, "Consumer Protection Law, Labor Law, Real Estate Law"),
    (0, "Family Law, Constitutional Law, Criminal Law"),
    (3, "Family Law, Tax Law, Medical Law"),
    (5, "Media and Entertainment Law, Corporate Law, Constitutional Law"),
    (1, "Intellectual Property Law, Immigration Law, Consumer Protection Law"),
    (1, "Medical Law, Civil Law, Intellectual Property Law"),
    (5, "Labor Law, Immigration Law, Intellectual Property Law"),
    (5, "Criminal Law, Constitutional Law, Family Law"),
    (4, "Labor Law, Consumer Protection Law, Medical Law"),
    (3, "Labor Law, Immigration Law, Criminal Law"),
    (1, "Media and Entertainment Law, Criminal Law, Human Rights Law"),
    (5, "Human Rights Law, Immigration Law, Banking and Finance Law"),
    (1, "Labor Law, Real Estate Law, Banking and Finance Law"),
    (0, "Immigration Law, Intellectual Property Law, Family Law"),
    (2, "Human Rights Law, Corporate Law, Real Estate Law"),
    (1, "Medical Law, Family Law"),
    (2, "Labor Law, Media and Entertainment Law"),
    (5, "Environmental Law, Criminal Law"),
    (5, "Real Estate Law, Immigration Law, Civil Law"),
    (1, "Family Law, Environmental Law"),
    (3, "Human Rights Law, Environmental Law"),
    (0, "Intellectual Property Law, Medical Law"),
    (1, "Banking and Finance Law, Human Rights Law, Consumer Protection Law"),
    (5, "Real Estate Law, Medical Law, Constitutional Law"),
    (1, "Empty"),
    (5, "Corporate Law, Intellectual Property Law, Real Estate Law"),
    (4, "Intellectual Property Law, Immigration Law, Banking and Finance Law"),
    (5, "Family Law, Intellectual Property Law"),
    (5, "Family Law, Environmental Law, Corporate Law"),
    (0, "Human Rights Law, Civil Law, Consumer Protection Law"),
    (3, "Labor Law, Consumer Protection Law, Constitutional Law"),
    (0, "Civil Law, Immigration Law, Tax Law"),
    (2, "Corporate Law, Criminal Law, Banking and Finance Law"),
    (2, "Human Rights Law, Constitutional Law"),
    (1, "Environmental Law, Real Estate Law, Human Rights Law"),
    (3, "Criminal Law, Labor Law, Family Law"),
    (1, "Constitutional Law, Banking and Finance Law, Immigration Law"),
    (2, "Banking and Finance Law, Tax Law, Criminal Law"),
    (2, "Intellectual Property Law, Consumer Protection Law"),
    (4, "Civil Law, Intellectual Property Law, Family Law"),
    (5, "Labor Law, Criminal Law, Real Estate")
]

df_laws = pd.DataFrame(data, columns=["Rating", "Laws"])

cost_rating_data = {
    'Cost': [
         421, 436, 237, 90, 247, 154, 181, 398, 84, 422, 242, 0, 90, 202, 90, 483, 413, 257, 151,
        470, 205, 122, 303, 0, 52, 157, 472, 127, 101, 307, 438, 255, 0, 255, 459, 97, 374, 359,
        93, 0, 306, 214, 390, 166, 362, 68, 428, 252, 337, 150, 144, 255, 459, 97, 374, 359, 93,
        465, 306, 214, 390, 166, 362, 68, 428, 252, 337, 150, 355, 398, 263, 328, 255, 452, 274,
        429, 411, 235, 154, 233, 422, 152, 286, 413, 209, 339, 161, 99, 407, 95, 172, 144, 255,
        459, 97, 374, 359, 93, 465, 306, 214, 390, 166, 362, 68, 428, 252, 337, 150, 355, 398, 263,
        328, 256, 452, 274, 429, 411, 235, 154, 233, 422, 152, 286, 414, 243, 129, 494, 303, 359,
        196, 0, 489, 179, 241, 342, 61, 415, 291, 175, 78, 123, 453, 359, 308, 232, 214, 148, 351,
        487, 129, 319, 251, 164, 421, 268, 295, 187, 132, 89, 371, 138, 361, 226, 237, 261, 215,
        95, 189, 349, 350, 179, 257, 137, 145, 60, 454, 145, 152, 176, 107, 338, 84
    ],
    'Rating': [
        5, 2, 5, 2, 2, 2, 4, 4, 5, 0, 5, 4, 1, 1, 5, 4, 4, 2, 3, 0, 0, 3, 5, 4, 5, 3, 4,
        1, 5, 0, 4, 5, 5, 3, 2, 5, 3, 4, 0, 5, 5, 5, 4, 5, 1, 4, 0, 4, 2, 5, 5, 5, 5, 5,
        5, 1, 0, 5, 4, 1, 4, 1, 2, 4, 3, 5, 4, 3, 5, 1, 2, 2, 2, 4, 5, 0, 5, 4, 3, 5, 3,
        5, 5, 1, 3, 5, 5, 5, 0, 4, 5, 4, 3, 4, 5, 5, 1, 2, 0, 1, 5, 1, 5, 4, 5, 0, 4, 4,
        2, 2, 2, 0, 3, 5, 1, 5, 5, 4, 3, 1, 5, 1, 2, 2, 4, 0, 1, 3, 1, 3, 4, 1, 5, 1, 2,
        0, 5, 0, 1, 2, 5, 5, 1, 3, 0, 1, 5, 1, 5, 4, 5, 5, 0, 3, 0, 4, 1, 4, 4, 0, 1, 4,
        3, 5, 4, 3, 2, 5, 1, 0, 5, 2, 4, 0, 4, 1, 3, 1, 5, 4, 1, 1, 4,
    ]
}

df_cost_rating = pd.DataFrame(cost_rating_data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("City Distribution Pie Chart"),
    dcc.Graph(id='city-pie-chart'),

    html.H1("Rating Distribution by Laws"),
    dcc.Graph(id='law-bar-chart'),

    html.H1("Cost vs. Rating Scatter Plot"),
    dcc.Graph(id='cost-rating-scatter')
])

# Callback to update the pie chart
@app.callback(
    Output('city-pie-chart', 'figure'),
    Input('city-pie-chart', 'relayoutData')
)
def update_pie_chart(relayoutData):
    # Create a pie chart
    fig = px.pie(df_cities, names='City', title='City Distribution')
    return fig

# Callback to update the bar chart
@app.callback(
    Output('law-bar-chart', 'figure'),
    Input('law-bar-chart', 'relayoutData')
)
def update_bar_chart(relayoutData):
    # Create a bar chart
    fig = px.bar(df_laws, x='Laws', y='Rating', title='Rating Distribution by Laws')
    return fig

# Callback to update the scatter plot
@app.callback(
    Output('cost-rating-scatter', 'figure'),
    Input('cost-rating-scatter', 'relayoutData')
)
def update_scatter_plot(relayoutData):
    # Create a scatter plot
    fig = px.scatter(df_cost_rating, x='Cost', y='Rating', title='Cost vs. Rating Scatter Plot')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


