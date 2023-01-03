
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFPRECnonassocELSEnonassoc=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleft+-left*/left\'rightUMINUSADDASSIGN BREAK CONTINUE DIFF DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GE ID IF INTNUM LE MULASSIGN ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions : instruction instructionsinstructions : instruction instruction : expression\n                    | assignment \';\'\n                    | ifexpr\n                    | loop\n                    | returnexpr \';\'\n                    | printexpr \';\'\n                    | breakOrContinue \';\'\n                    | complexinstructionbreakOrContinue : brk\n                        | cntbrk : BREAKcnt : CONTINUEcomplexinstruction : \'{\' instructions \'}\'assignment : assignable \'=\' expression\n                    | assignable ADDASSIGN expression\n                    | assignable SUBASSIGN expression\n                    | assignable MULASSIGN expression\n                    | assignable DIVASSIGN expression\n                    assignable : ID\n                    | ID \'[\' expression \',\' expression \']\'expression : binexp\n                    | transpose\n                    | num\n                    | assignable\n                    | str\n                    | special \'(\' expression \')\'\n                    | \'[\' minit \']\'\n                    | \'(\' expression \')\'\n                    | \'-\' expression %prec UMINUSstr : STRINGtranspose : expression "\'"\n    num : int\n            | floatint : INTNUMfloat : FLOATNUMbinexp : mutexp\n                | compexpmutexp : expression \'+\' expression\n                | expression \'-\' expression\n                | expression \'*\' expression\n                | expression \'/\' expression\n                | expression DOTADD expression\n                | expression DOTSUB expression\n                | expression DOTMUL expression\n                | expression DOTDIV expressioncompexp : expression LE expression\n                | expression GE expression\n                | expression EQ expression\n                | expression \'>\' expression\n                | expression \'<\' expression\n                | expression DIFF expressionspecial : EYE\n                | ZEROS\n                | ONESminit : \'[\' matrixcontents \']\' \',\' minit\n                | \'[\' matrixcontents \']\'\n                | matrixcontentsmatrixcontents : expression\n                        |  expression \',\' matrixcontentsifexpr : IF \'(\' expression \')\' instruction %prec IFPREC\n                | IF \'(\' expression \')\' instruction ELSE instructionloop : forloop\n            | whileloopforloop : FOR ID \'=\' range instructionwhileloop : WHILE \'(\' expression \')\' instructionrange : expression \':\' expressionreturnexpr : RETURN expressionprintexpr : PRINT printableprintable : expression\n                | expression \',\' printable'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,8,12,13,14,15,16,17,23,24,30,31,32,33,34,35,43,44,45,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,126,128,130,133,135,],[-3,0,-1,-2,-5,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,-41,-42,-37,-38,-24,-35,-39,-40,-4,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,-65,-69,-70,-25,-66,]),'[':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[20,20,-6,-8,-9,-13,-26,-27,-28,-29,-30,20,73,20,-67,-68,20,20,20,-41,-42,-37,-38,83,-35,-39,-40,-36,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-7,-10,-11,-12,20,20,20,20,20,20,-29,73,-34,20,20,20,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,20,20,-18,20,-31,20,20,20,20,73,-65,-69,20,-70,20,-25,-71,-66,]),'(':([0,4,5,7,8,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,33,34,35,36,37,38,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[19,19,-6,-8,-9,-13,-26,-27,-28,-29,-30,70,19,19,19,78,-67,-68,19,19,19,-41,-42,-37,-38,-24,-35,-57,-58,-59,85,-39,-40,-36,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-7,-10,-11,-12,19,19,19,19,19,19,-29,19,-34,19,19,19,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,19,19,-18,19,-31,19,19,19,19,19,-65,-69,19,-70,19,-25,-71,-66,]),'-':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,109,110,111,112,113,114,115,116,119,121,122,123,124,125,126,127,128,129,130,132,133,134,135,],[21,21,48,-8,-9,-13,-26,-27,-28,-29,-30,21,21,21,-67,-68,21,21,21,-41,-42,-37,-38,-24,-35,-39,-40,-36,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-7,-10,-11,-12,21,21,21,21,21,21,48,-29,21,48,-34,21,48,48,21,21,-43,-44,-45,-46,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-33,-32,21,48,21,-18,48,21,48,-31,21,21,21,48,21,21,-65,48,-69,21,-70,21,-25,48,-66,]),'IF':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[22,22,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,22,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,22,22,22,-65,-69,-70,22,-25,-71,-66,]),'RETURN':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[25,25,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,25,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,25,25,25,-65,-69,-70,25,-25,-71,-66,]),'PRINT':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[26,26,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,26,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,26,26,26,-65,-69,-70,26,-25,-71,-66,]),'{':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[29,29,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,29,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,29,29,29,-65,-69,-70,29,-25,-71,-66,]),'ID':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,39,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[34,34,-6,-8,-9,-13,-26,-27,-28,-29,-30,34,34,34,-67,-68,34,34,34,-41,-42,-37,-38,-24,-35,84,-39,-40,-36,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-7,-10,-11,-12,34,34,34,34,34,34,-29,34,-34,34,34,34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,34,34,-18,34,-31,34,34,34,34,34,-65,-69,34,-70,34,-25,-71,-66,]),'STRING':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[35,35,-6,-8,-9,-13,-26,-27,-28,-29,-30,35,35,35,-67,-68,35,35,35,-41,-42,-37,-38,-24,-35,-39,-40,-36,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-7,-10,-11,-12,35,35,35,35,35,35,-29,35,-34,35,35,35,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,35,35,-18,35,-31,35,35,35,35,35,-65,-69,35,-70,35,-25,-71,-66,]),'EYE':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[36,36,-6,-8,-9,-13,-26,-27,-28,-29,-30,36,36,36,-67,-68,36,36,36,-41,-42,-37,-38,-24,-35,-39,-40,-36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-7,-10,-11,-12,36,36,36,36,36,36,-29,36,-34,36,36,36,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,36,36,-18,36,-31,36,36,36,36,36,-65,-69,36,-70,36,-25,-71,-66,]),'ZEROS':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[37,37,-6,-8,-9,-13,-26,-27,-28,-29,-30,37,37,37,-67,-68,37,37,37,-41,-42,-37,-38,-24,-35,-39,-40,-36,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-7,-10,-11,-12,37,37,37,37,37,37,-29,37,-34,37,37,37,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,37,37,-18,37,-31,37,37,37,37,37,-65,-69,37,-70,37,-25,-71,-66,]),'ONES':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[38,38,-6,-8,-9,-13,-26,-27,-28,-29,-30,38,38,38,-67,-68,38,38,38,-41,-42,-37,-38,-24,-35,-39,-40,-36,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-7,-10,-11,-12,38,38,38,38,38,38,-29,38,-34,38,38,38,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,38,38,-18,38,-31,38,38,38,38,38,-65,-69,38,-70,38,-25,-71,-66,]),'FOR':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[39,39,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,39,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,39,39,39,-65,-69,-70,39,-25,-71,-66,]),'WHILE':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[40,40,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,40,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,40,40,40,-65,-69,-70,40,-25,-71,-66,]),'BREAK':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[41,41,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,41,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,41,41,41,-65,-69,-70,41,-25,-71,-66,]),'CONTINUE':([0,4,5,7,8,12,13,14,15,16,17,23,24,29,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,119,122,124,126,128,130,132,133,134,135,],[42,42,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,42,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,42,42,42,-65,-69,-70,42,-25,-71,-66,]),'INTNUM':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[43,43,-6,-8,-9,-13,-26,-27,-28,-29,-30,43,43,43,-67,-68,43,43,43,-41,-42,-37,-38,-24,-35,-39,-40,-36,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-7,-10,-11,-12,43,43,43,43,43,43,-29,43,-34,43,43,43,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,43,43,-18,43,-31,43,43,43,43,43,-65,-69,43,-70,43,-25,-71,-66,]),'FLOATNUM':([0,4,5,7,8,12,13,14,15,16,17,19,20,21,23,24,25,26,29,30,31,32,33,34,35,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,77,78,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,109,111,112,114,116,119,121,122,124,125,126,128,129,130,132,133,134,135,],[44,44,-6,-8,-9,-13,-26,-27,-28,-29,-30,44,44,44,-67,-68,44,44,44,-41,-42,-37,-38,-24,-35,-39,-40,-36,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-7,-10,-11,-12,44,44,44,44,44,44,-29,44,-34,44,44,44,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,44,44,-18,44,-31,44,44,44,44,44,-65,-69,44,-70,44,-25,-71,-66,]),'}':([4,5,7,8,12,13,14,15,16,17,23,24,30,31,32,33,34,35,43,44,45,46,61,62,63,64,72,77,82,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,126,128,130,133,135,],[-5,-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,-41,-42,-37,-38,-24,-35,-39,-40,-4,-36,-7,-10,-11,-12,-29,-34,112,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,-65,-69,-70,-25,-66,]),'ELSE':([5,7,8,12,13,14,15,16,17,23,24,30,31,32,33,34,35,43,44,46,61,62,63,64,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,112,116,126,128,130,133,135,],[-6,-8,-9,-13,-26,-27,-28,-29,-30,-67,-68,-41,-42,-37,-38,-24,-35,-39,-40,-36,-7,-10,-11,-12,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-18,-31,132,-69,-70,-25,-66,]),"'":([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[46,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,46,-29,46,-34,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-33,-32,46,46,46,-31,46,46,-25,46,]),'+':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[47,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,47,-29,47,-34,47,47,-43,-44,-45,-46,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-33,-32,47,47,47,-31,47,47,-25,47,]),'*':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[49,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,49,-29,49,-34,49,49,49,49,-45,-46,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-33,-32,49,49,49,-31,49,49,-25,49,]),'/':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[50,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,50,-29,50,-34,50,50,50,50,-45,-46,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-33,-32,50,50,50,-31,50,50,-25,50,]),'DOTADD':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[51,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,51,-29,51,-34,51,51,-43,-44,-45,-46,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-33,-32,51,51,51,-31,51,51,-25,51,]),'DOTSUB':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[52,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,52,-29,52,-34,52,52,-43,-44,-45,-46,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-33,-32,52,52,52,-31,52,52,-25,52,]),'DOTMUL':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[53,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,53,-29,53,-34,53,53,-43,-44,-45,-46,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-33,-32,53,53,53,-31,53,53,-25,53,]),'DOTDIV':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[54,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,54,-29,54,-34,54,54,-43,-44,-45,-46,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-33,-32,54,54,54,-31,54,54,-25,54,]),'LE':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[55,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,55,-29,55,-34,55,55,-43,-44,-45,-46,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-33,-32,55,55,55,-31,55,55,-25,55,]),'GE':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[56,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,56,-29,56,-34,56,56,-43,-44,-45,-46,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-33,-32,56,56,56,-31,56,56,-25,56,]),'EQ':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[57,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,57,-29,57,-34,57,57,-43,-44,-45,-46,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-33,-32,57,57,57,-31,57,57,-25,57,]),'>':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[58,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,58,-29,58,-34,58,58,-43,-44,-45,-46,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-33,-32,58,58,58,-31,58,58,-25,58,]),'<':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[59,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,59,-29,59,-34,59,59,-43,-44,-45,-46,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-33,-32,59,59,59,-31,59,59,-25,59,]),'DIFF':([5,13,14,15,16,17,30,31,32,33,34,35,43,44,46,71,72,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,113,115,116,123,127,133,134,],[60,-26,-27,-28,-29,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,60,-29,60,-34,60,60,-43,-44,-45,-46,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-33,-32,60,60,60,-31,60,60,-25,60,]),';':([6,9,10,11,13,14,15,17,27,28,30,31,32,33,34,35,41,42,43,44,46,72,77,79,80,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,106,108,116,120,133,],[61,62,63,64,-26,-27,-28,-30,-14,-15,-41,-42,-37,-38,-24,-35,-16,-17,-39,-40,-36,-29,-34,-72,-73,-74,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-19,-20,-21,-22,-23,-33,-32,-31,-75,-25,]),')':([13,14,15,17,30,31,32,33,34,35,43,44,46,71,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,105,106,108,110,115,116,133,],[-26,-27,-28,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,106,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,116,-33,-32,119,124,-31,-25,]),',':([13,14,15,17,30,31,32,33,34,35,43,44,46,72,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,113,116,117,133,],[-26,-27,-28,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,-29,109,-34,111,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,121,-31,125,-25,]),']':([13,14,15,17,30,31,32,33,34,35,43,44,46,72,74,75,76,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,107,108,116,117,118,127,131,133,],[-26,-27,-28,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,-29,108,-62,-63,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,117,-32,-31,-61,-64,133,-60,-25,]),':':([13,14,15,17,30,31,32,33,34,35,43,44,46,72,77,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,116,123,133,],[-26,-27,-28,-30,-41,-42,-37,-38,-24,-35,-39,-40,-36,-29,-34,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-33,-32,-31,129,-25,]),'=':([16,34,84,133,],[65,-24,114,-25,]),'ADDASSIGN':([16,34,133,],[66,-24,-25,]),'SUBASSIGN':([16,34,133,],[67,-24,-25,]),'MULASSIGN':([16,34,133,],[68,-24,-25,]),'DIVASSIGN':([16,34,133,],[69,-24,-25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,4,29,],[3,45,82,]),'instruction':([0,4,29,119,122,124,132,],[4,4,4,126,128,130,135,]),'expression':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[5,5,71,76,77,79,81,5,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,76,110,113,115,76,81,123,5,127,5,5,76,134,5,]),'assignment':([0,4,29,119,122,124,132,],[6,6,6,6,6,6,6,]),'ifexpr':([0,4,29,119,122,124,132,],[7,7,7,7,7,7,7,]),'loop':([0,4,29,119,122,124,132,],[8,8,8,8,8,8,8,]),'returnexpr':([0,4,29,119,122,124,132,],[9,9,9,9,9,9,9,]),'printexpr':([0,4,29,119,122,124,132,],[10,10,10,10,10,10,10,]),'breakOrContinue':([0,4,29,119,122,124,132,],[11,11,11,11,11,11,11,]),'complexinstruction':([0,4,29,119,122,124,132,],[12,12,12,12,12,12,12,]),'binexp':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'transpose':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'num':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'assignable':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[16,16,72,72,72,72,72,16,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,16,72,16,16,72,72,16,]),'str':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'special':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'forloop':([0,4,29,119,122,124,132,],[23,23,23,23,23,23,23,]),'whileloop':([0,4,29,119,122,124,132,],[24,24,24,24,24,24,24,]),'brk':([0,4,29,119,122,124,132,],[27,27,27,27,27,27,27,]),'cnt':([0,4,29,119,122,124,132,],[28,28,28,28,28,28,28,]),'mutexp':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'compexp':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'int':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'float':([0,4,19,20,21,25,26,29,47,48,49,50,51,52,53,54,55,56,57,58,59,60,65,66,67,68,69,70,73,78,83,85,109,111,114,119,121,122,124,125,129,132,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'minit':([20,73,125,],[74,74,131,]),'matrixcontents':([20,73,109,125,],[75,107,118,75,]),'printable':([26,111,],[80,120,]),'range':([114,],[122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',32),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',37),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',42),
  ('instructions -> instruction instructions','instructions',2,'p_instructions_1','Mparser.py',46),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',51),
  ('instruction -> expression','instruction',1,'p_instruction','Mparser.py',56),
  ('instruction -> assignment ;','instruction',2,'p_instruction','Mparser.py',57),
  ('instruction -> ifexpr','instruction',1,'p_instruction','Mparser.py',58),
  ('instruction -> loop','instruction',1,'p_instruction','Mparser.py',59),
  ('instruction -> returnexpr ;','instruction',2,'p_instruction','Mparser.py',60),
  ('instruction -> printexpr ;','instruction',2,'p_instruction','Mparser.py',61),
  ('instruction -> breakOrContinue ;','instruction',2,'p_instruction','Mparser.py',62),
  ('instruction -> complexinstruction','instruction',1,'p_instruction','Mparser.py',63),
  ('breakOrContinue -> brk','breakOrContinue',1,'p_breakOrContinue','Mparser.py',68),
  ('breakOrContinue -> cnt','breakOrContinue',1,'p_breakOrContinue','Mparser.py',69),
  ('brk -> BREAK','brk',1,'p_brk','Mparser.py',74),
  ('cnt -> CONTINUE','cnt',1,'p_cnt','Mparser.py',79),
  ('complexinstruction -> { instructions }','complexinstruction',3,'p_complexinstruction','Mparser.py',83),
  ('assignment -> assignable = expression','assignment',3,'p_assignment','Mparser.py',88),
  ('assignment -> assignable ADDASSIGN expression','assignment',3,'p_assignment','Mparser.py',89),
  ('assignment -> assignable SUBASSIGN expression','assignment',3,'p_assignment','Mparser.py',90),
  ('assignment -> assignable MULASSIGN expression','assignment',3,'p_assignment','Mparser.py',91),
  ('assignment -> assignable DIVASSIGN expression','assignment',3,'p_assignment','Mparser.py',92),
  ('assignable -> ID','assignable',1,'p_assignable','Mparser.py',98),
  ('assignable -> ID [ expression , expression ]','assignable',6,'p_assignable','Mparser.py',99),
  ('expression -> binexp','expression',1,'p_expression','Mparser.py',107),
  ('expression -> transpose','expression',1,'p_expression','Mparser.py',108),
  ('expression -> num','expression',1,'p_expression','Mparser.py',109),
  ('expression -> assignable','expression',1,'p_expression','Mparser.py',110),
  ('expression -> str','expression',1,'p_expression','Mparser.py',111),
  ('expression -> special ( expression )','expression',4,'p_expression','Mparser.py',112),
  ('expression -> [ minit ]','expression',3,'p_expression','Mparser.py',113),
  ('expression -> ( expression )','expression',3,'p_expression','Mparser.py',114),
  ('expression -> - expression','expression',2,'p_expression','Mparser.py',115),
  ('str -> STRING','str',1,'p_str','Mparser.py',127),
  ("transpose -> expression '",'transpose',2,'p_transpose','Mparser.py',132),
  ('num -> int','num',1,'p_num','Mparser.py',138),
  ('num -> float','num',1,'p_num','Mparser.py',139),
  ('int -> INTNUM','int',1,'p_int','Mparser.py',144),
  ('float -> FLOATNUM','float',1,'p_float','Mparser.py',149),
  ('binexp -> mutexp','binexp',1,'p_binexp','Mparser.py',154),
  ('binexp -> compexp','binexp',1,'p_binexp','Mparser.py',155),
  ('mutexp -> expression + expression','mutexp',3,'p_mutexp','Mparser.py',160),
  ('mutexp -> expression - expression','mutexp',3,'p_mutexp','Mparser.py',161),
  ('mutexp -> expression * expression','mutexp',3,'p_mutexp','Mparser.py',162),
  ('mutexp -> expression / expression','mutexp',3,'p_mutexp','Mparser.py',163),
  ('mutexp -> expression DOTADD expression','mutexp',3,'p_mutexp','Mparser.py',164),
  ('mutexp -> expression DOTSUB expression','mutexp',3,'p_mutexp','Mparser.py',165),
  ('mutexp -> expression DOTMUL expression','mutexp',3,'p_mutexp','Mparser.py',166),
  ('mutexp -> expression DOTDIV expression','mutexp',3,'p_mutexp','Mparser.py',167),
  ('compexp -> expression LE expression','compexp',3,'p_compexp','Mparser.py',172),
  ('compexp -> expression GE expression','compexp',3,'p_compexp','Mparser.py',173),
  ('compexp -> expression EQ expression','compexp',3,'p_compexp','Mparser.py',174),
  ('compexp -> expression > expression','compexp',3,'p_compexp','Mparser.py',175),
  ('compexp -> expression < expression','compexp',3,'p_compexp','Mparser.py',176),
  ('compexp -> expression DIFF expression','compexp',3,'p_compexp','Mparser.py',177),
  ('special -> EYE','special',1,'p_special','Mparser.py',182),
  ('special -> ZEROS','special',1,'p_special','Mparser.py',183),
  ('special -> ONES','special',1,'p_special','Mparser.py',184),
  ('minit -> [ matrixcontents ] , minit','minit',5,'p_minit','Mparser.py',189),
  ('minit -> [ matrixcontents ]','minit',3,'p_minit','Mparser.py',190),
  ('minit -> matrixcontents','minit',1,'p_minit','Mparser.py',191),
  ('matrixcontents -> expression','matrixcontents',1,'p_matrixcontents','Mparser.py',201),
  ('matrixcontents -> expression , matrixcontents','matrixcontents',3,'p_matrixcontents','Mparser.py',202),
  ('ifexpr -> IF ( expression ) instruction','ifexpr',5,'p_ifexpr','Mparser.py',210),
  ('ifexpr -> IF ( expression ) instruction ELSE instruction','ifexpr',7,'p_ifexpr','Mparser.py',211),
  ('loop -> forloop','loop',1,'p_loop','Mparser.py',219),
  ('loop -> whileloop','loop',1,'p_loop','Mparser.py',220),
  ('forloop -> FOR ID = range instruction','forloop',5,'p_forloop','Mparser.py',225),
  ('whileloop -> WHILE ( expression ) instruction','whileloop',5,'p_whileloop','Mparser.py',230),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',235),
  ('returnexpr -> RETURN expression','returnexpr',2,'p_returnexpr','Mparser.py',240),
  ('printexpr -> PRINT printable','printexpr',2,'p_printexpr','Mparser.py',245),
  ('printable -> expression','printable',1,'p_printable','Mparser.py',250),
  ('printable -> expression , printable','printable',3,'p_printable','Mparser.py',251),
]
