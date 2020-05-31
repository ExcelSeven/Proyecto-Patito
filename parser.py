import ply.yacc as yacc
import ply.lex as lex
from lexer import tokens
import lexer
import math
from program import Program
from patType import PatType
from varTable import Var
from varTable import VarTable
from tablaConstantes import Constante
from tablaConstantes import TablaConstantes
from functionDirectory import Function
from functionDirectory import FunctionDirectory
import sys


program = Program()
error_message = '\033[91m' + "ERROR: " + '\033[0m'
error = False

v = Var
vt = VarTable()


def p_programa(p):
    """
    programa : PROGRAM ID SEMICOL programa1
    """
    p[0] = 'Compilacion Exitosa'
    print(p[0])


def p_programa1(p):
    """
    programa1 : vars funcion main funcion
              | funcion main funcion
              | vars funcion
              | funcion
              | empty
    """

####### Main ##########################################################

def p_main(p):
    """
    main : MAIN LP RP LB statement RB
    """
    print("MAIN ok")


def p_statement(p):
    """
    statement : asignacion SEMICOL statement
              | if statement
              | vars statement
              | p_operacion statement
              | oper_aritmetica statement
              | empty
    """
    ## FALTA: llamada, lectura, escritura, for, if, while


def p_asignacion(p):
    """
    asignacion : ID IS value
    """
    v1 = vars(v(p[1], 'int', p[3], scope))
    vt.set(p[1], v1)

    ## FALTA:   ID arreglo IS value
    ##        | ID matrix IS value


####### Variables Locales ################################################

global scope
scope = 'local'

def p_vars(p):
    """
    vars : VAR tipo vars1
         | VAR tipo vars2
         | VAR tipo vars3
         | VAR tipo vars4
         | VAR tipo oper_aritmetica
         | varsG
         | empty
    """

# var int a;
def p_vars1(p):
    """
    vars1 : ID SEMICOL
          | ID SEMICOL vars
    """
    global tipo
    v1 = vars(v(p[1], p[-1], 'N', scope))
    #print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))



# var int a = 5;
def p_vars2(p):
    """
    vars2 : ID IS value SEMICOL
          | ID IS value SEMICOL vars
    """
    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error>", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error> ", p[3], " No es un float!")
        # sys.exit(0)
    else:
        v1 = vars(v(p[1], p[-1], p[3], scope))
        vt.__set__(p[1], v1)
        #print('Vars >> ', v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))

# var int a,b,c;
def p_vars3(p):
    """
    vars3 : ID COMMA vars3
          | ID SEMICOL vars
          | ID SEMICOL
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, 'N', scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a=0, b=1, c=2;
def p_vars4(p):
    """
    vars4 : ID IS value check_type COMMA vars4
          | ID IS value check_type SEMICOL vars
          | ID IS value check_type SEMICOL
          | empty
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, p[3], scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], p[3], scope))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))

# a=2;
# def p_vars5(p):
#     """
#     vars5 : ID IS value SEMICOL
#           | ID IS value SEMICOL vars
#     """
#     tipos = 'int'
#     v1 = vars(v(p[1], tipos, p[3], scope))
#     #print('Vars >> ', v1)
#     vt.__set__(p[1], v1)
#     #print("VarTable >>  ", vt.__getitem__(p[1]))


####### END Variables Locales ################################################

####### Variables Globales ################################################
global scope_G
scope_G = 'global'

def p_varsG(p):
    """
    varsG : VAR tipo vars1G
         | VAR tipo vars2G
         | VAR tipo vars3G
         | VAR tipo vars4G
         | VAR LB varsG RB
    """

# var int a;
def p_vars1G(p):
    """
    vars1G : ID SEMICOL
          | ID SEMICOL varsG
    """
    global tipo
    v1 = vars(v(p[1], p[-1], 'N', scope_G))
   # print('Vars >> ', v1)
    vt.__set__(p[1], v1)
    #print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a = 5;
def p_vars2G(p):
    """
    vars2G : ID IS value check_type SEMICOL
          | ID IS value check_type SEMICOL varsG
    """

    if p[-1] == 'int' and isinstance(p[3], int) is False:
        print("Error>", p[3], " No es un int!")
        # sys.exit(0)
    elif p[-1] == 'float' and isinstance(p[3], float) is False:
        print("Error> ", p[3], " No es un float!")
        # sys.exit(0)
    else:
        v1 = vars(v(p[1], p[-1], p[3], scope))
        vt.__set__(p[1], v1)
        # print('Vars >> ', v1)
        # print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a,b,c;
