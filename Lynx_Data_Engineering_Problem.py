
# coding: utf-8

# In[8]:

import gzip
import csv
import json
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

df = pd.read_csv("C:/Users/varsh/Desktop/TwoSixCapital/lynx_transaction_data.csv.gz", compression='gzip', header=0, sep='|', quotechar='"')
print(df.head())

engine = create_engine('mysql+mysqldb://lynx_user:Ah$rav@127.0.0.1:3306/lynx_historical_analysis', echo=False)
df.to_sql(name='lynx_transaction_data', con=engine, if_exists = 'append', index=False)


# In[31]:

import MySQLdb
from xlsxwriter.workbook import Workbook

def exec_query(rowIndex, colIndex, query, title, header1, header2):
    print ("", rowIndex, colIndex, query, title, header1, header2)
    sheet.write(rowIndex, colIndex, title, bold)
    sheet.write(rowIndex+2, colIndex, header1)
    sheet.write(rowIndex+2,colIndex+1, header2)
    rowIndex=rowIndex+3
    cursor = con.cursor()
    cursor.execute(query)
    for r, row in enumerate(cursor.fetchall(), start=rowIndex):
        for c, col in enumerate(row):
            sheet.write(r, colIndex + c, col)
    cursor.close()        

user = 'lynx_user' # your username
passwd = 'Ah$rav' # your password
host = '127.0.0.1' # your host
db = 'lynx_historical_analysis' # database where your table is stored
con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
workbook = Workbook('C:/Users/varsh/Desktop/TwoSixCapital/DataEngineeringChallenge.xlsx')
bold = workbook.add_format({'bold': 1})

sheet = workbook.add_worksheet("Revenue")
exec_query(0, 0, "select purchase_year as cohort_year, sum(billings) as revenue from lynx_transaction_data group by purchase_year;", 'Revenue by CohortYear', 'Revenue', 'CohortYear');
exec_query(0, 4, "SELECT EXTRACT(YEAR FROM transaction_date) as purchase_year, sum(billings) as revenue from lynx_transaction_data group by EXTRACT(YEAR FROM transaction_date); ", 'Revenue by PurchaseYear', 'PurchaseYear', 'Revenue');
exec_query(0, 8, "select product_group, sum(billings) as revenue from lynx_transaction_data group by product_group;", 'Revenue by ProductGroup', 'ProductGroup', 'Revenue');
exec_query(0, 12, "select product_type, sum(billings) as revenue from lynx_transaction_data group by product_type;", 'Revenue by ProductType', 'ProductType', 'Revenue',);
exec_query(0, 16, "select country, sum(billings) as revenue from lynx_transaction_data group by country;", 'Revenue by Country', 'Country', 'Revenue');

sheet = workbook.add_worksheet("Number of Customers")
exec_query(0, 0, "select purchase_year as cohort_year, count(distinct(base_license)) as number_of_customers from lynx_transaction_data group by purchase_year;", 'Number of Customers by Cohort year', 'CohortYear', 'Number of Customers');
exec_query(0, 4, "select EXTRACT(YEAR FROM transaction_date) as purchase_year, count(distinct(base_license)) as number_of_customers from lynx_transaction_data group by EXTRACT(YEAR FROM transaction_date);", 'Number of Customers by Purchase year', 'PurchaseYear','Number of Customers');
exec_query(0, 8, "select product_group, count(distinct(base_license)) as number_of_customers from lynx_transaction_data group by product_group;", 'Number of Customers by Product group', 'ProductGroup', 'Number of Customers');
exec_query(0, 12, "select product_type, count(distinct(base_license)) as number_of_customers from lynx_transaction_data group by product_type;", 'Number of Customers by Product type', 'ProductType', 'Number of Customers');
exec_query(0, 16, "select country, count(distinct(base_license)) as number_of_customers from lynx_transaction_data group by country;", 'Number of Customers by Country', 'Country', 'Number of Customers');

