-- creates an index with two columns
ALTER TABLE names
ADD COLUMN CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

CREATE INDEX idx_name_first ON names (first_letter, score);