def p_vars3G(p):
    """
    vars3G : ID COMMA vars3G
          | ID SEMICOL varsG
          | ID SEMICOL
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, 'N', scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], 'N', scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))


# var int a=0, b=1, c=2;
def p_vars4G(p):
    """
    vars4G : ID IS value check_type COMMA vars4G
          | ID IS value check_type SEMICOL varsG
          | ID IS value check_type SEMICOL
          | empty
    """
    global tipos
    if p[-1] == ',':
        tipos = 'int'
        v1 = vars(v(p[1], tipos, p[3], scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        #print("VarTable >>  ", vt.__getitem__(p[1]))
    else:
        tipos = p[-1]
        v1 = vars(v(p[1], p[-1], p[3], scope_G))
        #print('Vars >> ', v1)
        vt.__set__(p[1], v1)
        # print("VarTable >>  ", vt.__getitem__(p[1]))

# a=2;
# def p_vars5G(p):
#     """
#     vars5G : ID IS value SEMICOL
#           | ID IS value SEMICOL varsG
#     """
#     tipos = 'int'
#     v1 = vars(v(p[1], tipos, p[3], scope_G))
#     #print('Vars >> ', v1)
#     vt.__set__(p[1], v1)
#     #print("VarTable >>  ", vt.__getitem__(p[1]))

########## END Variables Globales ###############################################

def p_tipo(p):
    """
    tipo : INT
        | FLOAT
        | CHAR
    """
    p[0] = p[1]
    global tipo
    tipo = p[0]


c = Constante
tc = TablaConstantes()
listaV = list()
def p_value_constantes(p):
    """
    value : CTE_F
          | CTE_I
    """
    p[0] = p[1]

    if isinstance(p[1], int):
        c1 = vars(c('int', p[1]))
        tc.__set__(p[1], c1)
    else: # isinstance(p[1], float):
        c1 = vars(c('float', p[1]))
        tc.__set__(p[1], c1)
    # print(vars(tc))

    ## FALTA : if ID no existe en la tabla de variables, error.
    #if encuentra la variable de p[1], entonces p[0] = .valor


def p_value_id(p):
    """
    value : ID
    """
    p[0] = p[1]

def p_value_char(p):
    """
    value : CTE_C
    """
    p[0] = p[1]

def p_value_char2(p):
    """
    value : COMILLA ID COMILLA
          | COMILLAS ID COMILLAS
    """
    p[0] = p[2]
    if len(p[2]) > 1 or p[2].isalpha() is False:
        print("No es un char!")
        # sys.exit(0)


def p_check_type(p):
    """
    check_type :
    """
    # print("check_type >> ", p[-8])


####### Funciones ##########################################################

f = Function
fd = FunctionDirectory()

def p_funcion(p):
    """
    funcion : VOID ID LP param RP LB statement RB funcion
             | VOID ID LP param RP LB statement RB
             | tipo ID LP param RP LB statement RB funcion
             | tipo ID LP param RP LB statement RB
    """
    p[0] = p[2]

    fd.__set__(p[2], f(p[2], p[1], vars(vt)))
    print("Funciones >> ", vars(fd.__getitem__(p[2])))

def p_param(p):
    """
    param :
    """

def p_calc(p):
    """
    calc : expr
         | asignacion
         | empty
         | row
         | matrix
    """
    print(p_operacion(p[1]))
    print(p[1])
    return p_operacion(p[1])



pila = list()

def p_LT(p):
    """
    var_lt : expr LT expr
    """
    if p[1] < p[3]:
        p[0] = True
    else:
        p[0] = False

def p_GT(p):
    """
    var_gt : expr GT expr
    """
    if p[1] > p[3]:
        p[0] = True
    else:
        p[0] = False

def p_LEQ(p):
    """
    var_leq : expr LEQ expr
    """
    if p[1] <= p[3]:
        p[0] = True
    else:
        p[0] = False

def p_GEQ(p):
    """
    var_geq : expr GEQ expr
    """
    if p[1] >= p[3]:
        p[0] = True
    else:
        p[0] = False

def p_EQUAL(p):
    """
    var_equal : expr EQUAL expr
    """
    if p[1] == p[3]:
        p[0] = True
    else:
        p[0] = False

def p_NEQ(p):
    """
    var_neq : expr NEQ expr
    """
    # p[0] = ('<', p[1], p[3])
    if p[1] != p[3]:
        p[0] = True
    else:
        p[0] = False

