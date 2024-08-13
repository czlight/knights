from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
A_says_knave_and_knight = And(AKnight, AKnave) # A says statement: I am both a Knight and a Knave

knowledge0 = And(
    Implication(AKnight, A_says_knave_and_knight), # If A is a Knight, the sentence he says is true
    Implication(AKnave, Not(A_says_knave_and_knight)), # If A is a Knave, the sentence they say is false
    Or(AKnight, AKnave), # A is a Knight or A is a Knave
    Not(And(AKnight, AKnave)), # A cannot be both a Knight and a Knave

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_says_both_knaves = And(AKnave, BKnave)

knowledge1 = And(

    Or(AKnight, AKnave), # A is a Knight or A is a Knave
    Not(And(AKnight, AKnave)), # A cannot be both a Knight and a Knave
    Or(BKnight, BKnave), # A is a Knight or A is a Knave
    Not(And(BKnight, BKnave)), # A cannot be both a Knight and a Knave
    Implication(AKnight, A_says_both_knaves),
    Implication(AKnave, Not(A_says_both_knaves))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_says_same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_says_different = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    Or(AKnight, AKnave), # A is a Knight or A is a Knave
    Not(And(AKnight, AKnave)), # A cannot be both a Knight and a Knave
    Or(BKnight, BKnave), # A is a Knight or A is a Knave
    Not(And(BKnight, BKnave)), # A cannot be both a Knight and a Knave
    Implication(AKnight, A_says_same),
    Implication(AKnave, Not(A_says_same)),
    Implication(BKnight, B_says_different),
    Implication(BKnave, Not(B_says_different))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

A_says_knight_or_knave = Or(AKnight, AKnave)
A_says_knave = AKnave


knowledge3 = And(
    Or(AKnight, AKnave), # A is a Knight or A is a Knave
    Not(And(AKnight, AKnave)), # A cannot be both a Knight and a Knave
    Or(BKnight, BKnave), # A is a Knight or A is a Knave
    Not(And(BKnight, BKnave)), # A cannot be both a Knight and a Knave
    Or(CKnight, CKnave), # A is a Knight or A is a Knave
    Not(And(CKnight, CKnave)), # A cannot be both a Knight and a Knave
    Implication(BKnight, A_says_knave),
    Implication(BKnave, Not(A_says_knave)),
    Implication(AKnight, A_says_knight_or_knave),
    Implication(AKnave, Not(A_says_knight_or_knave)),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
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
