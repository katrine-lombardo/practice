-- 1. You are given a table random\_string. The text field holds a single row
--    which contains a random string. Your task is to take the random string and
--    split it on each vowel (a, e, i, o, u) then the resultant substrings will
--    be contained in the output table.
--  Note that the vowels should be removed. If there are no vowels, there will
--    only be one row returned. Where there are multiple vowels in succession,
--    you will see empty rows. A row should be created on each break, whether
--    there is content in the row or not.
--  Regex is advised but not mandatory.
SELECT unnest(REGEXP_SPLIT_TO_ARRAY(text,'[aeiou]'))
AS results
FROM random_string;
