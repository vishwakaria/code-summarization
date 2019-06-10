import rouge
import json
import sys
# overcome recursion limit...

def main():
    sys.setrecursionlimit(2000 * 500 + 1000)
    for model in ["ast_cleaned", "transformer_no_ast", "raw_python"]:
        fr = rouge.FilesRouge("hyps/" + model + "_hyp.txt",
                              "refs/" + model + "_ref.test")
        print(model)
        print(json.dumps(fr.get_scores(avg=True), indent = 2))

if __name__ == "__main__":
    main()
