# Import required modules
import pandas as pd
import mysql.connector as sconn
from mysql.connector import Error

"""--------------------------------------------------------------------- Exploratory Data Analysis of data ---------------------------------------------------------------------------------------"""

# Read the data from the .csv file and store it in a variable (these datas are uncleaned data)
customers_path = "uncleaned_dataset/Customers.csv"
exchange_rates_path = "uncleaned_dataset/Exchange_Rates.csv"
products = "uncleaned_dataset/Products.csv"
sales_path = "uncleaned_dataset/Sales.csv"
stores_path = "uncleaned_dataset/Stores.csv"
data_dictionary_path = "uncleaned_dataset/Data_Dictionary.csv"

uncleaned_customers = pd.read_csv(customers_path,encoding='ISO-8859-1')
uncleaned_exchange_rates = pd.read_csv(exchange_rates_path,encoding='ISO-8859-1')
uncleaned_products = pd.read_csv(products,encoding='ISO-8859-1')
uncleaned_sales = pd.read_csv(sales_path,encoding='ISO-8859-1')
uncleaned_stores = pd.read_csv(stores_path,encoding='ISO-8859-1')
uncleaned_data_dictionary = pd.read_csv(data_dictionary_path,encoding='ISO-8859-1')


#This funtion will display the top 10 data in the file
def head_data(data,data_name):
    try:
        print(f'The head datas in the {data_name} are:')
        print(data.head())
    except Exception as e:
        print(f'Error occured when fetching the head values from the {data_name}')


#This funtion will display the last 10 data in the file
def tail_data(data,data_name):
    try:
        print(f'The tail datas in the {data_name} are:')
        print(data.head())
    except Exception as e:
        print(f'Error occured when fetching the tail values from the {data_name}')


#This function will find the shape of the dataset
def find_shape(data, data_name):
    try:
        data_shape=data.shape
        print(f'{data_name}',":",data_shape)
    except Exception as e:
        print("Error occured when finding the shape of the data",data_name,":",e)


#This function will return the information of the dataset
def data_info(data, data_name):
    try:
        print(f'{data_name} Info:')
        data.info()
    except Exception as e:
        print("Error occured when finding the info of the data",data_name,":",e)


#This function will print the column name 
def get_column_names(file,file_name):
    try:
        print(f'The column name in the {file_name} are:')
        print(file.columns)
    except Exception as e:
        print(f'Error occured when fetching the column names from the {file_name} dataset',e)


#This function will change the change the datatype of a column to string
def change_dtype_str(file,column_name,file_name):
    try:
        file[column_name]=file[column_name].astype(str)
        print(f'the datatype of the {column_name} column from {file_name} is changed to string successfully')
    except Exception as e:
        print("Error occured when changing the datatype to string of column",column_name,":",e)


#This function will change the change the datatype of a column to int
def change_dtype_int(file,column_name,file_name):
    try:
        file[column_name]=file[column_name].astype(int)
        print(f'the datatype of the {column_name} column from {file_name} is changed to int successfully')
    except Exception as e:
        print("Error occured when changing the datatype to int of column",column_name,":",e)


#This function will change the change the datatype of a column to datetime
def change_dtype_datetime(file,column_name,file_name):
    try:
        file[column_name] = pd.to_datetime(file[column_name])
        print(f'the datatype of the {column_name} column from {file_name} is changed to datetime successfully')
    except Exception as e:
        print(f'Error occured when changing the dataype to datetime of',column_name,":",e)


#This function will check number of null values present in the each column in a dataset
def check_na(file,file_name):
    try:
        print(f'Null values in {file_name} dataset \n{file.isnull().sum()}')
        na_columns = file.isnull().sum()
        na_columns_filtered = na_columns[na_columns > 0]

        if not na_columns_filtered.empty:
            return na_columns_filtered.index.tolist()
        else:
            return []

    except Exception as e:
        print(f'Error occured when finding the sum of NULL values in the {file_name} dataset')


#This function prints the rows where any one column contains NULL value
def print_NA_rows(file,column_null,file_name):
    try:
        rows_with_null_in_state_code = file[file[column_null].isnull()]
        print(f'rows from the {file_name} dataset which contains Null values in any one column \n{rows_with_null_in_state_code}') 
    except Exception as e:
        print(f'Error occured when finding the NA rows in {file} dataset')


