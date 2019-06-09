#!/bin/sh

# Prints the BLEU and Rouge scores for Java summarization

# Assumes python 3.7 installed with calcBleu.py in the same directory
# also assumes python rouge package has been installed (can be installed using
# "pip install rouge")

JavaSumPres="java_ast_clean java_ast java_raw java_tokenized"

for pred in $JavaSumPres; do
  echo "BLEU for $pred:"
  python calcBleu.py hyps/$pred.pred.txt refs/$pred.test
  echo "ROUGE for $pred:"
  rouge -f hyps/$pred.pred.txt refs/$pred.test --avg
done
