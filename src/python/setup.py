from setuptools import setup, find_packages

setup(
    name="vehiclesystem",
    description="A data science and machine learning system for car rental predictions",
    long_description=(
        "This project provides data analysis and machine learning models for predicting "
        "car rental pricing, popularity, and demand based on various features like season, "
        "vehicle type, and customer demographics. It includes data processing, "
        "exploratory analysis, model training, and database management capabilities."
    ),
    version="0.1.0",
    py_modules=["vehiclesystem"],
    author="Nancy Onyejiaka, Shreyas Prakash, Vishak Nair",
    keywords=["car rental", "machine learning", "data science", "prediction"],
    install_requires=[
        "numpy>=1.24.2",
        "scipy>=1.10.0",
        "pandas>=1.5.3",
        "sqlalchemy>=2.0.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.11.2",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.2",
        "plotnine>=0.10.1",
        "networkx>=2",
        "scikit-learn>=1.2.1",
        "xgboost>=1.7.4",
        "statsmodels>=0.13.2",
        "dvc>=2.9.2",
        "joblib>=1.2.0",
        "ipykernel>=6.21.2",
        "jupyterlab>=3.6.1"
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