#This function will find the duplicate values present in the dataset
def find_duplicate(file,file_name):
    try:
        duplicate_row = file.loc[file.duplicated()]
        if not duplicate_row.empty:
            print(f"there is a {file.duplicated().sum()} duplicate values located in the table")
            print(f'The duplicate rows are \n{duplicate_row}')
        else:
            print(f'There is no duplicate values in the {file_name} dataset')
    except Exception as e:
        print(f'Error occured when finding the duplicate value in the {file_name} dataset')


#This function will find the garbage value present in the dataset
def find_garbage_value(file,file_name):
    try:
        for i in file.select_dtypes(include='object').columns:
            print(file[i].value_counts())
            print("*********garbage value*******")
    except Exception as e:
        print(f'Error occured when finding the garbage value in the {file_name} dataset',e)


#This function will dscribe the dataset
def describe_dataset(file,file_name):
    try:
        print(f'{file_name} data set description:')
        print(file.describe(include='all')) # Note : reason for include='all' because the describe function only describe int and datatime datatype, inorder to describe object datatype also include in added
    except Exception as e:
        print(f'Error occured when decribing the {file_name} dataset',e)


#This function will print the correlation between the columns in a dataset
def correlation(file,file_name):  
    try:
        print(file.corr())  # Note : corr can applicable in numeric datatypes like int and float not string datatype
    except Exception as e:
        print(f'Error occured when finding the correlation of the {file_name} dataset',e)


#This function will drop the row which contains null value in any cell
def drop_na(file,file_name):
    try:
        rows_before = file.shape[0]
        print(rows_before)
        file_cleaned = file.dropna()
        rows_after = file.shape[0]
        print(rows_after)
        rows_dropped = rows_before - rows_after
        print(f'{rows_dropped} rows containing null values were deleted successfully.')
        return file_cleaned
    except Exception as e:
        print(f'Error occured when dropping rows which contains null values in {file_name} dataset')


#This function will create a .csv file
def create_csv(file,new_file_name):
    try:
        file.to_csv(f"cleaned_dataset/{new_file_name}.csv", index=False)
        print(f'New {new_file_name} dataset is created successfully')
    except Exception as e:
        print(f'Error occured when creating a new {new_file_name} dataset',e)


#This function will drop the column in the table
def drop_column(file,column_name,file_name):
    try:
        dropped_data = file.drop(column_name,axis=1)
        print(f'The column {column_name} from {file_name} is deleted successfully')
        return dropped_data
    except Exception as e:
        print(f'Error occured when deleting {column_name} from {file_name} dataset',e)


#This function will drop the row in the table
def drop_row(file,column_name,file_name):
    try:
        dropped_row = file.dropna()
        print(f'The null row from {file_name} is deleted successfully')
        return dropped_row
    except Exception as e:
        print(f'Error occured when deleting the {column_name} from {file_name} dataset',e)


#This function will fill the null values with '0.0'
def fill_na(file,column_name,file_name):
    try:
        file[column_name] = file[column_name].fillna(0.0)
        print(f'The null row from {file_name} is filled successfully')
    except Exception as e:
        print(f'Error occured when filling the {column_name} from {file_name} dataset',e)


"""---------------------------------------------customers dataset------------------------------------------------------"""

# -------------------understanding dataset
find_shape(uncleaned_customers,'uncleaned_customers')
data_info(uncleaned_customers,'uncleaned_customers')

column_NA = check_na(uncleaned_customers,'uncleaned_customers')
print("column name with null value",column_NA)

if len(column_NA)!=0:
    for columnname in column_NA:
        print_NA_rows(uncleaned_customers,columnname,"uncleaned_customers")

find_duplicate(uncleaned_customers,'uncleaned_customers')
find_garbage_value(uncleaned_customers,'uncleaned_customers')
describe_dataset(uncleaned_customers,'uncleaned_customers')

#----------------------cleaning dataset
change_dtype_datetime(uncleaned_customers,'Birthday','uncleaned_customers')
customers_file_cleaned = drop_column(uncleaned_customers,'State Code','uncleaned_customers')
head_data(customers_file_cleaned,'uncleaned_customers')

#-----------------------storing the cleaned customer dataset
create_csv(customers_file_cleaned,'C_Customers')

"""---------------------------------------------sales dataset------------------------------------------------------"""

#**********************understanding the data
find_shape(uncleaned_sales,'uncleaned_sales')
get_column_names(uncleaned_sales,'uncleaned_sales')
data_info(uncleaned_sales,'uncleaned_sales')  #before changing datatype
describe_dataset(uncleaned_sales,'uncleaned_sales')
find_duplicate(uncleaned_sales,'uncleaned_sales')
find_garbage_value(uncleaned_sales,'uncleaned_sales')

column_NA_sales = check_na(uncleaned_sales,'uncleaned_sales')
print("column name with null value",column_NA_sales)

