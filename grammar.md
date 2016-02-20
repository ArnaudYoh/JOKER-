# GRAMMAR

Program => (Stmt END)*
Stmt => Assignment | Deal | Funcall | FunDef | If | While | Return
Assignment => VARNAME MathExpr
MathExpr => (VARNAME|VALUE) AddSub
AddSub => empty | (PLUS | MINUS) (VARNAME|VALUE) AddSub
Deal => DEAL VARNAME
Funcall => CALL FVARNAME VARNAME* //VARNAME* being the parameters
FunDef => DEF FVARNAME VARNAME* OPEN STMT* CLOSE
If => IF BoolExpr OPEN (Stmt END)* CLOSE // No else for now
While => WHILE BoolExprs OPEN (Stmt END)* CLOSE
BoolExprs => NOT? BoolExpr AndOr
AndOr => (AND | OR) NOT? BoolExpr AndOr
BoolExpr => (VARNAME | VALUE) (GT | LT | EQ) (VARNAME | VALUE)
Return => RETURN OPEN VARNAME? CLOSE