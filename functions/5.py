#The Towers of Hanoi is a classic recursive problem that involves moving a stack of disks from one peg to another, subject to the constraint that a smaller disk cannot be placed on top of a larger one.

def towers_of_hanoi(n, source_peg, auxiliary_peg, target_peg):
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
        return
    towers_of_hanoi(n - 1, source_peg, target_peg, auxiliary_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    towers_of_hanoi(n - 1, auxiliary_peg, source_peg, target_peg)

# Example usage:
towers_of_hanoi(3, 'A', 'B', 'C')