#*************************cleaning the data
change_dtype_datetime(uncleaned_sales,'Order Date','uncleaned_sales')
sales_file_cleaned = drop_column(uncleaned_sales,'Delivery Date','uncleaned_sales')

#******************* analayze data after cleaning
data_info(sales_file_cleaned,'uncleaned_sales') 
head_data(sales_file_cleaned,'uncleaned_sales')

# #******************** storing the cleaned sales dataset
create_csv(sales_file_cleaned,'C_Sales')

"""---------------------------------------------store dataset------------------------------------------------------"""

#**********************understanding the data
find_shape(uncleaned_stores,'uncleaned_stores')
data_info(uncleaned_stores,'uncleaned_stores')
describe_dataset(uncleaned_stores,'uncleaned_stores')
find_duplicate(uncleaned_stores,'uncleaned_stores')
find_garbage_value(uncleaned_stores,'uncleaned_stores')

column_NA_stores = check_na(uncleaned_stores,'uncleaned_sales')
print("column name with null value",column_NA_stores)

#*************************cleaning the data
change_dtype_datetime(uncleaned_stores,'Open Date','uncleaned_stores')
fill_na(uncleaned_stores,'Square Meters','uncleaned_stores')

column_NA_stores = check_na(uncleaned_stores,'uncleaned_sales')
print("column name with null value",column_NA_stores)

#******************** storing the cleaned sales dataset
create_csv(uncleaned_stores,'C_Store')

"""---------------------------------------------Product dataset------------------------------------------------------"""

#**********************understanding the data
find_shape(uncleaned_products,'uncleaned_products')
data_info(uncleaned_products,'uncleaned_products')
describe_dataset(uncleaned_products,'uncleaned_products')
find_duplicate(uncleaned_products,'uncleaned_products')
find_garbage_value(uncleaned_products,'uncleaned_products')

column_NA_products = check_na(uncleaned_products,'uncleaned_products')
print("column name with null value",column_NA_products)

#******************** storing the cleaned sales dataset
create_csv(uncleaned_products,'C_Products')

"""---------------------------------------------exchange rate dataset------------------------------------------------------"""

# **********************understanding the data
find_shape(uncleaned_exchange_rates,'uncleaned_exchange_rates')
data_info(uncleaned_exchange_rates,'uncleaned_exchange_rates')
describe_dataset(uncleaned_exchange_rates,'uncleaned_exchange_rates')
find_duplicate(uncleaned_exchange_rates,'uncleaned_exchange_rates')
find_garbage_value(uncleaned_exchange_rates,'uncleaned_exchange_rates')

column_NA_exchangerates= check_na(uncleaned_exchange_rates,'uncleaned_exchange_rates')
print("column name with null value",column_NA_exchangerates)

#*************************cleaning the data
change_dtype_datetime(uncleaned_exchange_rates,'Date','uncleaned_exchange_rates')
data_info(uncleaned_exchange_rates,'uncleaned_exchange_rates')

#******************** storing the cleaned sales dataset
create_csv(uncleaned_exchange_rates,'C_Exchange_Rates')


"""------------------------------------------------------------------------------ MySQL database --------------------------------------------------------------------------------"""

#Configure the sql connector 
def configuration():
    try:
        config = {
            "user":"root",
            "password":"Aa25@04@2002",
            "host":"localhost",
            "database":"project_dataspark"
        }
        print("Configuration completed")
        return config
    
    except Error as e:
        print("Error occurred during configuration:",e)


#Configure the connection between python and mysql
def connection():
    try:
        config=configuration()
        if config is None:
            return None
        conn=sconn.connect(**config)

        if conn.is_connected():
            print("connection completed")
        return conn
    
    except Error as e:
        print("Error occurred when open connection:",e)


#This function will drop the table
def drop_table(conn,query_drop):
    c=conn.cursor()
    try:
        c.execute(query_drop)
        print("Table dropped successfully")
    
    except Error as e:
        print("Error occurred when dropping data",e)


#This function will create the table
def create_table(conn,query_create):
    c=conn.cursor()
    try:
        c.execute(query_create)
        print("Table Created successfully")
        pass

    except Error as e:
        print("Error occurred when creating table",e)


#This function will insert data into the table
def insert_data_to_table(conn,query_insert,value):
    c=conn.cursor()
    try:
        c.executemany(query_insert,value)
        conn.commit()
        print("data inserted into the table successfully")
    except Error as e:
        print("Error occurred when inserting the data into the table",e)
 

#This function will close the connection
def close_connection(conn):
    try:
        conn.close()
        print("connection closed successfully")
    except Error as e:
        print('Error occurred when closing the connection: ',e)    


#Create connection -----------------------------------------------------------------------------------
conn = connection()

#If the table already exists drop it to avoid the append of datas ------------------------------------
drop_table(conn,'drop table if exists customers')
drop_table(conn,'drop table if exists sales')
drop_table(conn,'drop table if exists stores')
drop_table(conn,'drop table if exists products')
drop_table(conn,'drop table if exists exchange_rates')


#Creating tables----------------------------------------------------------------------------------------
query_create_table_customers = """create table if not exists customers (
customer_key int primary key,
gender varchar(100),
name varchar(100),
city varchar(100),
state varchar(100),
zip_code varchar(100),
country varchar(100),
continent varchar(100),
birthday date,
age int
);"""

query_create_table_sales = """create table if not exists sales (
order_number int,
line_item int,
order_date date,
customer_key int,
store_key int,
product_key int,
quantity int,
currency_code varchar(100)
);"""

query_create_table_store = """create table if not exists store (
store_key int primary key unique,
country varchar(100),
state varchar(100),
square_meters int,
open_date date
)"""

query_create_table_product = """create table if not exists products (
product_key int primary key unique,
product_name varchar(100),
brand varchar(100),
color varchar(100),
unit_cost_usd varchar(100),
unit_price_usd varchar(100),
profit varchar(100),
subcategory_key int not null,
subcategory varchar(100),
category_key int not null,
category varchar(100)
)"""

query_create_table_exchange_rates = """create table if not exists exchange_rates (
Date date,
currency varchar(100),
exchange float
)"""

create_table(conn,query_create_table_customers)
create_table(conn,query_create_table_sales)
create_table(conn,query_create_table_store)
create_table(conn,query_create_table_product)
create_table(conn,query_create_table_exchange_rates)

#Inserting data in table ---------------------------------------------------------------------------------------------------------------------
tuples_customer = list(map(tuple, customers_file_cleaned.values))
tuples_sales = list(map(tuple, sales_file_cleaned.values))
tuples_store = list(map(tuple, uncleaned_stores.values))
tuples_product = list(map(tuple, uncleaned_products.values))
tuples_exchange_rate = list(map(tuple, uncleaned_exchange_rates.values))

query_insert_customer_data="""insert into customers (customer_key,gender,name,city,state,zip_code,country,continent,birthday,age) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
on duplicate key update customer_key = values(customer_key), gender = values(gender),name = values(name), city =values(city),
state = values(state), zip_code =values(zip_code),country = values(country), continent = values(continent), birthday = values(birthday), age = values(age)
"""

query_insert_sales_data="""insert into sales (order_number,line_item,order_date,customer_key,store_key,product_key,quantity,currency_code) values (%s,%s,%s,%s,%s,%s,%s,%s)
on duplicate key update order_number = values(order_number), line_item = values(line_item),order_date = values(order_date), customer_key =values(customer_key),
store_key = values(store_key), product_key =values(product_key),quantity = values(quantity), currency_code =values(currency_code)
"""

query_insert_store_data="""insert into store (store_key,country,state,square_meters,open_date) values (%s,%s,%s,%s,%s)
on duplicate key update store_key = values(store_key), country = values(country),state = values(state), square_meters =values(square_meters), open_date = values(open_date)
"""

query_insert_product_data="""insert into products (product_key,product_name,brand,color,unit_cost_usd,unit_price_usd,profit,subcategory_key,subcategory,category_key,category) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
on duplicate key update product_key = values(product_key), product_name = values(product_name),brand = values(brand), color =values(color),
unit_cost_usd = values(unit_cost_usd), unit_price_usd =values(unit_price_usd), profit = values(profit), subcategory_key = values(subcategory_key), subcategory =values(subcategory),
category_key = values(category_key), category =values(category)
"""

query_insert_exchange_rate_data="""insert into exchange_rates (Date,currency,exchange) values (%s,%s,%s)
on duplicate key update Date = values(Date), currency = values(currency),exchange = values(exchange)
"""

insert_data_to_table(conn,query_insert_customer_data,tuples_customer)
insert_data_to_table(conn,query_insert_sales_data,tuples_sales)
insert_data_to_table(conn,query_insert_store_data,tuples_store)
insert_data_to_table(conn,query_insert_product_data,tuples_product)
insert_data_to_table(conn,query_insert_exchange_rate_data,tuples_exchange_rate)

#Close connection -----------------------------------------------------------------------------------------------------------------------------------
conn.close()

