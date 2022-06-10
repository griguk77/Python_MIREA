def zero(items, left, middle, right):
    if items[0] == 'KIT':
        return left
    if items[0] == 'RUBY':
        return middle
    if items[0] == 'SLASH':
        return right


def one(items, left, right):
    if items[1] == 'YACC':
        return left
    if items[1] == 'SQF':
        return right


def two(items, left, middle, right):
    if items[2] == 'PONY':
        return left
    if items[2] == 'ASN.1':
        return middle
    if items[2] == 'KRL':
        return right


def four(items, left, right):
    if items[4] == 'MQL4':
        return left
    if items[4] == 'PERL6':
        return right


def main(items):
    return two(
        items,
        zero(
            items,
            one(items, four(items, 0, 1), 2),
            four(items, one(items, 3, 4), 5),
            6
        ),
        7,
        zero(items, 8, 9, 10),
    )
