def c(s):
    """
    A function to calculate sum of numbers from a list in form:
    '''
    - Food: 10000
    - Car: 3000
    ...
    '''
    For this example will output 13000.

    I'm using it when managing budget in an ORG file
    """
    nums = [l.split(':')[-1].strip() for l in s.splitlines()]
    return sum(map(int, nums))
