def distance(strand_a, strand_b):
    """Return the Hamming distance of two same-length DNA strands."""
    # Check if strands have same length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands don't have the same length")

    # Iterate every char in strand_a comparing with strand_b
    # Increment distance_count for every difference found
    distance_count = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            distance_count += 1

    return distance_count


# Basic test calling the script directly
if __name__ == '__main__':
    print(distance('ABDA', 'ABDA'))