####### OPERACIONES ARITMETICAS ##########################################

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV')
)

def p_oper_aritmetica(p):
    """
    oper_aritmetica : ID IS expr SEMICOL

    """
    print("FINAL  ", p[3])

def p_expr(p):
    """
    expr : expr MUL expr
         | expr DIV expr
         | expr PLUS expr
         | expr MINUS expr
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    if p[2] == '-':
        p[0] = p[1] - p[3]
    if p[2] == '*':
        p[0] = p[1] * p[3]
    if p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_int_float(p):
    """
    expr : CTE_I
         | CTE_F
    """
    p[0] = p[1]


####### END OPERACIONES ARITMETICAS ##########################################

def p_expression_var(p):
    """
    expr : ID
         | ID row
         | ID matrix
    """
    p[0] = ('var', p[1])

    #print('hola')


def p_list_first(p):
    """
    value_list : expr
    row_list   : row
    """
    p[0] = [p[1]]

def p_list_extend(p):
    """
    row_list   : expr SEMICOL expr
    """
    #p[0] = p[1] + [p[3]]

def p_row(p):
    """
    row       : LC expr RC
    """
    p[0] = p[2]

def p_matrix(p):
    """
    matrix    : row row
    """
    return p[0]


def p_error(p):
    global error
    if p:
        # print('p >> ', p)
        print(error_message + "Unexpected token '" + str(p.value) + "' at line " + str(p.lexer.lineno) + ".")
        error = True
        # sys.exit(0)
        # print('ptype', p.type)
    else:
        print(error_message + "Syntax error at EOF")
        error = True
        #sys.exit(0)

def p_empty(p):
    """
    empty :
    """
    # p[0] = None


######## IF ############################################################

## FALTA : gotof, guarda_salto, goto

def p_if(p):
    """
    if : IF LP expression RP check_bool gotof LB statement RB guarda_salto
        | IF LP expression RP check_bool gotof LB statement RB guarda_salto elseif
        | IF LP expression RP check_bool gotof LB statement RB guarda_salto else
    """
    print("IF ok. Expresion >> ", p[3])

def p_elseif(p):
    """
    elseif : ELSEIF LP expression RP check_bool LB statement RB guarda_salto
           | ELSEIF LP expression RP check_bool LB statement RB guarda_salto elseif
           | ELSEIF LP expression RP check_bool LB statement RB guarda_salto else
    """

def p_else(p):
    """
    else : ELSE LB statement RB guarda_salto
    """

######## END IF ############################################################

def p_expression(p):
    """
    expression : var_gt
               | var_lt
               | var_equal
               | var_neq
               | var_geq
               | var_leq
               | TRUE
               | FALSE
               | ID
    """
    p[0] = p[1]

def p_check_bool(p):
    """
    check_bool :
    """
    if p[-2] != True and p[-2] != False and p[-2] != 'true' and p[-2] != 'false':
        print("Expresion no es bool!")
        # sys.exit(0)

def p_gotof(p):
    """
    gotof :
    """
    print("gotof")

def p_guarda_salto(p):
    """
    guarda_salto :
    """
    print("guarda_salto")


# parser = yacc.yacc()

env = {}

def p_operacion(p):
    """
    p_operacion :

    """
    global env

    if type(p) == tuple:
        if p[0] == '+':
            return p_operacion(p[1]) + p_operacion(p[2])
        elif p[0] == '-':
            return p_operacion(p[1]) - p_operacion(p[2])
        elif p[0] == '*':
            return p_operacion(p[1]) * p_operacion(p[2])
        elif p[0] == '/':
            return p_operacion(p[1]) / p_operacion(p[2])
        elif p[0] == '=':
            env[p[1]] = p_operacion(p[2])
            print (env)
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable!'
            return env[p[1]]
    else:
        return p



parser = yacc.yacc()
lexer = lex.lexer

def test():
    try:
        arch = open("funcion1.txt", 'r')
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            # print(tok)
        if (parser.parse(informacion, tracking=True) == 'Compilacion Exitosa'):
            print("No Syntax Error found")
            print("VarTable >> ", vars(vt))

        else:
            print("Syntax Error")
    except EOFError:
        # print("ERROREOF")
        print(EOFError)

test()

## Lectura desde Consola
# while True:
#     try:
#         s = input('>> ')
#     except EOFError:
#         break
#     parser.parse(s)
#     parser.parse(s)
