table = [
# 	(	)	*	"+"	,	-	;	<	"="	>	id	def	if	else	num	print	return	int	{	}	$		
[None,	None,	None,	None,	None,	None,	None,	"STMT",	None,	None,	None,	"STMT",	"FLIST", "STMT", None,	None,	"STMT",	"STMT",	"STMT",	"STMT",	None,	"",],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"FDEF FLIST'",	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"FDEF",	None,	None,	None,	None,	None,	None,	None,	None,	"",	],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"def ( PARLIST ) { STMLIST }",	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	"",	    None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"int id PARLIST'",	None,	None,	None,],
[None,	None,	"",	    None,	None,	", PARLIST",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	";",	None,	None,	None,	"ATRIBST ;",	None,	"IFSTMT",	None,	None,	"PRINTST ;"	"RETURNST ;",	"int id",	"{ STMLIST' }",	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"id = ATRIBST'",None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"FACTOR TERM' NUMEXPR' EXPR'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	"id TEST",	None,	None,	None,	"FACTOR TERM' NUMEXPR' EXPR'",	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"print EXPR",	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"return",	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"if ( EXPR ) STMT IFSTMT'",	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	"",	    None,	None,	None,	"",	    None,	"",	["", "else"],	None,	"",	    "",	    "",	    "",	    "",	    "",	],
[None,	None,	None,	None,	None,	None,	None,	"STMT STMLIST'",None,	None,	None,	"STMT STMLIST'",	None,	"STMT STMLIST'",None,	None,	"STMT STMLIST'","STMT STMLIST'","STMT STMLIST'","STMT STMLIST'",None,None,],
[None,	None,	None,	None,	None,	None,	None,	"STMLIST",	    None,	None,	None,	"STMLIST",	None,	"STMLIST",	None,	None,	"STMLIST",	"STMLIST",	"STMLIST",	"STMLIST",	"",	None,],
[None,	"NUMEXPR EXPR'",None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"NUMEXPR EXPR'",None,	None,	None,	None,	None,	None,],
["== NUMEXPR",	None,	"",	None,	None,	None,	None,	"",	"< NUMEXPR",	None,	"> NUMEXPR",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"TERM NUMEXPR'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"TERM NUMEXPR'",	None,	None,	None,	None,	None,   None,],
["",	None,	"",	None,	"+ TERM NUMEXPR'",	None,	"- TERM NUMEXPR'",	"",	"",	None,	"",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"FACTOR TERM'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"FACTOR TERM'",	None,	None,	None,	None,	None,None,],
["",	None,	"",	"* FACTOR TERM'",	"",	None,	"",	"",	"",	None,	"",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	"( NUMEXPR )",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"num",	None,	None,	None,	None,	None,	None,],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	"id ( PARLISTCALL )",	None,	None,	None,	None,	None,	None,	None,	None,	None,   None,],
["TERM' NUMEXPR' EXPR'",	"( PARLISTCALL )",	None,	"TERM' NUMEXPR' EXPR'",	"TERM' NUMEXPR' EXPR'",	None,	"TERM' NUMEXPR' EXPR'",	"TERM' NUMEXPR' EXPR'",	"TERM' NUMEXPR' EXPR'",	None,	"TERM' NUMEXPR' EXPR'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	"",	None,	None,	None,	None,	None,	None,	None,	None,	"id PARLISTCALL'",	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
[None,	None,	"",	None,	None,	", PARLISTCALL",None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,],
]