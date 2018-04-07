def distance(strand_a, strand_b):
    # Check if strands have same length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands don't have the same length")

    # Iterate every char in strand_a comparing with strand_b
    # Return False if a difference is found
    distanceCount = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            distanceCount += 1

    return distanceCount

if __name__ == '__main__':
    print(distance('ABDA','ABDA'))
