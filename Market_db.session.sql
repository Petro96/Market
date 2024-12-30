
/* ITEM SQL Query  */

INSERT INTO item (name, price, barcode, description) 
VALUES ('Motorola edge 50 neo',280 ,'014327851948','Motorola edge 50 neo 5G 8GB/256GB, CPU octa-core (4x2.5GHz Cortex A-78 & 4x2.0 GHz Cortex-A55 ),4310mAh Battery');

SELECT * FROM item WHERE owner IS NOT NULL;

SELECT * FROM item;

SELECT count(*) FROM item;

SELECT avg(price) FROM item;

SELECT sum(price) FROM item;

/* Inner Join  */
SELECT item.name, item.price , user.userName
FROM item
INNER JOIN user ON item.owner = user.id;

/* Left Join */
SELECT user.userName, item.name, item.owner
FROM user
LEFT JOIN item ON user.id = item.owner
ORDER BY user.userName;





/* USER SQL Query  */


SELECT * FROM user;

SELECT userName, email_address, budget FROM user WHERE budget>=500;

SELECT userName, email_address FROM user ORDER BY userName ASC;

SELECT userName, email_address, budget FROM user WHERE budget<600 AND userName LIKE 'J%'; 

/* select name that owned more than one item and select one of those items that cost more than 300$ */
SELECT user.userName, count(item.owner) as item_count,item.name
FROM item
INNER JOIN user ON user.id = item.owner
GROUP BY userName
HAVING Count(item.owner) > 1 AND price > 300;

