
/* ITEM SQL Query  */

INSERT INTO item (name, price, barcode, description) 
VALUES ('Motorola edge 50 neo',280 ,'014327851948','Motorola edge 50 neo 5G 8GB/256GB, CPU octa-core (4x2.5GHz Cortex A-78 & 4x2.0 GHz Cortex-A55 ),4310mAh Battery');

SELECT * FROM item WHERE owner IS NOT NULL;

SELECT * FROM item;

/* USER SQL Query  */


SELECT * FROM user;

SELECT userName, email_address, budget FROM user WHERE budget>=500;

SELECT userName, email_address FROM user ORDER BY userName ASC;

SELECT userName, email_address, budget FROM user WHERE budget<600 AND userName LIKE 'J%'; 

