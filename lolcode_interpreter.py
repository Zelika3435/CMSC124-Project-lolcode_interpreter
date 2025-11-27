# Ordered by precedence
LOLCODE_TOKENS = [
    # 1. IGNORE TOKENS (Comments and Whitespace)
    ('SKIP',         r'[\t\r]+'),         # Skip spaces, tabs, carriage returns
    ('NEWLINE',      r'\n'),               # Newline (important for single-line comments/statement termination)
    ('BTW_COMMENT',  r'BTW.*'),            # Single-line comment (BTW followed by anything)
    ('OBTW',         r'OBTW'),             # Block comment start
    ('TLDR',         r'TLDR'),             # Block comment end

    # 2. KEYWORDS (Exact Matches - Highest Precedence)
    # Match multi-word keywords first
    ('I_HAS_A',      r'I\s+HAS\s+A'),
    ('SUM_OF',       r'SUM\s+OF'),
    ('DIFF_OF',      r'DIFF\s+OF'),
    ('PRODUKT_OF',   r'PRODUKT\s+OF'),
    ('QUOSHUNT_OF',  r'QUOSHUNT\s+OF'),
    ('MOD_OF',       r'MOD\s+OF'),
    ('BIGGR_OF',     r'BIGGR\s+OF'),
    ('SMALLR_OF',    r'SMALLR\s+OF'),
    ('BOTH_OF',      r'BOTH\s+OF'),
    ('EITHER_OF',    r'EITHER\s+OF'),
    ('WON_OF',       r'WON\s+OF'),
    ('ANY_OF',       r'ANY\s+OF'),
    ('ALL_OF',       r'ALL\s+OF'),
    ('BOTH_SAEM',    r'BOTH\s+SAEM'),
    ('IS_NOW_A',     r'IS\s+NOW\s+A'),
    ('O_RLY',        r'O\s+RLY\?'),
    ('YA_RLY',       r'YA\s+RLY'),
    ('NO_WAI',       r'NO\s+WAI'),
    ('IM_IN_YR',     r'IM\s+IN\s+YR'),
    ('IM_OUTTA_YR',  r'IM\s+OUTTA\s+YR'),
    ('HOW_IZ_I',     r'HOW\s+IZ\s+I'),
    ('IF_U_SAY_SO',  r'IF\s+U\s+SAY\s+SO'),
    ('FOUND_YR',     r'FOUND\s+YR'),
    ('I_IZ',         r'I\s+IZ'),

    # Match single-word keywords
    ('HAI',          r'HAI'),
    ('KTHXBYE',      r'KTHXBYE'),
    ('WAZZUP',       r'WAZZUP'),
    ('BUHBYE',       r'BUHBYE'),
    ('ITZ',          r'ITZ'),
    ('R',            r'R'),
    ('NOT',          r'NOT'),
    ('DIFFRINT',     r'DIFFRINT'),
    ('SMOOSH',       r'SMOOSH'),
    ('MAEK',         r'MAEK'),
    ('AN',           r'\bAN\b'),
    ('A',            r'A'),
    ('VISIBLE',      r'VISIBLE'),
    ('GIMMEH',       r'GIMMEH'),
    ('OIC',          r'OIC'),
    ('WTF',          r'WTF\?'),
    ('OMGWTF',       r'OMGWTF'),
    ('OMG',          r'OMG'),
    ('UPPIN',        r'UPPIN'),
    ('NERFIN',       r'NERFIN'),
    ('YR',           r'YR'),
    ('TIL',          r'TIL'),
    ('WILE',         r'WILE'),
    ('GTFO',         r'GTFO'),
    ('MEBBE',        r'MEBBE'),
    ('MKAY',         r'MKAY'),
    ('PLUS',         r'\+'),

    # 3. LITERALS (Values)
    # NUMBAR must be before NUMBR to match the decimal point first
    # The '".*"' regex for YARN is simplified; a full lexer would handle escaped quotes
    # Support both curly quotes (") and straight quotes (")
    ('YARN_LITERAL', r'[""].*?[""]'),
    ('NUMBAR_LITERAL', r'-?[0-9]+\.[0-9]+'),
    ('NUMBR_LITERAL', r'-?[0-9]+'),
    ('TROOF_LITERAL', r'WIN|FAIL'),
    ('TYPE_LITERAL', r'NOOB|NUMBR|NUMBAR|YARN|TROOF'),

    # 4. IDENTIFIERS (User-Defined Names - Lowest Precedence)
    # It covers Variable, Function, and Loop identifiers
    ('IDENTIFIER',   r'[A-Za-z][A-Za-z0-9_]*'),

    # 5. ERROR (Catch-all for invalid characters)
    ('ERROR',        r'.'),
]

