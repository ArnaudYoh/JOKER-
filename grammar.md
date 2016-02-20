# GRAMMAR

Program => (Stmt END)*

Stmt => Assignment | Deal | Funcall | FunDef | If | While | Return

Assignment => VARNAME MathExpr

MathExpr => (VARNAME|VALUE|Funcall) AddSub

AddSub => empty | (PLUS | MINUS) (VARNAME|VALUE|Funcall) AddSub

Deal => DEAL VARNAME

Funcall => CALL FVARNAME OPEN (VARNAME END)* CLOSE //(VARNAME END)* being the parameters

FunDef => DEF FVARNAME OPEN (VARNAME END)* CLOSE OPEN Stmt* CLOSE

If => IF BoolExpr OPEN (Stmt END)* CLOSE // No else for now

While => WHILE BoolExprs OPEN (Stmt END)* CLOSE

BoolExprs => NOT? BoolExpr AndOr

AndOr => (AND | OR) NOT? BoolExpr AndOr

BoolExpr => (VARNAME | VALUE | Funcall) (GT | LT | EQ) (VARNAME | VALUE|Funcall)

Return => RETURN OPEN (VARNAME | VALUE | Funcall)? CLOSE