sheet = workbook.add_worksheet("Repeated Customers")
exec_query(0, 0, "select purchase_year as cohort_year, count(distinct(base_license)) as repeated_transactions from lynx_transaction_data group by purchase_year having count(base_license)>1;", 'Repeated Transactions by CohortYear', 'CohortYear', 'Repeated Transactions');
exec_query(0, 4, "select EXTRACT(YEAR FROM transaction_date) as purchase_year, count(distinct(base_license)) as repeated_transactions from lynx_transaction_data group by EXTRACT(YEAR FROM transaction_date) having count(base_license)>1;", 'Repeated Transactions by PurchaseYear', 'PurchaseYear', 'Repeated Transactions');
exec_query(0, 8, "select product_group, count(distinct(base_license)) as repeated_transactions from lynx_transaction_data group by product_group having count(base_license)>1;", 'Repeated Transactions by ProductGroup', 'ProductGroup', 'Repeated Transactions');
exec_query(0, 12, "select product_type, count(distinct(base_license)) as repeated_transactions from lynx_transaction_data group by product_type having count(base_license)>1;", 'Repeated Transactions by ProductType', 'ProductType', 'Repeated Transactions');
exec_query(0, 16, "select country, count(distinct(base_license)) as repeated_transactions from lynx_transaction_data group by country having count(base_license)>1;", 'Repeated Transactions by Country', 'Country', 'Repeated Transactions');

sheet = workbook.add_worksheet("Average Transaction Value")
exec_query(0, 0, "select purchase_year as cohort_year, avg(billings) as avg_trans_val from lynx_transaction_data group by purchase_year;", 'Average Transaction Value by CohortYear', 'CohortYear', 'Average Transaction Value');
exec_query(0, 4, "SELECT EXTRACT(YEAR FROM transaction_date) as purchase_year, avg(billings) as avg_trans_val from lynx_transaction_data group by EXTRACT(YEAR FROM transaction_date); ", 'Average Transaction Value by PurchaseYear', 'PurchaseYear', 'Average Transaction Value');
exec_query(0, 8, "select product_group, avg(billings) as avg_trans_val from lynx_transaction_data group by product_group;", 'Average Transaction Value by ProductGroup', 'ProductGroup', 'Average Transaction Value');
exec_query(0, 12, "select product_type, avg(billings) as avg_trans_val from lynx_transaction_data group by product_type;", 'Average Transaction Value by ProductType', 'ProductType', 'Average Transaction Value');
exec_query(0, 16, "select country, avg(billings) as avg_trans_val from lynx_transaction_data group by country;", 'Average Transaction Value by Country', 'Country', 'Average Transaction Value');

sheet = workbook.add_worksheet("Average Cumulative")
exec_query(0, 0, "select purchase_year as cohort_year, sum(billings)/count(distinct(base_license)) as avg_cumulative from lynx_transaction_data group by purchase_year;", 'Average Cumulative by CohortYear', 'CohortYear', 'Average Cumulative');
exec_query(0, 4, "SELECT EXTRACT(YEAR FROM transaction_date) as purchase_year, sum(billings)/count(distinct(base_license)) as avg_cumulative from lynx_transaction_data group by EXTRACT(YEAR FROM transaction_date); ", 'Average Cumulative by PurchaseYear', 'PurchaseYear', 'Average Cumulative');
exec_query(0, 8, "select product_group, sum(billings)/count(distinct(base_license)) as avg_cumulative from lynx_transaction_data group by product_group;", 'Average Cumulative by ProductGroup', 'ProductGroup', 'Average Cumulative');
exec_query(0, 12, "select product_type, sum(billings)/count(distinct(base_license)) as avg_cumulative from lynx_transaction_data group by product_type;", 'Average Cumulative by ProductType', 'ProductType', 'Average Cumulative');
exec_query(0, 16, "select country, sum(billings)/count(distinct(base_license)) as avg_cumulative from lynx_transaction_data group by country;", 'Average Cumulative by Country', 'Country', 'Average Cumulative');

workbook.close()
con.close()


#Revenue by Cohort year', 'Revenue', 'CohortYear');


# In[ ]:



