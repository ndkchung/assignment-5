# Assignment 5
**Westmont College Fall 2023**

**CS 128 Information Retrieval and Big Data**

## [Presentation Link](https://docs.google.com/presentation/d/12JK8ub-0zgyWfia7YQZH2dJunZNm5VSH87ZMismPTdk/edit#slide=id.g2a730db9de0_0_11)

## Author Information
* **Name(s)**: Andy Chung, Samuel An
* **Email(s)**: anchung@westmont.edu, san@westmont.edu

## Overview

* I chose to use the dataset 'Rainfall Data from 1901 to 2017 for India' from Kaggle. The dataset does not list an author, but it was updated by Sai Saran.

* Using the DataReader class, this code analyzes the amount of rainfall in India. It reads data from a CSV file, filters and plots relevant information for a specified subdivision and year, and calculates the average rainfall for the specified year.

## Project Structure

**'data' Directory**
* 'Rainfall_Data_LL.csv': csv file containing rainfall data.

**'src' Directory**
* 'rainfall_analysis'
  * 'models.py': Defines the 'DataReader' class with methods for reading data, plotting rainfall data, and implementing data analysis models.
  * 'runner.py': Runs rainfall analysis by taking user input for the subdivision and year, plotting the rainfall for each month, and displaying the average rainfall.
  * 'plot.png': Contains the plot that was generated using madplotlib.

* 'tests'
  * 'test_models': Unit tests to verify the functionality of the 'DataReader' class within the 'models.py' module.
  * 'plot.png': Contains the plot that was generated from the unit tests.

## Software Utilization

1. **Install Dependencies:**
    * Ensure that you have the necessary dependencies installed:
      * *pip install pandas matplotlib numpy*

2. **Run the Code:**
    * Execute the code by running the runner.py file.

3. **Provide a Query:**
    * The query must be a specific subdivision of India and year between 1901 and 2017

## Citations
***This system was developed with the assistance of ChatGPT after providing an initially written code:***

* Edit the following code so that it returns the average rainfall for a specified year and subdivision.

* Edit this code so that it filters the data in the column 'YEAR': <br/>
  * *filtered_data = data[(data["SUBDIVISION"].str.lower() == lowercased_subdivision) & data[str(year)].notna()]*

* Instead of showing the plot how do I export it to a png file?

* 'average_rainfall' does not calculate the average rainfall of the given subdivision and year but just outputs the year. How should I fix this?

* Edit the code for average_rainfall so that it contains the average rainfall of the given year.

* Give me an outline of a unit test file that fully cover the key methods of models.py.
