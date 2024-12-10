
# Vehicle Management System: Car Rentals and Sales

This repository contains the code and data for a data science project focused on predicting key metrics for a car rental and sale system. The objective of this system is to leverage data science models to forecast rental/sale pricing and vehicle popularity based on various factors.

## Objectives

The system provides the following predictive capabilities:

- Rental Price Prediction: Forecast rental prices based on seasonal trends and historical data.
- Vehicle Popularity Prediction: Predict the popularity of different rental car types.
- Model-Specific Price Prediction: Estimate rental prices for specific car models based on historical data.

# 👥 **Team**

- [Nancy Onyejiaka](https://github.com/nancyonyejiaka).
- [Shreyas Prakash](https://github.com/shreyas115).
- [Vishak Nair](https://github.com/Vishak27).


# Repository Structure & Workflow

## Available Notebooks

1. Data Preprocessing Notebooks
`car_dekho_data.ipynb`: Preprocessing for CarDekho vehicle dataset.
`car_rental_data_preprocessing.ipynb`: Cleaning and preparation of rental data.
`car_sales_data_preprocessing.ipynb`: Preprocessing car sales data for analysis.
`enterprise_station_preprocessing.ipynb`: Preprocessing store location data for rental trends.
`used_cars_data.ipynb`: Processing data related to used cars and pricing trends.
`vehicles_data.ipynb`: General preprocessing for vehicle-related datasets.

2. Data Analysis Notebooks
`DataAnalysisProj.ipynb`: Visual and statistical analysis of vehicle pricing, rentals, and sales.
`DataAnalysisProjSQL.ipynb`: SQL-based analysis for querying insights directly from the database.

3. Machine Learning Notebooks
`modelCarSales.ipynb`: Predicting car sales prices using machine learning techniques.
`modelVehicles.ipynb`: Predicting vehicle pricing and trends using regression models.

4. Application Interafce
`project_interface.py`

## Workflow
1. Start with the preprocessing notebooks to clean and prepare the data for analysis and modeling.
Run Data Analysis Notebooks:
2. Use the analysis notebooks to generate insights and visualizations from the preprocessed data.
3. Execute the machine learning notebooks to train models and make predictions based on the data.

# More information

Click on the links below to learn how to best use this repository.

<details><summary>🧰 Dev Setup</summary>

## 🧰 Dev Setup

### 🐍 The Python setup

1. Install [Python 3.9](python.org) or higher on your computer.
2. Install [anaconda](https://www.anaconda.com/products/individual) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your computer.
3. Create a new conda environment:

    ```bash
    conda create -y -n=venv-vehicle-management-system python=3.10.8
    ```
4. Activate the environment and make sure you have `pip` installed inside that environment:

  ```console
  # the exact `activate` command will vary depending on your OS
  conda activate venv-vehicle-management-system 
  ```

💡 Remember to activate this particular `conda` environment whenever you reopen VSCode/the terminal.

10. Install required libraries

  ```console
  pip install -r requirements.txt
  ```

Now, whenever you open a Jupyter Notebook, you should see the `venv-vehicle-management-system` kernel available. You can also run `jupyter kernelspec list` to see all the kernels available on your computer.

</details>

