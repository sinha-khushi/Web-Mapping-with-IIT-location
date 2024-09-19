# Web-Mapping-with-IIT-location
# Web-Map-with-Python

Web Map of IIT Locations
This project is a Python-based web application that visualizes various IIT (Indian Institutes of Technology) locations on an interactive map. The map uses data stored in JSON and Excel files to coordinate and plot the locations of different IIT campuses across India.

Features
Interactive map showing the locations of IIT campuses.
Utilizes a JSON file and an Excel file to store and retrieve geographic coordinates.
Simple and easy-to-use interface.
Technologies Used
Python: Core language used for data processing and map creation.
Folium: Used to generate interactive maps.
Pandas: To handle data from Excel files.
JSON: To handle data for location coordinates.
Jupyter Notebook: For testing and visualization (optional).
Installation and Setup
To run this project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/iit-web-map.git
cd iit-web-map
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Python script to generate the map:

bash
Copy code
python map_generator.py
This will generate an HTML file containing the interactive map.

Open the generated map.html file in your web browser to view the IIT locations.

Files
map_generator.py: The main Python script that processes the data and generates the web map.
iit_locations.json: A JSON file containing the coordinates of the IIT campuses.
iit_data.xlsx: An Excel file containing additional data on the IIT locations.
requirements.txt: List of required Python packages.
Dependencies
Make sure to install the following Python packages:

pandas
folium
openpyxl
How It Works
Data Input: The location data is stored in both JSON and Excel formats.
The JSON file contains the latitude and longitude of each IIT.
The Excel file contains additional metadata about the IITs.
Map Generation: The script uses Folium to generate a web-based interactive map. The data from the JSON and Excel files are processed using Pandas to plot markers for each IIT on the map.
Contributions
Feel free to open an issue or submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
