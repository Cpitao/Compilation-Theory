
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFPRECnonassocELSEnonassoc=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleft+-left*/left\'rightUMINUSADDASSIGN BREAK CONTINUE DIFF DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GE ID IF INTNUM LE MULASSIGN ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction instructions : instruction instruction : expression\n                    | assignment \';\'\n                    | ifexpr\n                    | loop\n                    | returnexpr \';\'\n                    | printexpr \';\'\n                    | BREAK \';\'\n                    | CONTINUE \';\'\n                    | complexinstructioncomplexinstruction : \'{\' instructions \'}\'assignment : assignable \'=\' expression\n                    | assignable ADDASSIGN expression\n                    | assignable SUBASSIGN expression\n                    | assignable MULASSIGN expression\n                    | assignable DIVASSIGN expressionassignable : ID\n                    | matrixelementmatrixelement : ID \'[\' expression \',\' expression \']\'expression : expression \'+\' expression\n                    | expression \'-\' expression\n                    | expression \'*\' expression\n                    | expression \'/\' expression\n                    | expression DOTADD expression\n                    | expression DOTSUB expression\n                    | expression DOTMUL expression\n                    | expression DOTDIV expression\n                    | expression LE expression\n                    | expression GE expression\n                    | expression EQ expression\n                    | expression \'>\' expression\n                    | expression \'<\' expression\n                    | expression DIFF expression\n                    | expression "\'"\n                    | INTNUM\n                    | FLOATNUM\n                    | assignable\n                    | special \'(\' expression \')\'\n                    | \'[\' minit \']\'\n                    | \'-\' expression %prec UMINUSspecial : EYE\n                | ZEROS\n                | ONESminit : minit \',\' \'[\' matrixcontents \']\'\n                | \'[\' matrixcontents \']\'matrixcontents : expression\n                        | matrixcontents \',\' expressionifexpr : IF \'(\' expression \')\' instruction %prec IFPREC\n                | IF \'(\' expression \')\' instruction ELSE instructionloop : forloop\n            | whileloopforloop : FOR ID \'=\' range instructionwhileloop : WHILE \'(\' expression \')\' instructionrange : expression \':\' expressionreturnexpr : RETURN expressionprintexpr : PRINT printableprintable : STRING\n                    | expression\n                    | printable \',\' expression'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,8,13,15,16,17,21,22,26,27,33,48,49,50,51,52,53,54,55,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,115,117,119,122,124,],[-3,0,-1,-2,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,-52,-56,-57,-23,-53,]),'BREAK':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[11,11,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,11,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,11,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,11,11,11,-52,-56,-57,11,-23,-58,-53,]),'CONTINUE':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[12,12,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,12,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,12,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,12,12,12,-52,-56,-57,12,-23,-58,-53,]),'INTNUM':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[15,15,-5,-6,-8,-9,-14,15,-39,-40,-41,-54,-55,15,15,15,-21,-22,-4,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-38,-7,-10,-11,-12,-13,-44,-41,15,15,15,15,15,15,15,15,15,15,15,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,15,-15,15,-42,15,15,15,15,15,15,-52,-56,15,-57,15,-23,-58,-53,]),'FLOATNUM':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[16,16,-5,-6,-8,-9,-14,16,-39,-40,-41,-54,-55,16,16,16,-21,-22,-4,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-38,-7,-10,-11,-12,-13,-44,-41,16,16,16,16,16,16,16,16,16,16,16,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,16,-15,16,-42,16,16,16,16,16,16,-52,-56,16,-57,16,-23,-58,-53,]),'[':([0,3,4,5,7,8,13,14,15,16,17,19,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[19,19,-5,-6,-8,-9,-14,19,-39,-40,-41,62,-54,-55,19,19,19,70,-22,-4,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-38,-7,-10,-11,-12,-13,-44,-41,19,19,19,19,19,19,19,19,19,19,19,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,106,19,-15,19,-42,19,19,19,19,19,19,-52,-56,19,-57,19,-23,-58,-53,]),'-':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,68,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,98,99,100,101,102,103,105,106,107,108,109,110,111,112,113,115,116,117,118,119,121,122,123,124,],[14,14,-5,35,-8,-9,-14,14,-39,-40,-41,-54,-55,14,14,14,-21,-22,-4,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-38,-7,-10,-11,-12,-13,-44,-41,14,14,14,14,14,14,14,14,35,35,14,14,14,-24,-25,-26,-27,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-43,35,14,-15,35,14,35,-42,14,14,14,35,14,14,35,14,35,-52,35,-56,14,-57,14,-23,35,-53,]),'IF':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[20,20,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,20,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,20,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,20,20,20,-52,-56,-57,20,-23,-58,-53,]),'RETURN':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[23,23,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,23,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,23,23,23,-52,-56,-57,23,-23,-58,-53,]),'PRINT':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[24,24,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,24,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,24,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,24,24,24,-52,-56,-57,24,-23,-58,-53,]),'{':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[25,25,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,25,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,25,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,25,25,25,-52,-56,-57,25,-23,-58,-53,]),'ID':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[26,26,-5,-6,-8,-9,-14,26,-39,-40,-41,-54,-55,26,26,26,-21,-22,71,-4,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-38,-7,-10,-11,-12,-13,-44,-41,26,26,26,26,26,26,26,26,26,26,26,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,26,-15,26,-42,26,26,26,26,26,26,-52,-56,26,-57,26,-23,-58,-53,]),'EYE':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[28,28,-5,-6,-8,-9,-14,28,-39,-40,-41,-54,-55,28,28,28,-21,-22,-4,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-38,-7,-10,-11,-12,-13,-44,-41,28,28,28,28,28,28,28,28,28,28,28,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,28,-15,28,-42,28,28,28,28,28,28,-52,-56,28,-57,28,-23,-58,-53,]),'ZEROS':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[29,29,-5,-6,-8,-9,-14,29,-39,-40,-41,-54,-55,29,29,29,-21,-22,-4,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-38,-7,-10,-11,-12,-13,-44,-41,29,29,29,29,29,29,29,29,29,29,29,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,29,-15,29,-42,29,29,29,29,29,29,-52,-56,29,-57,29,-23,-58,-53,]),'ONES':([0,3,4,5,7,8,13,14,15,16,17,21,22,23,24,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,98,99,101,103,105,106,107,109,110,112,115,117,118,119,121,122,123,124,],[30,30,-5,-6,-8,-9,-14,30,-39,-40,-41,-54,-55,30,30,30,-21,-22,-4,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-38,-7,-10,-11,-12,-13,-44,-41,30,30,30,30,30,30,30,30,30,30,30,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,30,-15,30,-42,30,30,30,30,30,30,-52,-56,30,-57,30,-23,-58,-53,]),'FOR':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[31,31,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,31,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,31,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,31,31,31,-52,-56,-57,31,-23,-58,-53,]),'WHILE':([0,3,4,5,7,8,13,15,16,17,21,22,25,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,107,110,112,115,117,119,121,122,123,124,],[32,32,-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,32,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,32,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,32,32,32,-52,-56,-57,32,-23,-58,-53,]),'}':([4,5,7,8,13,15,16,17,21,22,26,27,33,48,49,50,51,52,53,54,55,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,115,117,119,122,124,],[-5,-6,-8,-9,-14,-39,-40,-41,-54,-55,-21,-22,-4,-38,-7,-10,-11,-12,-13,-44,-41,99,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,-52,-56,-57,-23,-53,]),'ELSE':([5,7,8,13,15,16,17,21,22,26,27,48,49,50,51,52,53,54,55,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,99,103,115,117,119,122,124,],[-6,-8,-9,-14,-39,-40,-41,-54,-55,-21,-22,-38,-7,-10,-11,-12,-13,-44,-41,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-15,-42,121,-56,-57,-23,-53,]),'+':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[34,-39,-40,-41,-21,-22,-38,-44,-41,34,34,-24,-25,-26,-27,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-43,34,34,34,-42,34,34,34,34,-23,34,]),'*':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[36,-39,-40,-41,-21,-22,-38,-44,-41,36,36,36,36,-26,-27,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-43,36,36,36,-42,36,36,36,36,-23,36,]),'/':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[37,-39,-40,-41,-21,-22,-38,-44,-41,37,37,37,37,-26,-27,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-43,37,37,37,-42,37,37,37,37,-23,37,]),'DOTADD':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[38,-39,-40,-41,-21,-22,-38,-44,-41,38,38,-24,-25,-26,-27,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-43,38,38,38,-42,38,38,38,38,-23,38,]),'DOTSUB':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[39,-39,-40,-41,-21,-22,-38,-44,-41,39,39,-24,-25,-26,-27,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-43,39,39,39,-42,39,39,39,39,-23,39,]),'DOTMUL':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[40,-39,-40,-41,-21,-22,-38,-44,-41,40,40,-24,-25,-26,-27,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-43,40,40,40,-42,40,40,40,40,-23,40,]),'DOTDIV':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[41,-39,-40,-41,-21,-22,-38,-44,-41,41,41,-24,-25,-26,-27,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-43,41,41,41,-42,41,41,41,41,-23,41,]),'LE':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[42,-39,-40,-41,-21,-22,-38,-44,-41,42,42,-24,-25,-26,-27,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-43,42,42,42,-42,42,42,42,42,-23,42,]),'GE':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[43,-39,-40,-41,-21,-22,-38,-44,-41,43,43,-24,-25,-26,-27,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-43,43,43,43,-42,43,43,43,43,-23,43,]),'EQ':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[44,-39,-40,-41,-21,-22,-38,-44,-41,44,44,-24,-25,-26,-27,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-43,44,44,44,-42,44,44,44,44,-23,44,]),'>':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[45,-39,-40,-41,-21,-22,-38,-44,-41,45,45,-24,-25,-26,-27,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-43,45,45,45,-42,45,45,45,45,-23,45,]),'<':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[46,-39,-40,-41,-21,-22,-38,-44,-41,46,46,-24,-25,-26,-27,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-43,46,46,46,-42,46,46,46,46,-23,46,]),'DIFF':([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[47,-39,-40,-41,-21,-22,-38,-44,-41,47,47,-24,-25,-26,-27,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-43,47,47,47,-42,47,47,47,47,-23,47,]),"'":([5,15,16,17,26,27,48,54,55,65,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,97,100,102,103,108,111,113,116,122,123,],[48,-39,-40,-41,-21,-22,-38,-44,-41,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-43,48,48,48,-42,48,48,48,48,-23,48,]),';':([6,9,10,11,12,15,16,26,27,48,54,55,65,66,67,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,103,108,122,],[49,50,51,52,53,-39,-40,-21,-22,-38,-44,-41,-59,-60,-61,-62,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-17,-18,-19,-20,-43,-42,-63,-23,]),',':([15,16,26,27,48,54,55,63,66,67,68,73,74,75,76,77,78,79,80,81,82,83,84,85,86,93,94,95,100,103,104,108,113,114,120,122,],[-39,-40,-21,-22,-38,-44,-41,96,98,-61,-62,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,105,-50,-43,109,-42,-49,-63,-51,105,-48,-23,]),')':([15,16,26,27,48,54,55,73,74,75,76,77,78,79,80,81,82,83,84,85,86,92,95,97,102,103,122,],[-39,-40,-21,-22,-38,-44,-41,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,103,-43,107,112,-42,-23,]),']':([15,16,26,27,48,54,55,63,73,74,75,76,77,78,79,80,81,82,83,84,85,86,93,94,95,103,104,113,114,116,120,122,],[-39,-40,-21,-22,-38,-44,-41,95,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,104,-50,-43,-42,-49,-51,120,122,-48,-23,]),':':([15,16,26,27,48,54,55,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,103,111,122,],[-39,-40,-21,-22,-38,-44,-41,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-43,-42,118,-23,]),'=':([17,26,27,71,122,],[56,-21,-22,101,-23,]),'ADDASSIGN':([17,26,27,122,],[57,-21,-22,-23,]),'SUBASSIGN':([17,26,27,122,],[58,-21,-22,-23,]),'MULASSIGN':([17,26,27,122,],[59,-21,-22,-23,]),'DIVASSIGN':([17,26,27,122,],[60,-21,-22,-23,]),'(':([18,20,28,29,30,32,],[61,64,-45,-46,-47,72,]),'STRING':([24,],[67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,25,],[3,69,]),'instruction':([0,3,25,69,107,110,112,121,],[4,33,4,33,115,117,119,124,]),'expression':([0,3,14,23,24,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,64,69,70,72,98,101,105,106,107,109,110,112,118,121,],[5,5,54,65,68,5,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,97,5,100,102,108,111,113,94,5,116,5,5,123,5,]),'assignment':([0,3,25,69,107,110,112,121,],[6,6,6,6,6,6,6,6,]),'ifexpr':([0,3,25,69,107,110,112,121,],[7,7,7,7,7,7,7,7,]),'loop':([0,3,25,69,107,110,112,121,],[8,8,8,8,8,8,8,8,]),'returnexpr':([0,3,25,69,107,110,112,121,],[9,9,9,9,9,9,9,9,]),'printexpr':([0,3,25,69,107,110,112,121,],[10,10,10,10,10,10,10,10,]),'complexinstruction':([0,3,25,69,107,110,112,121,],[13,13,13,13,13,13,13,13,]),'assignable':([0,3,14,23,24,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,64,69,70,72,98,101,105,106,107,109,110,112,118,121,],[17,17,55,55,55,17,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,17,55,55,55,55,55,55,17,55,17,17,55,17,]),'special':([0,3,14,23,24,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,64,69,70,72,98,101,105,106,107,109,110,112,118,121,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'forloop':([0,3,25,69,107,110,112,121,],[21,21,21,21,21,21,21,21,]),'whileloop':([0,3,25,69,107,110,112,121,],[22,22,22,22,22,22,22,22,]),'matrixelement':([0,3,14,23,24,25,34,35,36,37,38,39,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,64,69,70,72,98,101,105,106,107,109,110,112,118,121,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'minit':([19,],[63,]),'printable':([24,],[66,]),'matrixcontents':([62,106,],[93,114,]),'range':([101,],[110,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',27),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',31),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',35),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_1','Mparser.py',39),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',43),
  ('instruction -> expression','instruction',1,'p_instruction','Mparser.py',54),
  ('instruction -> assignment ;','instruction',2,'p_instruction','Mparser.py',55),
  ('instruction -> ifexpr','instruction',1,'p_instruction','Mparser.py',56),
  ('instruction -> loop','instruction',1,'p_instruction','Mparser.py',57),
  ('instruction -> returnexpr ;','instruction',2,'p_instruction','Mparser.py',58),
  ('instruction -> printexpr ;','instruction',2,'p_instruction','Mparser.py',59),
  ('instruction -> BREAK ;','instruction',2,'p_instruction','Mparser.py',60),
  ('instruction -> CONTINUE ;','instruction',2,'p_instruction','Mparser.py',61),
  ('instruction -> complexinstruction','instruction',1,'p_instruction','Mparser.py',62),
  ('complexinstruction -> { instructions }','complexinstruction',3,'p_complexinstruction','Mparser.py',66),
  ('assignment -> assignable = expression','assignment',3,'p_assignment','Mparser.py',70),
  ('assignment -> assignable ADDASSIGN expression','assignment',3,'p_assignment','Mparser.py',71),
  ('assignment -> assignable SUBASSIGN expression','assignment',3,'p_assignment','Mparser.py',72),
  ('assignment -> assignable MULASSIGN expression','assignment',3,'p_assignment','Mparser.py',73),
  ('assignment -> assignable DIVASSIGN expression','assignment',3,'p_assignment','Mparser.py',74),
  ('assignable -> ID','assignable',1,'p_assignable','Mparser.py',78),
  ('assignable -> matrixelement','assignable',1,'p_assignable','Mparser.py',79),
  ('matrixelement -> ID [ expression , expression ]','matrixelement',6,'p_matrixelement','Mparser.py',83),
  ('expression -> expression + expression','expression',3,'p_expression','Mparser.py',87),
  ('expression -> expression - expression','expression',3,'p_expression','Mparser.py',88),
  ('expression -> expression * expression','expression',3,'p_expression','Mparser.py',89),
  ('expression -> expression / expression','expression',3,'p_expression','Mparser.py',90),
  ('expression -> expression DOTADD expression','expression',3,'p_expression','Mparser.py',91),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression','Mparser.py',92),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression','Mparser.py',93),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression','Mparser.py',94),
  ('expression -> expression LE expression','expression',3,'p_expression','Mparser.py',95),
  ('expression -> expression GE expression','expression',3,'p_expression','Mparser.py',96),
  ('expression -> expression EQ expression','expression',3,'p_expression','Mparser.py',97),
  ('expression -> expression > expression','expression',3,'p_expression','Mparser.py',98),
  ('expression -> expression < expression','expression',3,'p_expression','Mparser.py',99),
  ('expression -> expression DIFF expression','expression',3,'p_expression','Mparser.py',100),
  ("expression -> expression '",'expression',2,'p_expression','Mparser.py',101),
  ('expression -> INTNUM','expression',1,'p_expression','Mparser.py',102),
  ('expression -> FLOATNUM','expression',1,'p_expression','Mparser.py',103),
  ('expression -> assignable','expression',1,'p_expression','Mparser.py',104),
  ('expression -> special ( expression )','expression',4,'p_expression','Mparser.py',105),
  ('expression -> [ minit ]','expression',3,'p_expression','Mparser.py',106),
  ('expression -> - expression','expression',2,'p_expression','Mparser.py',107),
  ('special -> EYE','special',1,'p_special','Mparser.py',111),
  ('special -> ZEROS','special',1,'p_special','Mparser.py',112),
  ('special -> ONES','special',1,'p_special','Mparser.py',113),
  ('minit -> minit , [ matrixcontents ]','minit',5,'p_minit','Mparser.py',117),
  ('minit -> [ matrixcontents ]','minit',3,'p_minit','Mparser.py',118),
  ('matrixcontents -> expression','matrixcontents',1,'p_matrixcontents','Mparser.py',122),
  ('matrixcontents -> matrixcontents , expression','matrixcontents',3,'p_matrixcontents','Mparser.py',123),
  ('ifexpr -> IF ( expression ) instruction','ifexpr',5,'p_ifexpr','Mparser.py',127),
  ('ifexpr -> IF ( expression ) instruction ELSE instruction','ifexpr',7,'p_ifexpr','Mparser.py',128),
  ('loop -> forloop','loop',1,'p_loop','Mparser.py',133),
  ('loop -> whileloop','loop',1,'p_loop','Mparser.py',134),
  ('forloop -> FOR ID = range instruction','forloop',5,'p_forloop','Mparser.py',138),
  ('whileloop -> WHILE ( expression ) instruction','whileloop',5,'p_whileloop','Mparser.py',142),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',146),
  ('returnexpr -> RETURN expression','returnexpr',2,'p_returnexpr','Mparser.py',150),
  ('printexpr -> PRINT printable','printexpr',2,'p_printexpr','Mparser.py',154),
  ('printable -> STRING','printable',1,'p_printable','Mparser.py',158),
  ('printable -> expression','printable',1,'p_printable','Mparser.py',159),
  ('printable -> printable , expression','printable',3,'p_printable','Mparser.py',160),
]
