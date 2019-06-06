### Funcom Java dataset

Details on the dataset can be found at http://leclair.tech/data/funcom/#procdata

We use the filtered / tokenized datasets for the purpose of this project.

Due to size restrictions of Github, the all files can be downloaded from the following links:

### Variations

1. Raw Java ([link](https://www.dropbox.com/s/sd0w4aeq811nigb/java_raw.tar.gz?dl=0))
2. Tokenized Java ([link](https://drive.google.com/open?id=1Qa-GEZV2gEw8rRzchbOs66AEytVABctc))
3. Raw -> AST Java ([link](https://www.dropbox.com/s/cblexca1k3a05w8/java_ast_syntax.tar.gz?dl=0))
4. Raw -> AST Java Cleaned ([link](https://www.dropbox.com/s/zqy4fx2oxy5fwrf/java_ast_no_syntax.tar.gz?dl=0))

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
  
NOTE: Each variation uses the same indices for the train/valid/test split.

NOTE: The AST files were generated after reading in the source code from the JSON files, using the javalang module in Python

NOTE: Cleaned entails the removal of parentheses, brackets, and other special characters. For example:

#### AST
`
Module(body=[FunctionDef(name='_load_file', args=arguments(args=[Name(id='filename', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='fp', ctx=Store())], value=Call(func=Name(id='open', ctx=Load()), args=[Name(id='filename', ctx=Load()), Str(s='rb')], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='source', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='read', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None), op=Add(), right=Str(s='\n'))), TryExcept(body=[Assign(targets=[Name(id='co', ctx=Store())], value=Call(func=Name(id='compile', ctx=Load()), args=[Name(id='source', ctx=Load()), Name(id='filename', ctx=Load()), Str(s='exec')], keywords=[], starargs=None, kwargs=None))], handlers=[ExceptHandler(type=Name(id='SyntaxError', ctx=Load()), name=None, body=[Print(dest=Attribute(value=Name(id='sys', ctx=Load()), attr='stderr', ctx=Load()), values=[Str(s='>>Syntax \terror \tin'), Name(id='filename', ctx=Load())], nl=True), Raise(type=None, inst=None, tback=None)])], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='close', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Return(value=Name(id='co', ctx=Load()))], decorator_list=[])])
`
#### AST Cleaned
`
module body functiondef name load file args arguments args name id filename ctx param vararg none kwarg none defaults body assign targets name id fp ctx store value call func name id open ctx load args name id filename ctx load str s rb keywords starargs none kwargs none assign targets name id source ctx store value binop left call func attribute value name id fp ctx load attr read ctx load args keywords starargs none kwargs none op add right str s n tryexcept body assign targets name id co ctx store value call func name id compile ctx load args name id source ctx load name id filename ctx load str s exec keywords starargs none kwargs none handlers excepthandler type name id syntaxerror ctx load name none body print dest attribute value name id sys ctx load attr stderr ctx load values str s syntax terror tin name id filename ctx load nl true raise type none inst none tback none orelse expr value call func attribute value name id fp ctx load attr close ctx load args keywords starargs none kwargs none return value name id co ctx load decorator list
`
