def solve_hanoi(num_disk, first_peg, mid_peg, last_peg):

    if num_disk == 1:
        print("Move the top disk from peg {} to peg {}.".format(first_peg, last_peg))
    else:
        solve_hanoi(num_disk-1, first_peg, last_peg, mid_peg)
        solve_hanoi(1, first_peg, mid_peg, last_peg)
        solve_hanoi(num_disk-1, mid_peg, first_peg, last_peg)
    # return 0

solve_hanoi(3, "A", "B", "C")