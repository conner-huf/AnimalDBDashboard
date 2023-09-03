# AnimalDBDashboard

In this project, I worked with MongoDB and python to create a module that allowed for CRUD operations on a database and created a GUI that could filter and display the data stored on the database.
I worked with the following technologies in this project:
<ul>
        Python
        Jupyter Notebook
        MongoDB
        Numpy, Pandas, and Plotly python libs
</ul>

This was my first introduction to adding UI components to database manipulation, so it was an incredible learning experience for figuring out how to add things like data tables, geolocators, data visualizations, and data filtering. I'm happy with how it turned out, and this is a great stepping stone toward figuring out how to make these types of dashboards represent data in a more aesthetically pleasing way.

![Screenshot unfiltered](https://github.com/conner-huf/CS-340/assets/126115012/8b857d6f-ff32-4da0-b3f9-154684b74fae)

^^ Above is a screenshot of the finished dashboard with no filter applied. ^^

--------------------------------------------------------------------------------------------- 

About the Project/Project Title
Provide a little information about your project or an overview that explains what the project is about.

This project aims to create a Python module that works with PyMongo to perform CRUD operation within a database in MongoDB. PyMongo is the driver used for this project. PyMongo is officially supported by the MongoDB team, which ensures that it stays up-to-date with the latest releases of MongoDB. Additionally, PyMongo offers operation that is intuitive consistent with the MongoDB syntax, which makes it an excellent choice of driver for working with MongoDB. The purpose of the project is to create a module in Python that can perform CRUD operations (Create, Read, Update, and Delete) on documents within a database. These operations are built in Python and tested using a Jupyter Notebook.

V2:
In an update, I’ve added the dashboard and filtering options to represent the data populated into the data table. The dashboard includes a data table that can be filtered, a geolocator that shows the location of the currently selected animal, and a pie chart that shows the breed distribution of the currently selected filtering option. The filtering options filter for the following criteria: unfiltered, animals best suited for disaster or individual tracking, animals best suited for mountain or wilderness rescue, and animals best suited for water rescue.

Motivation
This is a short description of the motivation behind the creation and maintenance of the project. This should explain why the project exists.

V2: This dashboard and the data visualization tools could be tweaked to represent different filtering options, or could be used as a skeletal structure to represent an entirely different data set. 

Getting Started
This is an example of how you may give instructions on setting up your project locally: “To get a local copy up and running, follow these simple example steps.”

The first thing I did to get this project going is get my data imported into MongoDB. I used a csv file and imported that into MongoDB. Once I verified that the data was uploaded correctly, I created a user for the database with readWrite permissions. I then created a Python module for performing CRUD operations within the database and a Jupyter Notebook to test the function of this module.

V2:
Nothing additional needed to get the dashboard running. As written, the jupyter notebook initiates the dashboard on a local host server, so it just opens a new tab in your browser to display the dashboard.

Installation
List the tools you need to use the software and how to install them.

To use this software you need MongoDB, a Python IDE and interpreter, and Jupyter Notebook.

V2: 
No additional software needed for the updated program.

Usage
Use this space to show useful examples of how your project works and how it can be used. Be sure to include examples of your code, tests, and screenshots.

Code Example
Show what the library does as concisely as possible. Developers should be able to figure out how your project solves their problem by looking at the code example. Make sure that your code is short and concise.

def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data) 
            return result.acknowledged # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
def read(self, query):
        cursor = self.collection.find(query)
        return list(cursor)

Above is a snippet of the code that creates a document and finds a document in the database.

def update(self, query, update_data):
       result = self.collection.update_many(query, {"$set": update_data})
       return result.modified_count

def delete(self, query):
      result = self.collection.delete_many(query)
      return result.deleted_count

Above is a snippet of the code that updates a document and deletes a document in the database.

Tests
Describe and show how to run the tests with code examples.

shelter = AnimalShelter()
data = {'animal_type': ‘Dog’,  'breed': 'Labrador',  'color': 'Yellow',}
success = shelter.create(data)
if success:
    print("Document inserted successfully.")
else:
    print("Failed to insert document.")
    
query = {'breed': 'Labrador', 'outcome_type': 'Transfer'}
results = shelter.read(query)
print(results)

 I tested the performance of these operations in Jupyter Notebook by instantiating an AnimalShelter object, using the create operation to create an object, reporting success or failure, then reading that same document, and reporting success or failure.

