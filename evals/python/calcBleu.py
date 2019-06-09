from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

import sys

bleu = sentence_bleu
cc = SmoothingFunction()

"""
  Calculates the average bleu score given a reference file refFile
  and a hypothesis file hypFile.
"""
def calcBleu(hypFile, refFile, printGoodSumms = False, thresh = 0.8):
    refs = open(refFile, "r")
    hyps = open(hypFile, "r")
    ref = refs.readline()
    hyp = hyps.readline()

    comparisons = 0.0
    total = 0.0
    while ref != '' and hyp != '':
        ref = [ref.split()]
        hyp = hyp.split()
        score = bleu(ref, hyp, smoothing_function=cc.method4)
        total += score

        # for printing out any prediction with a high BLEU score
        if (printGoodSumms and score > thresh):
            print(score)
            print("Predicted: " + str(hyp))
            print("Reference: " + str(ref[0]))
            print('')

        ref = refs.readline()
        hyp = hyps.readline()
        comparisons += 1


    refs.close()
    hyps.close()

    return total / comparisons

def main():
    if len(sys.argv) < 3:
        print("Error, not enough arguments.")
    elif len(sys.argv) == 3:
        print(calcBleu(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 4:
        print(calcBleu(sys.argv[1], sys.argv[2], sys.argv[3]))
    elif len(sys.argv) == 5:
        print(calcBleu(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
    else:
        print("Too many arguments")

if __name__ == "__main__":
    main()
