from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")



# Puzzle 0
# A says "I am both a knight and a knave."
Statement0 = And(AKnight, AKnave)

A_says_knight = AKnight
A_says_knave_and_knight = And(AKnight, AKnave)

knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, A_says_knight),
    Implication(A_says_knave_and_knight, AKnave)

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Statement0
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    i = 0
    j = 0
    for puzzle, knowledge in puzzles:

        print("knowledge is: ", knowledge)
        print("formula:", knowledge.formula())
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                print("symbol:", symbol)
                print("symbols", symbols)
                if model_check(knowledge, symbol):
                    print("model check is true")
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
