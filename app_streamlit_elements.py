import streamlit as st
from streamlit_elements import Elements

# Create a new element context
mt = Elements()

# Example taken from https://material-ui.com/components/data-grid/

cols = [
    { "field": 'id', "headerName": 'ID', "width": 70 },
    { "field": 'firstName', "headerName": 'First name', "width": 130 },
    { "field": 'lastName', "headerName": 'Last name', "width": 130 },
    { "field": 'age', "headerName": 'Age', "type": 'number', "width": 90 },
    {
        "field": 'fullName',
        "headerName": 'Full name',
        "description": 'This column has a value getter and is not sortable.',
        "sortable": False,
        "width": 160,
        "valueGetter": lambda params: (params.getValue("firstName") | "") + " " + (params.getValue("lastName") | "")
    },
]

rows = [
    { "id": 1, "lastName": "Snow", "firstName": "Jon", "age": 35 },
    { "id": 2, "lastName": "Lannister", "firstName": "Cersei", "age": 42 },
    { "id": 3, "lastName": "Lannister", "firstName": "Jaime", "age": 45 },
    { "id": 4, "lastName": "Stark", "firstName": "Arya", "age": 16 },
    { "id": 5, "lastName": "Targaryen", "firstName": "Daenerys", "age": None },
    { "id": 6, "lastName": "Melisandre", "firstName": None, "age": 150 },
    { "id": 7, "lastName": "Clifford", "firstName": "Ferrara", "age": 44 },
    { "id": 8, "lastName": "Frances", "firstName": "Rossini", "age": 36 },
    { "id": 9, "lastName": "Roxie", "firstName": "Harvey", "age": 65 },
]

mt.default_state(selection=[])

with mt.html.div(style={"height": 400, "width": "100%"}):
    mt.data_grid(
        rows=rows,
        columns=cols,
        page_size=5, 
        checkbox_selection=True,
        on_selection_change=lambda new_select: mt.state.selection.set(new_select.rowIds)
    )

mt.on_change(mt.submit)
ret = mt.show("material-ui")

st.write(ret.state.selection)