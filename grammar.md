## LOLCODE GRAMMAR

Use angle brackets (<,>) to denote abstractions. Type lexemes that have been defined in Project
Requirement 01 using lowercase letters. If the lexemes have not yet been defined, add the newly defined
lexemes at the last section of this document.

## LHS ::= RHS

```
<program> ::= hai <linebreak> <statement> <linebreak>
kthxbye
<literal> ::= numbr | numbar | yarn | troof
<linebreak> ::= newline | newline <linebreak>
<code_block> ::= <var_declaration_block> <statement_list> |
<statement_list>
<var_declaration_block
>
```
```
::= wazzup <linebreak> <var_declaration_list>
<linebreak> buhbye <linebreak>
<var_declaration_list> ::= <var_declaration> | <var_declaration>
<linebreak> <var_declaration_list>
<statement_list> ::= <statement> | <statement> <linebreak>
<statement_list>
<var_declaration> ::= i has a varident | i has a varident itz
<literal> | i has a varident itz varident | i
has a varident itz <expr>
<statement> ::= <assignment> | <print> | <input> |
<if_statement> | <switch_statement> |
<loop_statement> | <function_call> |
<typecast_statement> | <expr> | <comment>
<comment> ::= btw <text> | <linebreak> obtw <linebreak>
<text_block> <linebreak> tldr
<text_block> ::= <text> | <text> <linebreak> <text_block>
<assignment> ::= varident r <literal> | varident r varident |
varident r <expr>
<typecast_statement> ::= varident is now a type
<print> ::= visible <print_list>
<print_list> ::= <print_item> | <print_item> + <print_list>
<print_item> ::= varident | <literal> | <expr>
<input> ::= gimmeh varident
```

**LOLCODE Grammar Project Requirement 02**

```
<expr> ::= <arithmetic_expr> | <relational_expr> |
<boolean_expr> | <comparison_expr> |
<concatenation_expr> | <typecast_expr>
<arithmetic_expr> ::= sum of <operand> AN <operand> | diff of
<operand> AN <operand> | produkt of <operand>
AN <operand> | quoshunt of <operand> AN
<operand> | mod of <operand> AN <operand>
<relational_expr> ::= biggr of <operand> AN <operand> | smallr of
<operand> AN <operand>
<boolean_expr> ::= both of <operand> AN <operand> | either of
<operand> AN <operand> | won of <operand> AN
<operand> | not <operand> | all of
<operand_list> mkay | any of <operand_list>
mkay
<comparison_expr> ::= both saem <operand> AN <operand> | diffrint
<operand> AN <operand> | both saem <operand>
AN <relational_expr> | diffrint <operand> and
<relational_expr>
<concatenation_expr> ::= smoosh <operand_list>
<typecast_expr> ::= maek varident a type | maek varident type
<operand> ::= <literal> | varident | <expr>
<operand_list> ::= <operand> AN <operand> | <operand> AN
<operand_list>
<if_statement> ::= <expr> <linebreak> o rly? <linebreak>
<if_block> oic | <expr> <linebreak> o rly?
<linebreak> <if_block> <else_chain> oic
<if_block> ::= ya rly <linebreak> <statement_list>
<linebreak>
<else_chain> ::= <elseif_list> <else_block> | <elseif_list> |
<else_block>
<elseif_list> ::= <elseif_block> | <elseif_block> <elseif_list>
<elseif_block> ::= mebbe <expr> <linebreak> <statement_list>
<linebreak>
<else_block> ::= no wai <linebreak> <statement_list>
<linebreak>
<switch_statement> ::= wtf? <linebreak> <case_list> oic | wtf?
<linebreak> <case_list> <default_case> oic
<case_list> ::= <case_block> | <case_block> <case_list>
<case_block> ::= omg <literal> <linebreak> <statement_list>
<linebreak> | omg <literal> <linebreak>
<statement_list> <linebreak> gtfo <linebreak>
<default_case> ::= omgwtf <linebreak> <statement_list>
```

**LOLCODE Grammar Project Requirement 02**

```
<linebreak>
<loop_statement> ::= im in yr loopident <loop_operation> yr
varident <linebreak> <statement_list>
<linebreak> im outta yr loopident | im in yr
loopident <loop_operation> yr varident
<loop_condition> <linebreak> <statement_list>
<linebreak> im outta yr loopident
<loop_operation> ::= uppin | nerfin
<loop_condition> ::= til <expr> | wile <expr>
<function_definition> ::= how iz i funcident <linebreak>
<statement_list> <linebreak> if u say so | how
iz i funcident <parameter_list> <linebreak>
<statement_list> <linebreak> if u say so
<parameter_list> ::= yr varident | yr varident AN <parameter_list>
<function_call> ::= i iz funcident mkay | i iz funcident
<argument_list> mkay
<argument_list> ::= yr <expr> | yr <expr> AN <argument_list>
<return_statement> ::= found yr <expr> | gtfo
```
**NEWLY-ADDED LEXEMES**
Put here the definition of the lexemes that have not yet been defined in Project Requirement 01.

```
LEXEME Regular Expression
newline ^\n$
AN ^AN$
<text> [^\n]*
```

