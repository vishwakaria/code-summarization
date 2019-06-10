# Evaluation

This folder contains the scripts used to evaluate the BLEU and ROUGE scores of
our test sets for both our Python and Java models. Each prediction file has its
own reference file since the rouge library in Python enforces that the line
count of the both files are the same.

For BLEU, the SmoothingFunction used was method4, which allowed for any
references shorter than 4 words be accounted as non-zero values while scaling
accordingly.
