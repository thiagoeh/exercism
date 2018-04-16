def slices(series, length):
    if length == 0:
        raise ValueError('length parameter must be greater than 0')
    if length > len(series):
        raise ValueError('length parameter is greater than series length')

    series_slices = []
    for i in range(len(series) - length + 1):
        series_slices.append(list(map(int, series[i:length + i])))

    return series_slices
