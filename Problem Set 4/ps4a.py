# Problem Set 4A
# Name: Patryk Rogala
# Collaborators:
# Time Spent: 0:01

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]

    permutations = []
    for i in range(len(sequence)):
        for perm in get_permutations(sequence[:i] + sequence[i+1:]):
            permutations.append(sequence[i] + perm)
    return permutations

if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'bc'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'cd'
    print('Input:', example_input)
    print('Expected Output:', ['cd', 'dc'])
    print('Actual Output:', get_permutations(example_input))