To test the update and delete operations, I updated the earlier created document, then used the read method to display that the document had been updated. Then I used the delete method, again using the find method to show that the document could no longer be found. Additionally, the update and delete methods return the number of modified/deleted documents.

V2:
Here is a snippet of my app layout as it’s written in the notebook file:


app.layout = html.Div([
    html.Div(id='hidden-div', style={'display': 'none'}),
    html.Center([
        html.Img(src='logo.png', alt="Grazioso Salvare Logo", style={'width': '10em'}),
        html.B(html.H1('SNHU CS-340 Dashboard - Conner Hufnagel'))
    ]),
    html.Hr(),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='filter-dropdown', #include a drop down menu, with unfiltered selected by default
                options=filter_options,
                value='unfiltered',
                clearable=False,
                style = {'width':'20em'}
            ),
            dash_table.DataTable(
                id='datatable-id',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
                ],
                data=df.to_dict('records'),
                row_selectable="single",
                selected_rows=[0],  # Select the first row by default
                page_current=0,
                page_size=20
            ),
        ]),
    ]),
    
    html.Br(),
    html.Hr(),
    html.Div([
        html.Div(
            id='map-id',
            className='col s12 m6',
            style={'width': '50%', 'display': 'inline-block'}
        ),
        html.Div(
            dcc.Graph(id='pie-chart'),
            style={'width': '50%', 'display': 'inline-block'}
        )
    ])
])


To break this down a bit, I’ve separated the dashboard into two sections, an upper section and a lower section. The upper section contains the data table and the filter options and the lower section contains the geolocation map and the pie chart. 


Note: For a reason that I can’t identify, the logo is not loading in with the pathing I’ve provided. The above code snippet shown shows the syntax “html.Img(src='logo.png', alt="Grazioso Salvare Logo", style={'width': '10em'}),” which is an example of relative pathing. This would mean that the logo is searched for within the current directory, so I placed the logo.png file with the Grazioso Slavare logo within the same directory as my notebook file and my py file and it still wouldn’t load.

Then I tried absolute pathing to the logo.png, and that didn’t work either. After troubleshooting a few different solves, I eventually added alt text because I’d reached the deadline for this project. If anyone has a possible explanation for what I could be doing wrong, please don’t hesitate to reach out. I’d love to get this fixed, even after finishing the project. I’ve included a screenshot of the directory my files are inside in the screenshots section below.


Here is a snippet of how I’m going about filtering the different options:


@app.callback(
    Output('datatable-id', 'data'),
    [Input('datatable-id', 'page_current'),
    Input('filter-dropdown', 'value')]
)
def update_table(page_current, filter_value):
    
    if filter_value == 'water_rescue': # if user selects water rescue from drop down, filter
        filtered_df = df[
            (df['breed'].isin(['Labrador Retriever Mix', 'Chesapeake Bay Retriever', 'Newfoundland'])) &
            (df['sex_upon_outcome'] == 'Intact Female') &
            (df['age_upon_outcome_in_weeks'].between(26, 156))
        ]
    elif filter_value == 'mountain_rescue': # else, if user selects mountain rescue, filter
        filtered_df = df[
            (df['breed'].isin(['German Shepherd', 'Alaskan Malamute', 'Old English Sheepdog', 'Siberian Husky', 'Rottweiler'])) &
            (df['sex_upon_outcome'] == 'Intact Male') &
            (df['age_upon_outcome_in_weeks'].between(26, 156))
        ]
    elif filter_value == 'disaster_tracking': # else, if user selects mountain rescue, filter
        filtered_df = df[
            (df['breed'].isin(['Doberman Pinscher', 'German Shepherd', 'Golden Retriever', 'Bloodhound', 'Rottweiler'])) &
            (df['sex_upon_outcome'] == 'Intact Male') &
            (df['age_upon_outcome_in_weeks'].between(20, 300))
        ]
    else:
        filtered_df = df # otherwise, or if unfiltered is selected, return unfiltered table
    
    return filtered_df.iloc[
        page_current * 20: (page_current + 1) * 20
    ].to_dict('records')


This snippet is the callback for loading the data table in the dashboard. It checks the current page selected (which is page 1, the first page, initialized), and the filter value (which is unfiltered initialized). Depending on the filter value, the program checks a number of different column values to determine which rows should populate the table. The program checks for the water rescue filter, then mountain rescue, then disaster tracking. Then, if none of those are selected, the program assumes the table should be unfiltered.


Contact
Your name: Conner Hufnagel