import re

def lolcode_lexer(code):
    """
    Tokenizes the input LOLCODE string based on the defined specifications.

    Args:
        code (str): The raw LOLCODE source code.

    Yields:
        tuple: (token_type, token_value) for each recognized token.
    """
    position = 0
    code_length = len(code)

    # 1. Pre-compile all regular expressions for efficiency
    token_patterns = [(token_type, re.compile(pattern)) for token_type, pattern in LOLCODE_TOKENS]

    while position < code_length:
        match_found = False

        # 2. Iterate through patterns in ORDER OF PRECEDENCE
        for token_type, pattern in token_patterns:
            # Try to match the pattern starting from the current position
            match = pattern.match(code, position)

            if match:
                value = match.group(0) # Get the matched string

                # 3. Handle 'SKIP' and 'NEWLINE' tokens
                if token_type in ('SKIP', 'NEWLINE'):
                    # These tokens are consumed but not yielded to the parser
                    pass

                # 4. Handle Block Comments
                elif token_type == 'OBTW':
                    # Find the corresponding 'TLDR' end marker
                    end_match = re.search(r'TLDR', code[position:])
                    if end_match:
                        # Consume the OBTW, the comment body, and TLDR
                        position += end_match.end()
                    else:
                        # Error: Unclosed block comment
                        raise SyntaxError(f"Unclosed OBTW block starting at position {position}")
                    # Don't yield comment content

                # 5. Handle Single-Line Comments
                elif token_type == 'BTW_COMMENT':
                    # Consume the comment and ignore it
                    pass

                # 6. Yield all other meaningful tokens (Keywords, Literals, Identifiers)
                elif token_type != 'ERROR':
                    yield (token_type, value)

                # Move the position past the consumed token
                position = match.end()
                match_found = True
                break # IMPORTANT: Exit the inner loop after a match is found

        # 7. Handle Unmatched Input (Error)
        if not match_found:
            # If no pattern matched, it's an unrecognized character/sequence
            char = code[position]
            raise SyntaxError(f"Illegal character '{char}' at position {position}")
            # position += 1 # Or continue/exit based on error strategy

    # Optional: Yield an End-of-File token (EOF)
    yield ('EOF', None)


