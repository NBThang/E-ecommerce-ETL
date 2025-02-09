CREATE TABLE product_category_name_translation(
    product_category_name varchar(64),
    product_category_name_english varchar(64),

    PRIMARY KEY(product_category_name)
);

CREATE TABLE customers(
    customer_id varchar(64),
    customer_unique_id varchar(64),
    customer_zip_code_prefix INT,
    customer_city varchar(64),
    customer_state varchar(64),

    PRIMARY KEY(customer_id)
);


CREATE TABLE geolocation(
    geolocation_zip_code_prefix INT,
    geolocation_lat FLOAT,
    geolocation_lng FLOAT,
    geolocation_city varchar(64),
    geolocation_state varchar(64)
);

CREATE TABLE products(
    product_id varchar(64),
    product_category_name varchar(64),
    product_name_lenght FLOAT,
    product_description_lenght FLOAT,
    product_photos_qty FLOAT,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT,

    PRIMARY KEY(product_id),
    FOREIGN KEY (product_category_name) REFERENCES product_category_name_translation(product_category_name)
);

CREATE TABLE orders(
    order_id varchar(64),
    customer_id varchar(64),
    order_status varchar(64),
    order_purchase_timestamp date,
    order_approved_at date,
    order_delivered_carrier_date date,
    order_delivered_customer_date date,
    order_estimated_delivery_date date,

    PRIMARY KEY(order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE sellers(
    seller_id varchar(64),
    seller_zip_code_prefix INT,
    seller_city varchar(64),
    seller_state varchar(64),

    PRIMARY KEY(seller_id)
);


CREATE TABLE order_items(
    order_id varchar(64),
    order_item_id INT,
    product_id varchar(64),
    seller_id varchar(64),
    shipping_limit_date date,
    price FLOAT,
    freight_value FLOAT,

    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);

CREATE TABLE order_payments(
    order_id varchar(64),
    payment_sequential INT,
    payment_type varchar(64),
    payment_installments INT,
    payment_value FLOAT,

    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE order_reviews(
    review_id varchar(64),
    order_id varchar(64),
    review_score INT,
    review_comment_title text,
    review_comment_message text,
    review_creation_date date,
    review_answer_timestamp date,

    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
