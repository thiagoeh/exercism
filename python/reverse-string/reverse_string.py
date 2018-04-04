def reverse(input=''):
    input_len = len(input)
    reversed  = ''

    for i in range(input_len-1,-1,-1):
        reversed = reversed + input[i]

    return(reversed)



