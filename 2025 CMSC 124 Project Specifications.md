 

University of the Philippines Los Banos  
College of Arts and Sciences  
Institute of Computer Science

# **CMSC 124**

## Design and Implementation of Programming Languages

**PROJECT SPECIFICATIONS**  
First Semester A.Y. 2025-2026

Specifications based on  
KBPPelaez’ and CNMPeralta’s Previous CMSC124 Project Specifications

# 

# **General Instructions**

You are to create an **interpreter** for the LOLCode Programming Language. The constructs required for the project are discussed in the succeeding pages of this document. However, more information regarding LOLCode can be found here: \[[Website](http://www.lolcode.org/)\] \[[Original Specifications](https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md)\] \[[Interpreter](https://github.com/justinmeza/lci)\].

The project-making process is divided into 2 phases:

1. **Planning Phase**  
   In this phase, you are to submit \[type\]written documents that you will use during the coding phase. These documents must be submitted early so that we can annotate them with corrections if there are any.

   The documents are as follows:  
   1. **Patterns for LOLCode Lexemes**  
      A list of regular expressions that will match the lexemes of the LOLCode PL must be submitted by September 29. Answers must be written/typed using this template: \[[Google Docs](https://docs.google.com/document/d/1nJLL_EbinxDJm6y6pPfVMqCp5PKdywirsrvjx2a4lXU/edit?usp=sharing)\].  
   2. **Grammar for LOLCode Syntax**  
      The grammar that your LOLCode interpreter will follow must be written/typed using this template: \[[Google Docs](https://docs.google.com/document/d/1bgkrAOGSvlFYz1uk5ieOgdpt1y5NC9yoTPyj0dlfVaw/edit?usp=sharing)\]. This must be submitted by October 23.  
        
2. **Coding Phase**  
   You must start coding at least a month before the end of the classes. You are to present your progress to your lab instructors three (3) times: one for the lexical analyzer part, one for the syntax analyzer part, and one for the semantics of your code.

   The progress presentations are required *and are graded* to guarantee that you are coding the interpreter correctly, thus lessening the possibility of re-coding in the succeeding presentations.

You are allowed to start coding once the feedback on your regular expressions has been given.

### **Note\!**

You are required to submit a working interpreter. At the minimum, your interpreter must be able to evaluate at least one operation or statement.

Since you are to create an interpreter, the interpreter must be able to analyze each line of the program *lexically, syntactically, and semantically*. If your program cannot completely execute these three phases of interpretation, that will not be accepted, and thus you will be given a grade of 0 for the coding portion of your project.

# **Specifications**

The minimum requirements for the project are listed below.

### **FILE NAMING AND FORMATTING                                                                                          \<\<**

* LOLCode source files should have the `.lol` file extension.  
* LOLCode programs should start with the `HAI` keyword (nothing before, except comments or functions (if you implement functions)), and end with the `KTHXBYE` keyword (nothing after, except comments or functions (if you implement functions)).  
* There is no need to include the version number after the `HAI` keyword.

| `sample1.lol` | `sample2.lol` |
| :---- | :---- |
| `HAI   BTW statements here KTHXBYE` | `BTW this is accepted! HAI    BTW statements here KTHXBYE BTW this is accepted!` |

### **SPACING/WHITESPACES                                                                                                               \<\<**

* You may assume that one line contains one statement only. There is no need to support soft command breaks. Each statement is delimited by the new line.

| `HAI   BTW no need to support this   I HAS A ...   var ITZ 2, VISIBLE var KTHXBYE` |
| :---- |

* You may assume that there is only one whitespace between keywords.

| `I HAS A var1 BTW YEEES!` | `I   HAS A      var2 BTW NO` |
| :---- | :---- |

* Indentation is irrelevant.  
* Spaces inside a `YARN` literal should be retained.

| `“Spaces          between” BTW should NOT become “Spaces between”` |
| :---- |

### **COMMENTS                                                                                                                                             \<\<**

* Comments are not considered statements, and must be ignored. They should be able to coexist with another statement on a line.

| `HAI   I HAS A var ITZ 2 BTW I’m allowed! KTHXBYE` |
| :---- |

* Keywords `OBTW` and `TLDR` for multi-line comments must have their own lines, i.e., they cannot co-exist with other statements. The `OBTW` and `TLDR` must have their own lines (which may include some comments *but not other statements*).

| `I HAS A var ITZ 2 OBTW Hi! TLDR         ← NOT ALLOWED!!! I HAS A var OBTW noot TLDR ITZ 2        ← NOT ALLOWED!!! I HAS A num OBTW konnichiwa             ← NOT ALLOWED!!!             TLDR  I HAS A var1                            ← NOT ALLOWED!!! OBTW what way? TLDR I HAS A var2 I HAS A var3                            ← YASSSS ALLOWED!!! OBTW this      Way TLDR` |
| :---- |

### **VARIABLES                                                                                                                                              \<\<**

* All variables must be declared inside the `WAZZUP` portion of the program. The `WAZZUP` clause is found at the beginning of the program, after `HAI`.

| `WAZZUP BTW Declare variables here BUHBYE` |
| :---- |

* Variable names must start with a letter, followed by any combination of letters, numbers, and underscores. No spaces, dashes, or other special symbols are allowed to be part of the variable name.  
* Variable declaration is done using the keyword `I HAS A`.  
* Variable initialization is done using the `ITZ` keyword, and the value may be a literal, the value of another variable, or the result of an expression. Initializing variables is not required.

| `I HAS A thing                      BTW uninitialized var I HAS A thing2 ITZ “some”          BTW literal I HAS A thing3 ITZ thing2          BTW variable I HAS A thing4 ITZ SUM OF 5 AN 4   BTW expression` |
| :---- |

* Initialization may contain any operation that results to a literal value.  
* You should be able to implement the implicit `IT` variable.

### **DATA TYPES                                                                                                                                            \<\<**

* Variables in LOLCode are dynamically-typed, i.e., the data type of its variables changes automatically when a new value of a different data type is assigned.  
* LOLCode implements the following data types:

| DATA TYPE | IN LOLCode | DESCRIPTION |
| :---: | :---: | ----- |
| `untyped` | `NOOB` | The data type of uninitialized variables is `NOOB`. |
| `integer` | `NUMBR` | These are sequences of digits without a decimal point (`.`) and are not enclosed by double quotes. Negative numbers must be preceded by a negative sign (`-`), but positive numbers **MUST NOT** be preceded by a positive sign (`+`). |
| `float` | `NUMBAR` | They are sequences of digits with exactly one decimal point (`.`) and are not enclosed by double quotes. They may be preceded by a negative sign (`-`) to indicate that the value is negative. For positive values, it **MUST NOT** be preceded by a positive sign (`+`) to indicate that it is positive. |
| `string` | `YARN` | These are delimited by double quotes (`“”`). |
| `boolean` | `TROOF` | The value of a `TROOF` can be `WIN` (true) or `FAIL` (false). |


* Special characters inside `YARN`s (e.g. `:)`, `:>`, etc.) are not required.

  ### 

### **OPERATIONS                                                                                                                                          \<\<**

* Operations are in prefix notation.  
* All operations except `SMOOSH`, `ALL OF`, `ANY OF`, and `NOT` are binary.  
* `SMOOSH`, `ALL OF`, and `ANY OF` are of infinite arity.  
* `NOT` is unary.  
* All operations except `SMOOSH`, `ALL OF`, and `ANY OF` can be nested.  
* The `AN` keyword is required to separate operands.

#### **Input/Output**

* Printing to the terminal is done using the `VISIBLE` keyword.  
* `VISIBLE` has infinite arity and concatenates all of its operands after casting them to `YARN`s. Each operand is separated by a ‘+’ symbol.  
* The `VISIBLE` statement automatically adds a new line after all the arguments are printed.  
* Accepting input is done using the `GIMMEH` keyword.  
* `GIMMEH` must always use a variable, where the user input will be placed. The input value is always a `YARN`.

#### **Arithmetic/Mathematical Operations**

* Below are the arithmetic operations:

| `SUM OF <x> AN <y>             BTW + (add) DIFF OF <x> AN <y>            BTW - (subtract) PRODUKT OF <x> AN <y>         BTW * (multiply) QUOSHUNT OF <x> AN <y>        BTW / (divide) MOD OF <x> AN <y>             BTW % (modulo) BIGGR OF <x> AN <y>           BTW max SMALLR OF <x> AN <y>          BTW min` |
| :---- |

* Mathematical operations are performed with `NUMBR`s and/or `NUMBAR`s involved.  
* If a value is not a `NUMBAR` and is not a `NUMBR`, it must be implicitly typecast into a `NUMBAR`/`NUMBR` depending on the value. Typecasting rules must apply (see section on typecasting).  
* If a value cannot be typecast, **the operation must fail with an error**.  
* If **both** operands evaluate to a `NUMBR`, the result of the operation is a `NUMBR`.  
* If **at least one** operand is a `NUMBAR`, the result of the operation is a `NUMBAR`.  
* Nesting of operations is allowed, but all operations are still binary.

| `SUM OF 2 AN 4               BTW result is NUMBR DIFF OF 4 AN 3.14           BTW result is NUMBAR PRODUKT OF “2” AN “7”       BTW result is NUMBR QUOSHUNT OF 5 AN “12”       BTW result is a NUMBR MOD OF 3 AN “3.14”          BTW result is a NUMBAR SUM OF QUOSHUNT OF PRODUKT OF 3 AN 4 AN 2 AN 1   BTW ((3*4)/2)+1 SUM OF SUM OF SUM OF 3 AN 4 AN 2 AN 1            BTW ((3+4)+2)+1` |
| :---- |

#### **Concatenation**

* The syntax for string concatenation is shown below:

| `SMOOSH str1 AN str2 AN ... AN strN  BTW str1+str2+...+strN` |
| :---- |

* `SMOOSH` does not require the `MKAY` keyword.  
* If the operand evaluates to another data type, they are implicitly typecast to `YARN`s when given to `SMOOSH`. For example, 124 will become “124”, 2.8 will become “2.8”, `WIN` will become “WIN”, and so on.

#### 

#### **Boolean Operations**

* Below are the boolean operations:

| `BOTH OF <x> AN <y>             BTW and EITHER OF <x> AN <y>           BTW or WON OF <x> AN <y>              BTW xor NOT <x>                        BTW not ALL OF <x> AN <y> ... MKAY     BTW infinite arity AND ANY OF <x> AN <y> ... MKAY     BTW infinite arity OR` |
| :---- |


* If the operands are not `TROOF`s, they should be implicitly typecast.  
* `ALL OF` and `ANY OF` cannot be nested into each other and themselves, but may have other boolean operations as operands.

| `ALL OF NOT x AN BOTH OF y AN z AN EITHER OF x AN y MKAY BTW (!x) ⋀ (y⋀z) ⋀ (x⋁y) ← YAASSS ALLOWED!! ALL OF ALL OF x AN y MKAY AN z MKAY BTW :( ← NOT ALLOWED!!` |
| :---- |

#### **Comparison Operations**

* Below are the comparison operations:

| `BOTH SAEM <x> AN <y>          BTW x == y DIFFRINT <x> AN <y>           BTW x != y` |
| :---- |


* Relational operations are created by adding the `BIGGR OF` or `SMALLR OF` operations:

| `BOTH SAEM <x> AN BIGGR OF <x> AN <y>    BTW x >= y BOTH SAEM <x> AN SMALLR OF <x> AN <y>   BTW x <= y DIFFRINT <x> AN SMALLR OF <x> AN <y>    BTW x > y DIFFRINT <x> AN BIGGR OF <x> AN <y>     BTW x < y` |
| :---- |

* Comparisons are done using integer math if the operands are `NUMBR`s, and floating-point math if the operands are `NUMBAR`s.  
* There is no automatic typecasting for operands in a comparison operation.

#### **Typecasting**

* The following are the rules you must follow when typecasting in LOLCode.

| DATA TYPE | DESCRIPTION |
| :---: | ----- |
| `NOOB` | `NOOB`s can be implicitly typecast into `TROOF`. Implicit typecasting to any other type except `TROOF` will result in an error. Explicit typecasting of `NOOB`s is allowed and results to empty/zero values depending on the type. |
| `TROOF` | The empty string (`“”`) and numerical zero values are cast to `FAIL`. All other values, except those mentioned above, are cast to `WIN`. Casting `WIN` to a numerical type results in `1` or `1.0`. Casting `FAIL` results in a numerical zero. |
| `NUMBAR` | Casting `NUMBAR`s to `NUMBR` will truncate the decimal portion of the `NUMBAR`. Casting `NUMBAR`s to `YARN` will truncate the decimal portion up to two decimal places. |
| `NUMBR` | Casting `NUMBR`s to `NUMBAR` will just convert the value into a floating point. The value should be retained. Casting `NUMBR`s to `YARN` will just convert the value into a string of characters. |
| `YARN` | A `YARN` can be successfully cast into a `NUMBAR` or `NUMBR` if the `YARN` does not contain any non-numerical, non-hyphen, non-period characters. |

* Explicit typecasting a value can be done using the `MAEK` operator. This operator, however, only modifies the resulting value, and not the variable involved, if there is any.

| `I HAS A var1 ITZ 12    BTW var1 is a NUMBR MAEK var1 A NUMBAR     BTW returns NUMBAR equivalent of var1 to IT (12.0)                        BTW var1 is still a NUMBR MAEK var1 YARN         BTW returns YARN equivalent of var1 to IT (“12”)                        BTW var1 is still a NUMBR` |
| :---- |

* Re-casting a variable can be done via normal assignment statement involving `MAEK` or via `IS NOW A`.

| `I HAS A number ITZ 17        BTW number is NUMBR type number IS NOW A NUMBAR       BTW number is NUMBAR type now (17.0) number R MAEK number YARN    BTW number reassigned to the YARN value of number (“17.0”)` |
| :---- |

### **STATEMENTS                                                                                                                                        \<\<**

#### **Expression Statements**

* The result of an expression may not be assigned to a variable. In this case, its result will be stored in the implicit variable `IT`.

#### **Assignment Statements**

* The assignment operation keyword is `R`.  
* The left-hand side is always a receiving variable, while the right side may be a literal, variable, or an expression.

| `<variable> R <literal>             <variable> R <variable>            <variable> R <expression>`          |
| :---- |

#### **Flow-control Statements**

* LOLCode has two kinds of conditional statements: if-then and switch-case.  
    
  **IF-THEN STATEMENTS**  
* The IF-THEN statement in LOLCode uses five keywords: `O RLY?`, `YA RLY`, `MEBBE`, `NO WAI`, and `OIC`. The syntax for if-then statements is shown below:

| `<expression>                BTW result is stored in IT O RLY?    YA RLY                   BTW if       <if code block>    NO WAI                   BTW else       <else code block> OIC` |
| :---- |


* Indentation is irrelevant.  
* If the `IT` variable can be cast to `WIN`, the if-clause executes. Otherwise, the else-clause executes.  
* Implementing `MEBBE` (else-if) clauses is not required.  
* The if-clause starts at the `YA RLY` keyword and ends when the `NO WAI` or `OIC` keyword is encountered.  
* The else-clause starts at the `NO WAI` keyword and ends when the `OIC` keyword is encountered.  
* You may assume that `O RLY?`, `YA RLY`, `NO WAI`, and `OIC` are alone in their respective lines. `MEBBE`, if implemented, should be followed by an expression in the same line.  
    
  **SWITCH-CASE STATEMENTS**  
* There are four (4) keywords used in a switch-case in LOLCode: `WTF?`, `OMG`, `OMGWTF`, and `OIC`. The syntax for switch-case statements is shown below:

| `WTF?                        BTW uses value in IT OMG <value literal>    <code block> [OMG <value literal>    <code block>...] [OMGWTF    <code block>] OIC` |
| :---- |


* Once `WTF?` is encountered, the value of the implicit `IT` variable is compared to each case, denoted by an `OMG` keyword. If `IT` and the case are equal, the succeeding code block executes until a `GTFO` (break) or an `OIC` keyword is encountered.  
* The cases may be of any literal type (`NUMBR`s, `NUMBAR`s, `YARN`s, and `TROOF`s).  
* The default case is specified by `OMGWTF` and is executed if none of the preceding cases match the value of `IT`. Execution then stops when an `OIC` is encountered.

  **LOOPS**

* Loops in LOLCode follow the form below:

| `IM IN YR <label> <operation> YR <variable> [TIL|WILE <expression>]     <code block> IM OUTTA YR <label>` |
| :---- |


* The `IM IN YR <label>` and `IM OUTTA YR <label>` clauses specify the start and end of the loop. The `<label>` follows the format for a valid variable name, and is used as a delimiter, especially in the case where nested loops are implemented.  
* The `<operation>` can either be `UPPIN` (increment by 1\) or `NERFIN` (decrement by 1), which modifies the `<variable>` that follows.  
* The variable specified in `<variable>` should be an existing variable (i.e., declared) and whose value can be cast to a numerical value so it can be processed by `UPPIN`/`NERFIN`.  
* The loops can be terminated by meeting the condition expressions `TIL`/`WILE` or by issuing a `GTFO` statement inside the loop.  
* The `TIL <expression>` clause will repeat the loop as long as `<expression>` is `FAIL`.  
* The `WILE <expression>` clause will repeat the loop as long as `<expression>` returns `WIN`.

| `I HAS A temp ITZ 2 BTW prints 2 to 9 using TIL IM IN YR print10 UPPIN YR temp TIL BOTH SAEM temp AN 10    VISIBLE temp IM OUTTA YR print10 BTW at this point, temp’s value is 10, so we must reassign its initial value temp R 2 BTW prints 2 to 9 but using WILE IM IN YR print10 UPPIN YR temp WILE DIFFRINT temp AN 10    VISIBLE temp IM OUTTA YR print10` |
| :---- |

### **FUNCTIONS                                                                                                                                              \<\<**

#### **Definition**

* Functions have a fixed number of parameters in the definition.

| `HOW IZ I <function name> [YR <parameter1> [AN YR <parameter2> [AN YR <parameter3> ...]]]   BTW function body IF U SAY SO`         |
| :---- |

* `<parameter1>`, `<parameter2>`, and `<parameter3>` are the parameters of the function. If there are no parameters, then the parameters will be omitted:

| `HOW IZ I sample_function                     BTW function with 0 arguments HOW IZ I sample_function2 YR x AN YR y       BTW function with 2 arguments` |
| :---- |

* Functions cannot access identifiers outside of it. Only the arguments passed are accessible to the function.  
* Arguments are passed via pass-by value only.  
* The parameters in the function become a variable of that function, with the passed argument as the initial value.

#### **Returning**

* `FOUND YR <expression>` returns the value of the expression.  
* `GTFO` returns with no value (NOOB), but if no `GTFO` is found, the return type will also be NOOB automatically.  
* Return values will automatically be stored in the implicit variable `IT`.

#### **Calling**

* Functions can be called using the following syntax:

| `I IZ <function name> [YR <expression1> [AN YR <expression2> AN YR <expression2>]] MKAY` |
| :---- |

* The expressions must be executed first before executing the function body.

### **\>\>                                                                                                                                                                     \<\<**

**The specifications listed here must be followed first. For any other rules not specified here, you may follow the specifications from Github.**

# **Extra Credit**

Implementing anything that is not required in the project will give you bonus pBTWoints. The number of bonus points depends on the level of difficulty of the feature you implement. Possible bonus features are:

| Soft-line/command breaks (,) | Special characters in a YARN (:\>, :), etc) | Loop-nesting | MEBBE |
| :---- | :---- | :---- | :---- |
| Special characters in strings | Line continuation (...) | Else-if clauses | Array |
| Suppress the newline after a line of output by ending the VISIBLE statement with a \! |  |  |  |
| Nesting of different flow control statements |  | If-else nesting | Switch-nesting |

# **Scoring**

Since this is a group project, there will be a peer evaluation at the end of the semester. The peer evaluation score will be directly multiplied by your group’s overall score in the project. You will evaluate each of your group mates AND yourself. Refer to the example below:

| MEMBER | GROUP SCORE | PEER EVAL (Average) | FINAL PROJECT GRADE |
| :---: | :---: | :---: | :---: |
| Carlo | 97.63% | 100% | 97.630 |
| Beili |  | 80% | 78.104 |
| Erika |  | 60% | 58.578 |

The peer evaluation has a big effect on your final project grade. **Be mindful of the contributions you make to the group project and always put your best foot forward** so that your group mates will want to give you the full 100% for their evaluation of your contributions, cooperativity, etc.

The breakdown for computing the project group score is as follows:

| SUB-UNIT |  | POINTS |  | SUB-UNIT |  | POINTS |  |
| ----- | ----- | :---: | :---: | ----- | :---: | :---: | :---: |
| Regular Expressions |  | 10 |  | Operations | Assignment | 2 |  |
| Grammars |  | 10 |  |  | Arithmetic | 3 |  |
| User Input | GIMMEH | 5 |  |  | Comparison | 3 |  |
| User Output | string/literal | 1 |  |  | Boolean | 3 |  |
|  | variable | 2 |  | Typecasting |  | 5 |  |
|  | expression | 3 |  | Switch-Case | OMG | 3 |  |
| Variables | I HAS A | 5 |  |  | OMGWTF | 3 |  |
|  | ITZ literal | 2 |  |  | GTFO | 3 |  |
|  | ITZ expr | 3 |  | Loops | Delimiter | 2 |  |
| If-Else | YA RLY | 3 |  |  | UPPIN/NERFIN | 3 |  |
|  | NO WAI | 3 |  |  | TIL | 4 |  |
| Milestone Presentations(5 points each) |  | 15 |  |  | WILE | 4 |  |
|  |  |  |  | Functions | Definition | 3 |  |
|  |  |  |  |  | Return | 3 |  |
|  |  |  |  |  | Calling | 2 |  |
|  | **TOTAL** | **62** | \+ | **TOTAL** |  | **46** |  |
|  |  |  |  | **GRAND TOTAL** |  | **108** |  |

# **Submission Format**

* **You may use any programming language** that you want.   
* A **Graphical User Interface (GUI) is required** and should look similar to the diagram below:

![][image1]

* The parts of the GUI are as follows:  
  * **(1) File explorer –** Allows you to select a file to run. Once a file is selected, the contents of the file should be loaded into the text editor (2).  
  * **(2) Text editor –** Allows you to view the code you want to run. The text editor should be editable, and edits done should be reflected once the code is run.  
  * **(3) List of Tokens –** This should be updated every time the Execute/Run button (5) is pressed. This should contain all the lexemes detected from the code being ran, and their classification.  
  * **(4) Symbol Table –** This should be updated every time the Execute/Run button (5) is pressed. This should contain all the variables available in the program being ran, and their updated values.  
  * **(5) Execute/Run button –** This will run the code from the text editor (2).  
  * **(6) Console –** Input/Output of the program should be reflected in the console. For variable input, you can add a separate field for user input, or have a dialog box pop up.  
* For (3) and (4) in the GUI, you can either: a) update the list/table every time a line is read, or (b) update the list of tokens one time, and the symbol table every time a value is updated.  
* You are **NOT ALLOWED** **to use Flex/Lex or YACC/Bison or Parsing Expression Grammars (PEG) or any lexer/parser generator tools**. You are required to implement your own lexical and syntax analyzer.  
    
* The zipped file of your codebase will be uploaded in the classroom.  
* A document containing detailed instructions for submission and presentation will be posted separately.

[image1]: <data:image/png;base64,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>