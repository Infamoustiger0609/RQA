import streamlit as st
import json

# Load predefined queries from the JSON file
with open('queries.json', 'r') as file:
    queries = json.load(file)

# Fake database (as a dictionary)
fake_db = {
    "top-selling products": [
        {"product_name": "Laptop", "total_sales": 500},
        {"product_name": "Smartphone", "total_sales": 450},
        {"product_name": "Headphones", "total_sales": 300}
    ],
    "least-selling products": [
        {"product_name": "Tablet", "total_sales": 5},
        {"product_name": "Smartwatch", "total_sales": 10},
        {"product_name": "Bluetooth Speaker", "total_sales": 15}
    ],
    "overstocked products": [
        {"product_name": "Keyboard", "stock_quantity": 1500},
        {"product_name": "Mouse", "stock_quantity": 1200},
        {"product_name": "Monitor", "stock_quantity": 1100}
    ],
    "understocked products": [
        {"product_name": "Charger", "stock_quantity": 2},
        {"product_name": "USB Cable", "stock_quantity": 5},
        {"product_name": "Hard Drive", "stock_quantity": 8}
    ]
}

# Title of the Streamlit app
st.title('Retail Query Assistant')

# Instructions for the user
st.write('Please enter a query related to product sales and stock. You can try one of the predefined queries listed below:')

# Display predefined queries on the web page (only once, at the start)
st.write("### Predefined Queries:")
for query in queries.keys():
    st.write(f"- {query}")

# Text input for the query
user_query = st.text_input("Enter your query:")

# Button to submit the query
if st.button("Submit"):
    if user_query in queries:
        # Fetch the SQL query from predefined queries (just for display)
        sql_query = queries[user_query]

        # Display the SQL query
        st.write(f"SQL Query: {sql_query}")

        # Simulate fetching results from the fake database
        results = fake_db.get(user_query, [])

        if results:
            st.write("Results:")
            for result in results:
                st.write(result)
        else:
            st.write("No results found.")
    else:
        # Display error message
        st.write("Query not recognized. Please try again.")
