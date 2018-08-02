# evaluation_assert data["goals"]["correct"]
from turingarena import *

all_passed = True

inputs=[4,13]
ans=[5832,23514624000]
for I in range(0,len(ans)):

    try:
        with run_algorithm(submission.source) as process:
            c = process.functions.find(inputs[I])
        if c == ans[I]:
            print(f" find({inputs[I]}) --> {c} (correct)")
        else:
            print(f" find({inputs[I]}) --> {c} (wrong!)")
            all_passed = False
    except AlgorithmError as e:
        print(f"find({inputs[I]}) --> {e}")
        all_passed = False

evaluation.data(dict(goals=dict(correct=all_passed)))
