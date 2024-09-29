def read_amount(amount):
    quotient = amount // 10
    remainder = amount % 10

    match quotient:
        case 3:
            if remainder == 0:
                return 'thirty'
            return  'thirty ' + read_units(remainder)
        case 2:
            if remainder == 0:
                return 'twenty'
            return  'twenty ' + read_units(remainder)
        case 1:
            return read_tens(amount)

    return read_units(amount)


def read_tens(amount):

    match amount:
        case 19:
            return 'nineteen'
        case 18:
            return 'eighteen'
        case 17:
            return 'seventeen'
        case 16:
            return 'sixteen'
        case 15:
            return 'fifteen'
        case 14:
            return 'fourteen'
        case 13:
            return 'thirteen'
        case 12:
            return 'twelve'
        case 11:
            return 'eleven'
    return 'ten'


def read_units(amount):

    match amount:
        case 1:
            amount = 'one'
        case 2:
            amount = 'two'
        case 3:
            amount = 'three'
        case 4:
            amount = 'four'
        case 5:
            amount = 'five'
        case 6:
            amount = 'six'
        case 7:
            amount = 'seven'
        case 8:
            amount = 'eight'
        case 9:
            amount = 'nine'
        case 0:
            amount = 'zero'
    return amount
