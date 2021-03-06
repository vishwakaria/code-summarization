# code-summarization
The aim of the project is to  build a tool that can automatically produce a natural language summary of source code written in Python

## Directories & descriptions

| Directory | Description |
|-----------|-------------|
| V2 | V2/parallel is the initial extracted function declaration, description & body. V2/repo_split contains the splits used in the original paper|
| data | Contains the processed dataset of function declaration+body, description, and generated ASTs for Python & Java|
| notebooks for java data| Contains the notebook artifacts used to run the process the data, train, and translate. The notebooks act as logs of training, showing the moving train acc, periodic validation acc, and runtimes involved for each experiment. |
| models for python data| The models generated for python dataset |
| predictions for java | Contains the predictions output from various tests conducted to evaluate the importance of different prep-processing steps for Java dataset |
| evals | Contains evaluation scores |
| utils | Helper methods for preprocessing tasks |
| parallel-corpus | The raw corpus used in the original paper |




## Data preprocessing description

The Python3 source codes, obtained from GitHub repositories, were preprocessed by removing the comments, removing semantically irrelevant spaces or new lines. An example of an extracted function is as follows:

### Python function
```python
def _interceptdot (w, X, y):

  ””” 
  Computes  y∗np . dot (X, w).
  It takes into consideration whether  the  intercept  should  be  fit.
  Parameters
  −−−−−−−−−−
  w : ndarray ,  ndarray ,  shape  ( n_features , )  or  ( n_features +  1 , )
    Coefficient  vector .
  [ . . . ]

  ”””

  c =  0
  if w.size  == X. shape [ 1 ]  +  1:
    c = w[−1]
    w = w[:−1]
    z =  safe_sparse_dot (X, w)  + c
    yz = y∗z
  return w,  c ,  yz
  ```
### Extracted declaration 
```def _interceptdot(w, X,  y):``` 

### Extracted docstring 
``` ’ Computes  y∗np . dot (X, w) . DCNL It  takes  into  consideration  if  the  intercept  should be  fit  or  not. DCNL P arameters DCNL w :  ndarray ,  shape  ( n_features , )  or  (n_features  +  1 , ) DCNL Coefficient  vector . DCNL  [ . . . ] ’ ```

### Extracted function-body
``` DCSP c = 0.0 DCNL DCSP  if  (w.size == (X.shape [1] + 1) ): DCNL DCSP  DCSP c = w[(−1)] DCNL DCSP  DCSP w = w[:(−1)] DCNL DCSP z =(safe_sparse_dot(X, w) + c) DCNL DCSP yz = (y∗z) DCNL DCSP  return w,  c ,  yz ```

### Extracted AST
```"Module(body=[FunctionDef(name='_interceptdot', args=arguments(args=[arg(arg='w', annotation=None), arg(arg='X', annotation=None), arg(arg='y', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Str(s='\\n  Computes  y∗np . dot (X, w).\\n  It takes into consideration whether  the  intercept  should  be  fit.\\n  Parameters\\n  −−−−−−−−−−\\n  w : ndarray ,  ndarray ,  shape  ( n_features , )  or  ( n_features +  1 , )\\n    Coefficient  vector .\\n  [ . . . ]\\n\\n  ')), Assign(targets=[Name(id='c', ctx=Store())], value=Num(n=0)), If(test=Compare(left=Attribute(value=Name(id='w', ctx=Load()), attr='size', ctx=Load()), ops=[Eq()], comparators=[BinOp(left=Subscript(value=Attribute(value=Name(id='X', ctx=Load()), attr='shape', ctx=Load()), slice=Index(value=Num(n=1)), ctx=Load()), op=Add(), right=Num(n=1))]), body=[Assign(targets=[Name(id='c', ctx=Store())], value=Subscript(value=Name(id='w', ctx=Load()), slice=Index(value=UnaryOp(op=USub(), operand=Num(n=1))), ctx=Load())), Assign(targets=[Name(id='w', ctx=Store())], value=Subscript(value=Name(id='w', ctx=Load()), slice=Slice(lower=None, upper=UnaryOp(op=USub(), operand=Num(n=1)), step=None), ctx=Load())), Assign(targets=[Name(id='z', ctx=Store())], value=BinOp(left=Call(func=Name(id='safe_sparse_dot', ctx=Load()), args=[Name(id='X', ctx=Load()), Name(id='w', ctx=Load())], keywords=[]), op=Add(), right=Name(id='c', ctx=Load()))), Assign(targets=[Name(id='yz', ctx=Store())], value=BinOp(left=Name(id='y', ctx=Load()), op=Mult(), right=Name(id='z', ctx=Load()))), Return(value=Tuple(elts=[Name(id='w', ctx=Load()), Name(id='c', ctx=Load()), Name(id='yz', ctx=Load())], ctx=Load()))], orelse=[])], decorator_list=[], returns=None)])"```


