names = ['Simon', 'Alier', 'Ali', 'Moha']

def is_long_names(name):
    return len(name) > 4
long_names = list(filter(is_long_names, names))
print(long_names)