def parse_lolcode(code):
    """
    Parse LOLCODE source code into an AST
    """
    tokens = list(lolcode_lexer(code))
    
    # Parser state (using lists to allow mutation in closures)
    tokens_list = tokens
    position = [0]
    current_token = [None]
    
    # Token type mappings
    ARITHMETIC_TOKENS = {
        'SUM_OF': 'SUM',
        'DIFF_OF': 'DIFF',
        'PRODUKT_OF': 'PRODUKT',
        'QUOSHUNT_OF': 'QUOSHUNT',
        'MOD_OF': 'MOD',
    }
    
    RELATIONAL_TOKENS = {
        'BIGGR_OF': 'BIGGR',
        'SMALLR_OF': 'SMALLR',
    }
    
    BOOLEAN_BINARY_TOKENS = {
        'BOTH_OF': 'BOTH',
        'EITHER_OF': 'EITHER',
        'WON_OF': 'WON',
    }
    
    BOOLEAN_LIST_TOKENS = {
        'ALL_OF': 'ALL',
        'ANY_OF': 'ANY',
    }
    
    COMPARISON_TOKENS = {
        'BOTH_SAEM': 'BOTH_SAEM',
        'DIFFRINT': 'DIFFRINT',
    }

    # ------------------------------------------------------------------
    # Basic token utilities (closures)
    # ------------------------------------------------------------------
    def next_token():
        if position[0] < len(tokens_list):
            current_token[0] = tokens_list[position[0]]
            position[0] += 1
        else:
            current_token[0] = ('EOF', None)
        return current_token[0]

    def peek_token():
        if position[0] < len(tokens_list):
            return tokens_list[position[0]]
        return ('EOF', None)

    def match(token_type):
        return current_token[0][0] == token_type

    def expect(token_type):
        if not match(token_type):
            raise SyntaxError(
                f"Expected {token_type}, got {current_token[0][0]} at position {position[0]}"
            )
        token = current_token[0]
        next_token()
        return token

    def save():
        return position[0], current_token[0]

    def restore(snapshot):
        position[0], current_token[0] = snapshot

    # Initialize
    next_token()
    
    # ------------------------------------------------------------------
    # Grammar productions (all as nested functions)
    # ------------------------------------------------------------------
    def program():
        expect('HAI')
        code_block_result = code_block()
        expect('KTHXBYE')
        return {'type': 'program', 'code_block': code_block_result}

    def code_block():
        if match('WAZZUP'):
            var_decls = var_declaration_block()
            statements = statement_list()
            return {'var_declarations': var_decls, 'statements': statements}
        statements = statement_list()
        return {'statements': statements}

    def var_declaration_block():
        expect('WAZZUP')
        declarations = var_declaration_list()
        expect('BUHBYE')
        return declarations

    def var_declaration_list():
        declarations = [var_declaration()]
        while match('I_HAS_A'):
            declarations.append(var_declaration())
        return declarations

    def var_declaration():
        expect('I_HAS_A')
        var_token = expect('IDENTIFIER')
        if match('ITZ'):
            expect('ITZ')
            if is_literal_token():
                value = literal()
            elif match('IDENTIFIER'):
                value = identifier()
            elif match('I_IZ'):
                value = function_call()
            else:
                value = expr()
            return {'type': 'var_declaration', 'var': var_token[1], 'value': value}
        return {'type': 'var_declaration', 'var': var_token[1], 'value': None}

    def statement_list():
        statements = [statement()]
        while not match_any({'EOF', 'OIC', 'IM_OUTTA_YR', 'NO_WAI', 'MEBBE', 'OMG', 'OMGWTF', 'BUHBYE', 'KTHXBYE', 'IF_U_SAY_SO'}):
            statements.append(statement())
        return statements

    def statement():
        if match('I_HAS_A'):
            return var_declaration()
        if match('IDENTIFIER') and peek_token()[0] == 'R':
            return assignment()
        if match('VISIBLE'):
            return print_statement()
        if match('GIMMEH'):
            return input_statement()
        if match('WTF'):
            return switch_statement()
        if match('IM_IN_YR'):
            return loop_statement()
        if match('I_IZ'):
            return function_call()
        if match('HOW_IZ_I'):
            return function_definition()
        if match('FOUND_YR') or match('GTFO'):
            return return_statement()
        if match('IDENTIFIER') and peek_token()[0] == 'IS_NOW_A':
            return typecast_statement()
        if match('BTW_COMMENT') or match('OBTW'):
            return comment()

        snapshot = save()
        try:
            expr_result = expr()
            if match('O_RLY'):
                return if_statement_with_condition(expr_result)
            return expr_result
        except:
            restore(snapshot)
            raise

    def assignment():
        target = expect('IDENTIFIER')[1]
        expect('R')
        if is_literal_token():
            value = literal()
        elif match('IDENTIFIER'):
            value = identifier()
        elif match('I_IZ'):
            value = function_call()
        else:
            value = expr()
        return {'type': 'assignment', 'var': target, 'value': value}

    def print_statement():
        expect('VISIBLE')
        items = [print_item()]
        while match('PLUS'):
            expect('PLUS')
            items.append(print_item())
        return {'type': 'print', 'items': items}

    def print_item():
        if match('IDENTIFIER'):
            return identifier()
        if is_literal_token():
            return literal()
        return expr()

    def input_statement():
        expect('GIMMEH')
        var_name = expect('IDENTIFIER')[1]
        return {'type': 'input', 'var': var_name}

    def typecast_statement():
        var_name = expect('IDENTIFIER')[1]
        expect('IS_NOW_A')
        target_type = expect('TYPE_LITERAL')[1]
        return {'type': 'typecast', 'var': var_name, 'target_type': target_type}

    def comment():
        if match('BTW_COMMENT'):
            expect('BTW_COMMENT')
            return {'type': 'comment'}
        expect('OBTW')
        while not match('TLDR') and not match('EOF'):
            next_token()
        expect('TLDR')
        return {'type': 'comment'}

    # ------------------------------------------------------------------
    # Expressions
    # ------------------------------------------------------------------
    def expr():
        token_type = current_token[0][0]
        if token_type in ARITHMETIC_TOKENS:
            return arithmetic_expr()
        if token_type in RELATIONAL_TOKENS:
            return relational_expr()
        if token_type in BOOLEAN_BINARY_TOKENS:
            return boolean_binary_expr()
        if token_type in BOOLEAN_LIST_TOKENS:
            return boolean_list_expr()
        if token_type == 'NOT':
            return boolean_not_expr()
        if token_type in COMPARISON_TOKENS:
            return comparison_expr()
        if token_type == 'SMOOSH':
            return concatenation_expr()
        if token_type == 'MAEK':
            return typecast_expr()
        if is_literal_token():
            return literal()
        if token_type == 'IDENTIFIER':
            return identifier()
        raise SyntaxError(f"Unexpected token {token_type} in expression")

    def arithmetic_expr():
        op_token = current_token[0][0]
        op_name = ARITHMETIC_TOKENS[op_token]
        expect(op_token)
        left = operand()
        expect('AN')
        right = operand()
        return {'type': 'arithmetic_expr', 'operator': op_name, 'left': left, 'right': right}

    def relational_expr():
        op_token = current_token[0][0]
        op_name = RELATIONAL_TOKENS[op_token]
        expect(op_token)
        left = operand()
        expect('AN')
        right = operand()
        return {'type': 'relational_expr', 'operator': op_name, 'left': left, 'right': right}

    def boolean_binary_expr():
        op_token = current_token[0][0]
        op_name = BOOLEAN_BINARY_TOKENS[op_token]
        expect(op_token)
        left = operand()
        expect('AN')
        right = operand()
        return {'type': 'boolean_expr', 'operator': op_name, 'left': left, 'right': right}

    def boolean_list_expr():
        op_token = current_token[0][0]
        op_name = BOOLEAN_LIST_TOKENS[op_token]
        expect(op_token)
        operands = operand_list()
        expect('MKAY')
        return {'type': 'boolean_expr', 'operator': op_name, 'operands': operands}

    def boolean_not_expr():
        expect('NOT')
        operand_val = operand()
        return {'type': 'boolean_expr', 'operator': 'NOT', 'operand': operand_val}

    def comparison_expr():
        op_token = current_token[0][0]
        op_name = COMPARISON_TOKENS[op_token]
        expect(op_token)
        left = operand()
        expect('AN')
        if match('BIGGR_OF') or match('SMALLR_OF'):
            right = relational_expr()
        else:
            right = operand()
        return {'type': 'comparison_expr', 'operator': op_name, 'left': left, 'right': right}

    def concatenation_expr():
        expect('SMOOSH')
        operands = operand_list()
        return {'type': 'concatenation_expr', 'operands': operands}

    def typecast_expr():
        expect('MAEK')
        var_name = expect('IDENTIFIER')[1]
        if match('A'):
            expect('A')
        target_type = expect('TYPE_LITERAL')[1]
        return {'type': 'typecast_expr', 'var': var_name, 'target_type': target_type}

    def operand():
        if is_literal_token():
            return literal()
        if match('IDENTIFIER'):
            return identifier()
        if match('I_IZ'):
            return function_call()
        return expr()

    def operand_list():
        operands = [operand()]
        while match('AN'):
            expect('AN')
            operands.append(operand())
        return operands

    def literal():
        if match('NUMBR_LITERAL'):
            value = int(expect('NUMBR_LITERAL')[1])
            return {'type': 'literal', 'value': value, 'literal_type': 'NUMBR'}
        if match('NUMBAR_LITERAL'):
            value = float(expect('NUMBAR_LITERAL')[1])
            return {'type': 'literal', 'value': value, 'literal_type': 'NUMBAR'}
        if match('YARN_LITERAL'):
            raw = expect('YARN_LITERAL')[1]
            return {'type': 'literal', 'value': raw[1:-1], 'literal_type': 'YARN'}
        if match('TROOF_LITERAL'):
            value = expect('TROOF_LITERAL')[1] == 'WIN'
            return {'type': 'literal', 'value': value, 'literal_type': 'TROOF'}
        raise SyntaxError(f"Unexpected token {current_token[0][0]} as literal")

    def identifier():
        return {'type': 'identifier', 'name': expect('IDENTIFIER')[1]}

    def is_literal_token():
        return match('NUMBR_LITERAL') or match('NUMBAR_LITERAL') or match('YARN_LITERAL') or match('TROOF_LITERAL')

    def match_any(token_set):
        return current_token[0][0] in token_set

    # ------------------------------------------------------------------
    # Control flow
    # ------------------------------------------------------------------
    def if_statement():
        condition = expr()
        return if_statement_with_condition(condition)

    def if_statement_with_condition(condition):
        expect('O_RLY')
        if_block_result = if_block()
        if match('OIC'):
            expect('OIC')
            return {'type': 'if_statement', 'condition': condition, 'if_block': if_block_result}
        else_chain_result = else_chain()
        expect('OIC')
        return {'type': 'if_statement', 'condition': condition, 'if_block': if_block_result, 'else_chain': else_chain_result}

    def if_block():
        expect('YA_RLY')
        return statement_list()

    def else_chain():
        result = {}
        if match('MEBBE'):
            result['elseif_list'] = elseif_list()
        if match('NO_WAI'):
            result['else_block'] = else_block()
        return result

    def elseif_list():
        blocks = []
        while match('MEBBE'):
            blocks.append(elseif_block())
        return blocks

    def elseif_block():
        expect('MEBBE')
        condition = expr()
        statements = statement_list()
        return {'condition': condition, 'statements': statements}

    def else_block():
        expect('NO_WAI')
        return statement_list()

    def switch_statement():
        expect('WTF')
        cases = case_list()
        default_block = None
        if match('OMGWTF'):
            default_block = default_case()
        expect('OIC')
        node = {'type': 'switch_statement', 'cases': cases}
        if default_block is not None:
            node['default'] = default_block
        return node

    def case_list():
        cases = []
        while match('OMG'):
            cases.append(case_block())
        return cases

    def case_block():
        expect('OMG')
        case_literal = literal()
        statements = statement_list()
        has_gtfo = False
        if match('GTFO'):
            expect('GTFO')
            has_gtfo = True
        return {'literal': case_literal, 'statements': statements, 'has_gtfo': has_gtfo}

    def default_case():
        expect('OMGWTF')
        return statement_list()

    def loop_statement():
        expect('IM_IN_YR')
        loop_name = expect('IDENTIFIER')[1]
        operation = loop_operation()
        expect('YR')
        var_name = expect('IDENTIFIER')[1]
        condition = None
        if match('TIL') or match('WILE'):
            condition = loop_condition()
        statements = statement_list()
        expect('IM_OUTTA_YR')
        expect('IDENTIFIER')  # consume loop identifier
        node = {'type': 'loop_statement', 'loop_id': loop_name, 'operation': operation, 'var': var_name, 'statements': statements}
        if condition is not None:
            node['condition'] = condition
        return node

    def loop_operation():
        if match('UPPIN'):
            expect('UPPIN')
            return 'UPPIN'
        if match('NERFIN'):
            expect('NERFIN')
            return 'NERFIN'
        raise SyntaxError(f"Expected loop operation, got {current_token[0][0]}")

    def loop_condition():
        if match('TIL'):
            expect('TIL')
            return {'type': 'TIL', 'expr': expr()}
        if match('WILE'):
            expect('WILE')
            return {'type': 'WILE', 'expr': expr()}
        raise SyntaxError(f"Expected loop condition, got {current_token[0][0]}")

    def function_definition():
        expect('HOW_IZ_I')
        func_name = expect('IDENTIFIER')[1]
        parameters = []
        if match('YR'):
            parameters = parameter_list()
        statements = statement_list()
        expect('IF_U_SAY_SO')
        return {'type': 'function_definition', 'name': func_name, 'parameters': parameters, 'statements': statements}

    def parameter_list():
        params = []
        while True:
            expect('YR')
            params.append(expect('IDENTIFIER')[1])
            if not match('AN'):
                break
            expect('AN')
        return params

    def function_call():
        expect('I_IZ')
        func_name = expect('IDENTIFIER')[1]
        args = []
        if match('YR'):
            args = argument_list()
        expect('MKAY')
        return {'type': 'function_call', 'name': func_name, 'args': args}

    def argument_list():
        args = []
        while True:
            expect('YR')
            args.append(expr())
            if not match('AN'):
                break
            expect('AN')
        return args

    def return_statement():
        if match('FOUND_YR'):
            expect('FOUND_YR')
            return {'type': 'return_statement', 'value': expr()}
        expect('GTFO')
        return {'type': 'return_statement', 'value': None}

    # Call program() to start parsing
    return program()


# Read SAMPLE_INPUT from unzipped test case files
import os
import glob

def get_sample_input():
    testcases_dir = os.path.join(os.path.dirname(__file__), "testfiles")
    
    # Find all .lol files in the test cases directory
    lol_files = glob.glob(os.path.join(testcases_dir, "*.lol"))
    
    if not lol_files:
        # Fallback if directory structure is different
        return ""
    
    # Sort files to get them in order (01_variables.lol, 02_gimmeh.lol, etc.)
    lol_files.sort()
    
    # Read the first test case file by default
    with open(lol_files[0], 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    tokens = list(lolcode_lexer(get_sample_input()))
    print("Tokens:")
    print(tokens)
    print("\nAST:")
    import json
    print(json.dumps(parse_lolcode(get_sample_input()), indent=2))