# Retail transaction data management and Customer Analytics framework

In this project, we propose to build an application that will help online retail stores in offering personalized services to customers. To achieve better results, three strategies in customer analytics are considered in this project - a personalized recommendation system, categorization of customers, and sales trend analysis for achieving better customer retention.

## Features
 * #### Support for Excel and MySQL data input

      * Input transaction data can be loaded from either Excel or MySQL.

      * Formatting functions and filter functions can be specified to the particular input without affecting the other input.

 * #### Re-usable independent module for data pre-processing

      * Data pre-processing is made as an independent step. The pre-processed data can be retrieved without running the entire program and can be re-used by any other program.

      * Data pre-processing can be set specific to input from MySQL/Excel without affecting the processing from a different source.


 * #### RFM Analysis

      * re-usable model which performs Recency, Frequency, and monetary matrix based analysis on the transactional data.

      * All the 3 aspects of the analysis are modularized so single analysis can be performed without any code change.

 * #### Customer segmentation

      * Nested bullet

      * Sub-nested bullet etc.

 * #### Basket analysis

      * Nested bullet

      * Sub-nested bullet etc.

## Installation

#### Requirements
* MariaDB  10.4+ or any latest version of SQL.
* Any valid IDE to run the python code with Python 3.7+ Interpreter.
* Python 3.7+ packages listed below - 
   * Python package Pandas. 

     ```pip install pandas```

  * Python package Numpy. 

     ```pip install numpy```

  * Python package pymysql. 

     ```pip install pymysql```

  * Python package matplotlib.pyplot.

     ```pip install matplotlib.pyplot```

  * Python package Scipy.

     ```pip install scipy```

## Usage

To load the data from Excel - 
```python
from online_retail_analysis import *

# loads the data from excel sheet
data_df_dictionary = load_online_retail_data()

# to select any specific data, use the get method as shown below
data_df_dictionary.get('complete_retail_data')

```

To load the data from MySQL - 

```python
from online_retail_analysis import *

# loads the data from excel sheet
data_df_dictionary = load_online_retail_data(read_from_csv=False)

# to select any specific data, use the get method as shown below
data_df_dictionary.get('complete_retail_data')
```

To run the RFM analysis - 
```python
from online_retail_analysis import *

# loads the data from excel sheet
rfm_analysis_data_df = perform_rfm_analysis(read_from_csv=True, data_set_name="complete_retail_data")

print(rfm_analysis_data_df)
```

To run the Customer segmentation - (NOT IMPLEMENTED)
```python
from online_retail_analysis import *
```

To run the Customer segmentation - (NOT IMPLEMENTED)
```python
from online_retail_analysis import *
```

To run the Sales trend analysis - (NOT IMPLEMENTED)
```python
from online_retail_analysis import *
```

## Contributing

Please access the code at - https://github.com/ar1422/CSCI-620-Group-Project.git.<Currently the repository is kept private for development purpose.>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
