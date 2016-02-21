# GRAMMAR

Program => (Stmt END)*

Stmt => Assignment | Deal | Funcall | FunDef | If | While | Return

Assignment => VARNAME OPEN MathExpr CLOSE

MathExpr => Value AddSub

Value => (VARNAME|VALUE|Funcall)

AddSub => empty | (PLUS | MINUS) Value AddSub

Deal => DEAL VARNAME

FunCall => CALL (FVARNAME|CHR) OPEN (VARNAME END)* CLOSE //(VARNAME END)* being the parameters

FunDef => DEF FVARNAME OPEN (VARNAME END)* CLOSE OPEN Stmt* CLOSE

If => IF BoolExprs OPEN (Stmt END)* CLOSE // No else for now

While => WHILE BoolExprs OPEN (Stmt END)* CLOSE

BoolExprs => NOT? BoolExpr AndOr

AndOr => empty | (AND | OR) BoolExprs

BoolExpr => Value (GT | LT | EQ) Value

Return => RETURN OPEN Value? CLOSE
