#Added Indexes to improve query performance

ALTER TABLE lynx_transaction_data ADD INDEX IDX_PURCHASE_YEAR(purchase_year);
ALTER TABLE lynx_transaction_data ADD INDEX IDX_TX_DATE(transaction_date);
ALTER TABLE lynx_transaction_data ADD INDEX IDX_PRD_GROUP(product_group);
ALTER TABLE lynx_transaction_data ADD INDEX IDX_PRD_TYPE(product_type);
ALTER TABLE lynx_transaction_data ADD INDEX IDX_COUNTRY(country);
commit;