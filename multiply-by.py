
def render(table, params):
    for column in params['columns']:
        table[column] = params['constant'] * table[column]
    if params['constant'] < 0:
        return (table, "The number is negative")
    else:
        return table
