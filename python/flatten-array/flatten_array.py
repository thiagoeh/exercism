import collections


def flatten(iterable):
    flattened = []
    for item in iterable:
        if item != None:
            # Flattens any iterable except strings
            if isinstance(item, collections.Iterable) and not isinstance(item, str):
                flattened.extend(flatten(item))
            else:
                flattened.append(item)
    return flattened
