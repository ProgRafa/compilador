# Este arquivo contêm regras sintáticas da gramática
SYNTATIC_RULES = [
    # type of instruction : #identifier, Automato : {estados, gramatica, regras}
    {
        "class declaration" : "#CLASS_DECLARATION", 
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D'],
            "grammar" : ['#CLASS', '#IDENTIFIER'],
            "rules" : {
                "A" : { "#CLASS" : ["B"] },
                "B" : { "#IDENTIFIER" : ["C", "D"] },
                "C" : { "#START" : ["D"] },
                "D" : { " " : "D" }
            }
        },
    },

    {
        "method declaration" : "#METHOD_DECLARATION",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H"],
            "grammar" : ['#PUBLIC', '#STATIC', '#VOID', '#INTEGER', '#IDENTIFIER', '#PARENTHESISOPEN', '#PARENTHESISCLOSE'],
            "rules" : {
                "A" : { "#PUBLIC" : ["B", "C"] },
                "B" : { "#STATIC" : ["C"] },
                "C" : { "#VOID #INTEGER" : ["D"] },
                "D" : { "#IDENTIFIER" : ["E"] },
                "E" : { "#PARENTHESISOPEN" : ["F", "I"] },
                "F" : { "#PARENTHESISCLOSE" : ["G", "H"] },
                "G" : { "#START" : ["H"] },
                "H" : { " " : "H" },
                "I" : { "#STRING" : "J" },
                "J" : { "#ARRAYOPEN" : "K" },
                "K" : { "#ARRAYCLOSE" : "L"},
                "L" : { "#IDENTIFIER" : "F"},
            }
        },
    },

    {
        "variable declaration" : "#VARIABLE_DECLARATION",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J'],
            "grammar" : ['#IDENTIFIER', '#INTEGER', '#EQUALS', '#NUMBER', 
                         '#NEW', '#PARENTHESISOPEN', '#PARENTHESISCLOSE', 
                         '#STRUCTIONEND', '#SUM'],
            "rules" : {
                "A" : { "#IDENTIFIER #INTEGER #STRING" : ["B"] },
                "B" : { "#IDENTIFIER" : ["C", "I"] },
                "C" : { "#EQUALS" : ["D", "E", "K"] },
                "D" : { "#IDENTIFIER" : ["I"] },
                "E" : { "#NEW" : ["F"] },
                "F" : { "#IDENTIFIER" : ["G"] },
                "G" : { "#PARENTHESISOPEN" : ["H"] },
                "H" : { "#PARENTHESISCLOSE" : ["I"] },
                "I" : { "#STRUCTIONEND" : ["J"] },
                "J" : { " " : ["J"] },
                "K" : { "#NUMBER" : ["K", "I", "L"] },
                "L" : { "#SUM" : ["D"] }
            }
        },
    },

    {
        "run class method" : "#RUN_CLASS_METHOD",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            "grammar" : ['#IDENTIFIER', '#POINT', '#IDENTIFIER', 
                         '#PARENTHESISOPEN', '#PARENTHESISCLOSE'],
            "rules" : {
                "A" : { "#IDENTIFIER" : ["B"] },
                "B" : { "#POINT" : ["C"] },
                "C" : { "#IDENTIFIER" : ["D", "B"] },
                "D" : { "#PARENTHESISOPEN" : ["E", "H"] },
                "E" : { "#PARENTHESISCLOSE" : ["F", "E"] },
                "F" : { "#STRUCTIONEND" : ["G"] },
                "G" : { " " : ["G"] },
                "H" : { "#IDENTIFIER" : ["D"] }
            }
        },
    },

    {
        "for looping" : "#FOR_LOOPING",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'],
            "grammar" : ['#FOR', "#PARENTHESISOPEN", "#PARENTHESISCLOSE",
                         '#INTEGER', '#IDENTIFIER', '#EQUALS', '#NUMBER',
                         '#STRUCTIONEND', '#MINOR', '#SUM', '#SUBTRACT'],
            "rules" : {
                "A" : { "#FOR" : ["B"] },
                "B" : { "#PARENTHESISOPEN" : ["C"] },
                "C" : { "#INTEGER" : ["D"] },
                "D" : { "#IDENTIFIER" : ["E"] },
                "E" : { "#EQUALS" : ["F"] },
                "F" : { "#NUMBER" : ["G"] }, 
                "G" : { "#STRUCTIONEND" : ["H"] }, 
                "H" : { "#IDENTIFIER #NUMBER" : ["I", "J"] },
                "I" : { "#EQUALS" : ["J"] },
                "J" : { "#MINOR #BIGGER" : ["K"] },
                "K" : { "#IDENTIFIER #NUMBER" : ["L"] },
                "L" : { "#STRUCTIONEND" : ["M"] },
                "M" : { "#IDENTIFIER" : ["N"] },
                "N" : { "#SUM #SUBTRACT" : ["O"] },
                "O" : { "#SUM #SUBTRACT" : ["P"] },
                "P" : { "#PARENTHESISCLOSE" : ["Q"] },
                "Q" : { "#START" : ["Q"] }
            }
        },
    },

    {
        "set variable" : "#SET_VARIABLE",
        "AFD" : { 
            "states" : ['A', 'B','C', 'D', 'E', 'F', 'G'],
            "grammar" : ['#IDENTIFIER', '#EQUALS', '#MULTIPLY', 
                         '#SUM', '#SUBTRACT', '#INTEGER', '#STRUCTIONEND'],
            "rules" : {
                "A" : { "#IDENTIFIER" : ["B", "E"] },
                "B" : { "#EQUALS" : ["C", "D"] },
                "C" : { "#IDENTIFIER" : ["F"] },
                "D" : { "#NUMBER" : ["D", "F"] },
                "E" : { "#MULTIPLY #SUBTRACT #SUM" : ["B"] },
                "F" : { "#STRUCTIONEND" : ["G"] },
                "G" : { " " : ["G"] }
            }
        },
    },

    {
        "method return" : "#METHOD_RETURN",
        "AFD" : { 
            "states" : ['A', 'B', 'C', 'D'],
            "grammar" : ['#RETURN', '#IDENTIFIER', '#NUMBER', '#STRUCTIONEND'],
            "rules" : {
                "A" : { "#RETURN" : ["B"] },
                "B" : { "#IDENTIFIER #NUMBER" : ["C"] },
                "C" : { "#STRUCTIONEND" : ["D"] },
                "D" : { " " : ["D"] }
            }
        },
    }
]