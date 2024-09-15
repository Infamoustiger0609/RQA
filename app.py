import streamlit as st
import json

# Load predefined queries from JSON file
with open('queries.json', 'r') as file:
    predefined_queries = json.load(file)

def execute_query(query):
    if query in predefined_queries:
        return predefined_queries[query]
    else:
        return {
            "error": "Query not recognized. Please try one of the predefined queries.",
            "availableQueries": list(predefined_queries.keys())
        }

# Streamlit app
st.title('Retail Query Assistant')

query_input = st.text_input('Enter your query:', '')

if st.button('Submit'):
    if query_input:
        result = execute_query(query_input.lower())
        
        if 'error' in result:
            st.error(result['error'])
            st.write('Available queries:')
            st.write(result['availableQueries'])
        else:
            st.subheader('SQL Query:')
            st.code(result['sql'])
            st.subheader('Result:')
            st.json(result['result'])
    else:
        st.warning('Please enter a query.')
