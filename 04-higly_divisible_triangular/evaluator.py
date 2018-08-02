from turingarena import *

all_passed = True
ans=[28,528,25200,25200,73920,2031120]
N=[5,20,50,70,100,200]
for I in range(0,len(ans)):

    try:
        with run_algorithm(submission.source) as process:
            c = process.functions.num(N[I])
        if c == ans[I]:
            print(f" num({N[I]}) --> {c} (Correct)")
        else:
            print(f" num({N[I]}) --> {c} (Wrong!)")
            all_passed = False
    except AlgorithmError as e:
        print(f"num({N[I]}) --> {e}")
        all_passed = False

evaluation.data(dict(goals=dict(correct=all_passed)))
