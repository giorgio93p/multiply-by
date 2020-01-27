from cjwmodule.i18n import trans

def render(table, params):
    for column in params['columns']:
        table[column] = params['constant'] * table[column]
    if params['constant'] < 0:
        return (table, trans("is_negative"))
    else:
        return table
