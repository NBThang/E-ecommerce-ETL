LOAD DATA local INFILE 'D:\\E-commerce-ETL\\dataset\\olist_sellers_dataset.csv'
INTO TABLE sellers FIELDS TERMINATED BY ',' enclosed by '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;