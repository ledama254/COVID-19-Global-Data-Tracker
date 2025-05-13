📊 COVID-19 Data Tracker 📈
A simple Python data analysis project that tracks COVID-19 cases from a CSV dataset using pandas. It reads the data, checks for missing values, displays basic dataset information, and provides summary statistics.

📂 Project Structure
kotlin
Copy
Edit
covid19_data_tracker/
├── dataowid-covid-data.csv
├── notebook.ipynb
├── script.py
├── README.md
📦 Dependencies
Before running the project, ensure you have the following Python libraries installed:

bash
Copy
Edit
pip install pandas numpy
📑 How to Run
Clone or download this repository.

Make sure dataowid-covid-data.csv is in the project directory.

Open notebook.ipynb in Jupyter Notebook or run script.py in your terminal.

Run via terminal:
bash
Copy
Edit
python script.py
📌 Features
Load COVID-19 data from a CSV file.

Display dataset column names.

Check for missing values.

Replace 'null' string values with NaN.

Display basic statistical descriptions of the dataset.

Optional: Filter data by specific countries and convert date columns to datetime (make sure to use the correct column name from df.columns).

📝 Notes
Make sure the CSV file has the correct column names as expected by your code.

If you encounter KeyError, use print(df.columns) to check the actual column names and update your code accordingly.

Avoid using null in Python — use None or numpy.nan (np.nan).

📖 Author
Joshua Ledama
PLP Feb Cohort
