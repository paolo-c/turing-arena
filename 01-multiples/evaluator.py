from turingarena import *

all_passed = True
ans=[23,2318,233168]
for I in range(0,len(ans)):

    try:
        with run_algorithm(submission.source) as process:
            c = process.functions.sum(10**(I+1))
        if c == ans[I]:
            print(f" sum({10**(I+1)}) --> {c} (correct)")
        else:
            print(f" sum({10**(I+1)}) --> {c} (wrong!)")
            all_passed = False
    except AlgorithmError as e:
        print(f"sum({10**(I+1)}) --> {e}")
        all_passed = False

evaluation.data(dict(goals=dict(correct=all_passed)))
