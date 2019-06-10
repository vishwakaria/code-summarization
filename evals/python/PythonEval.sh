#!/bin/sh

# Prints the BLEU and Rouge scores for Java summarization

# Assumes python 3.7 installed with calcBleu.py in the same directory
# also assumes python rouge package has been installed (can be installed using
# "pip install rouge")

PythonModels="ast_cleaned transformer_no_ast raw_python unprocessed_ast"

for model in $PythonModels; do
  echo "BLEU for $model:"
  python calcBleu.py hyps/${model}_hyp.txt refs/${model}_ref.test
done
python calcRouge.py
