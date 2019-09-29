
TABLE = [
    # Lexema : Símbolo, Automato : {estados, gramatica, regras}
    {
        "class" : "#CLASS", 
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F'],
            "grammar" : ['c', 'l', 'a', 's'],
            "rules" : {
                "A" : { "c" : "B" },
                "B" : { "l" : "C" },
                "C" : { "a" : "D" },
                "D" : { "s" : "E" },
                "E" : { "s" : "F" },
                "F" : { " " : "F" }
            }
        },
    },
    {
        "{" : "#START",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['{'],
            "rules" : {
                "A" : { "{" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "}" : "#END",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['}'],
            "rules" : {
                "A" : { "}" : "B" },
                "B" : { " " : "B" }
            }
        },
    },

    {
        "[" : "#ARRAYOPEN",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['['],
            "rules" : {
                "A" : { "[" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "]" : "#ARRAYCLOSE",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : [']'],
            "rules" : {
                "A" : { "]" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "." : "#POINT",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['.'],
            "rules" : {
                "A" : { "." : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "(" : "#PARENTHESISOPEN",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['('],
            "rules" : {
                "A" : { "(" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        ")" : "#PARENTHESISCLOSE",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : [')'],
            "rules" : {
                "A" : { ")" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "<" : "#MINOR",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['<'],
            "rules" : {
                "A" : { "<" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        ">" : "#BIGGER",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['>'],
            "rules" : {
                "A" : { ">" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "=" : "#EQUALS",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['='],
            "rules" : {
                "A" : { "=" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "!" : "#NOT",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['!'],
            "rules" : {
                "A" : { "!" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        ";" : "#STRUCTIONEND",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : [';'],
            "rules" : {
                "A" : { ";" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "," : "#COMMA",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : [','],
            "rules" : {
                "A" : { "," : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "-" : "#SUBTRACT",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['-'],
            "rules" : {
                "A" : { "-" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "*" : "#MULTIPLY",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['*'],
            "rules" : {
                "A" : { "*" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "+" : "#SUM",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['+'],
            "rules" : {
                "A" : { "+" : "B" },
                "B" : { " " : "B" }
            }
        },
    },
    {
        "/" : "#DIVISION",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['/'],
            "rules" : {
                "A" : { "/" : "B" },
                "B" : { " " : "B" }
            }
        },
    },

    {
        "public" : "#PUBLIC",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            "grammar" : ['p', 'u', 'b', 'l', 'i', 'c'],
            "rules" : {
                "A" : { "p" : "B" },
                "B" : { "u" : "C" },
                "C" : { "b" : "D" },
                "D" : { "l" : "E" },
                "E" : { "i" : "F" },
                "F" : { "c" : "G" },
                "G" : { " " : "G" }
            }
        },
    },
    {
        "static" : "#STATIC",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            "grammar" : ['s', 't', 'a', 't', 'i', 'c'],
            "rules" : {
                "A" : { "s" : "B" },
                "B" : { "t" : "C" },
                "C" : { "a" : "D" },
                "D" : { "t" : "E" },
                "E" : { "i" : "F" },
                "F" : { "c" : "G" },
                "G" : { " " : "G" }
            }
        },  
    },
    {
        "void" : "#VOID",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E'],
            "grammar" : ['v', 'o', 'i', 'd'],
            "rules" : {
                "A" : { "v" : "B" },
                "B" : { "o" : "C" },
                "C" : { "i" : "D" },
                "D" : { "d" : "E" },
                "E" : { " " : "E" },
            }
        },
    },
    {
        "String" : "#STRING",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            "grammar" : ['S', 't', 'r', 'i', 'n', 'g'],
            "rules" : {
                "A" : { "S" : "B" },
                "B" : { "t" : "C" },
                "C" : { "r" : "D" },
                "D" : { "i" : "E" },
                "E" : { "n" : "F" },
                "F" : { "g" : "G" },
                "G" : { " " : "G" },
            }
        },
    },
    {
        "int" : "#INTEGER",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D'],
            "grammar" : ['i', 'n', 't'],
            "rules" : {
                "A" : { "i" : "B" },
                "B" : { "n" : "C" },
                "C" : { "t" : "D" },
                "D" : { " " : "D" }
            }
        },
    },
    {
        "boolean" : "#BOOLEAN",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            "grammar" : ['b', 'o', 'l', 'e', 'a', 'n'],
            "rules" : {
                "A" : { "b" : "B" },
                "B" : { "o" : "C" },
                "C" : { "o" : "D" },
                "D" : { "l" : "E" },
                "E" : { "e" : "F" },
                "F" : { "a" : "G" },
                "G" : { "n" : "H" },
                "H" : { " " : "H" }
            }
        },
    },

    {
        "if" : "#IF",
        "AFD" : { 
            "states" : ['A', 'B', 'C'],
            "grammar" : ['i', 'f'],
            "rules" : {
                "A" : { "i" : "B" },
                "B" : { "f" : "C" },
                "C" : { " " : "C" }
            }
        },
    },
    { 
        "else" : "#ELSE",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E'],
            "grammar" : ['e', 'l', 's'],
            "rules" : {
                "A" : { "e" : "B" },
                "B" : { "l" : "C" },
                "C" : { "s" : "D" },
                "D" : { "e" : "E" },
                "E" : { " " : "E" },
            }
        },
    },
    { 
        "while" : "#WHILE",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F'],
            "grammar" : ['w', 'h', 'i', 'l', 'e'],
            "rules" : {
                "A" : { "w" : "B" },
                "B" : { "h" : "C" },
                "C" : { "i" : "D" },
                "D" : { "l" : "E" },
                "E" : { "e" : "F" },
                "F" : { " " : "F" }
            }
        },
    },
    {
        "for" : "#FOR",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D'],
            "grammar" : ['f', 'o', 'r'],
            "rules" : {
                "A" : { "f" : "B" },
                "B" : { "o" : "C" },
                "C" : { "r" : "D" },
                "D" : { " " : "D" }
            }
        },
    },
    {
        "return" : "#RETURN",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            "grammar" : ['r', 'e', 't', 'u', 'r', 'n'],
            "rules" : {
                "A" : { "r" : "B" },
                "B" : { "e" : "C" },
                "C" : { "t" : "D" },
                "D" : { "u" : "E" },
                "E" : { "r" : "F" },
                "F" : { "n" : "G" },
                "G" : { " " : "G" }
            }
        },
    },
    {
        "new" : "#NEW",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D'],
            "grammar" : ['n', 'e', 'w'],
            "rules" : {
                "A" : { "n" : "B" },
                "B" : { "e" : "C" },
                "C" : { "w" : "D" },
                "D" : { " " : "D" }
            }
        },
    },
    {
        "this" : "#THIS",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E'],
            "grammar" : ['t', 'h', 'i', 's'],
            "rules" : {
                "A" : { "t" : "B" },
                "B" : { "h" : "C" },
                "C" : { "i" : "D" },
                "D" : { "s" : "E" },
                "E" : { " " : "E" }
            }
        },
    },
    {
        "false" : "#FALSE",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F'],
            "grammar" : ['f', 'a', 'l', 's', 'e'],
            "rules" : {
                "A" : { "f" : "B" },
                "B" : { "a" : "C" },
                "C" : { "l" : "D" },
                "D" : { "s" : "E" },
                "E" : { "e" : "F" },
                "F" : { " " : "F" }
            }
        },
    },
    {
        "true" : "#TRUE",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E'],
            "grammar" : ['t', 'r', 'u', 'e'],
            "rules" : {
                "A" : { "t" : "B" },
                "B" : { "r" : "C" },
                "C" : { "u" : "D" },
                "D" : { "e" : "E" },
                "E" : { " " : "E" }
            }
        },
    },
    {
        "null" : "#NULL",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E'],
            "grammar" : ['n', 'u', 'l'],
            "rules" : {
                "A" : { "n" : "B" },
                "B" : { "u" : "C" },
                "C" : { "l" : "D" },
                "D" : { "l" : "E" },
                "E" : { " " : "E" }
            }
        },
    },

    {
        "identifier" : "#IDENTIFIER",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'w', '_'],
            "rules" : {
                "A" : { 
                    "abcdefghijklmnopqrstuvwxyz" : "B",
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "B",
                    "_" : "B",
                    " " : "B"
                },
                "B" : { 
                   "abcdefghijklmnopqrstuvwxyz" : "B",
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "B",
                    "_" : "B",
                    " " : "B"
                },
            }
        },
    },
    { 
        "number" : "#NUMBER",
        "AFD" : { 
            "states" : ['A', 'B'],
            "grammar" : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            "rules" : {
                "A" : { 
                    "0123456789" : "B"
                },
                "B" : { 
                    "0123456789" : "B",
                    " " : "B"
                },
            }
        },
    }
]