# Data

## Java

Details on the dataset can be found at http://leclair.tech/data/funcom/#procdata

We use the filtered / tokenized datasets for the purpose of this project.

Due to size restrictions of Github, the all files can be downloaded from the following links:

### Variations

1. Raw Java ([link](https://www.dropbox.com/s/zxizopqgx5at8o3/java_raw.zip?dl=0))
2. Tokenized Java ([link](https://drive.google.com/open?id=1Qa-GEZV2gEw8rRzchbOs66AEytVABctc))
3. Raw -> AST Java ([link](https://www.dropbox.com/s/vwf8sh32xj4ogli/java_ast_syntax.zip?dl=0))
4. Raw -> AST Java Cleaned ([link](https://www.dropbox.com/s/r6w8qgepq1v3hiq/java_ast_no_syntax.zip?dl=0))

Each link contains a compressed file with the following folders:

1. train
    1. functions
    2. comments
2. valid
    1. functions
    2. comments
3. test
    1. functions
    2. comments

NOTE: The AST files were generated after reading in the source code from the JSON files, using the javalang module in Python

NOTE: Cleaned entails the removal of parentheses, brackets, and other special characters. For example:

NOTE: preprocessed here means:
- The methods are split between method name and method body AND both have been tokenized and subtokenized
- The method name has been stripped of parameters
- The methody body has been converted to an AST with several paths sampled between terminal nodes

## Python
- The following are the inputs and targets when AST encodings are used : 

### Inputs (X)
- unprocessed_ast_list_train.zip
- unprocessed_ast_list_dev.zip
- unprocessed_ast_list_test.zip

### Outputs (Y)
- unprocessed_summary_train.zip
- unprocessed_summary_dev.zip
- unprocessed_summary_test.zip

##
- The following are the inputs and targets when AST encodings are not used. Instead, function bodies are used to train the model :

### Inputs (X)
- input_train.txt
- input_dev.txt
- input_test.txt

### Outputs (Y)
- summary_train.txt
- summary_dev.txt
- summary_test.txt

Source: [code2seq](https://github.com/tech-srl/code2seq#datasets)

## Model
We have used the Transformer model as the main architecture for our work. The standard encoder-decoder architecture has served to perform well for many machine translation tasks, hence the transformer architecture was built on top of it. The success of transformers in most NLP tasks has proven the fact that a simple architecture composed of attention mechanisms alone, can outperform the complex CNN and RNN architectures.

## Our contribution
- Evaluate the influence of Abstract Syntax Trees in the input to our summarization model
- Assess the effect of static vs. dynamic typing by training the model on both Java and Python datasets
- Gauge the importance of pre-processing the dataset before feeding it to the model vs. not performing any pre-processing

## Evaluation Metrics:
- BLEU score
- ROUGE-1
- ROUGE-2
- ROUGE-3

## References 
[1] Barone, Antonio Valerio Miceli, and Rico Sennrich. "A parallel corpus of Python functions and documentation strings for automated code documentation and code generation." arXiv preprint arXiv:1707.02275 (2017).

[2] Alon, Uri, Omer Levy, and Eran Yahav. "code2seq: Generating sequences from structured representations of code." arXiv preprint arXiv:1808.01400 (2018).
