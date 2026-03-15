-- Lists all records of the table second_table
-- Does not list rows where the name column does not contain a value
-- Records are listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
