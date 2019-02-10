import sys

MINIMUM_MINUTE = 0
MAXIMUM_MINUTE = 59

MINIMUM_HOUR = 0
MAXIMUM_HOUR = 23

MINIMUM_MONTH_DAY = 1
MAXIMUM_MONTH_DAY = 31

MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

MINIMUM_WEEKDAY = 0
MAXIMUM_WEEKDAY = 6


class OutOfRangeException(Exception):
    """Value out of range exception."""
    def __init__(self):
        print('[ERROR] Value out of valid range')
        exit()


def validate_input(args):
    if len(args) < 6:
        print('''
            [ERROR] There are not enough values for input
            [ERROR] Format should be following:
            [ERROR] minute hour day_of_the_month month day_of_the_week command
        ''')
        exit()


def validate_range(start, end, minimum, maximum):
    if int(start) < minimum or int(end) > maximum:
        raise OutOfRangeException()


def parse_value_list(vals, minimum, maximum):
    out_of_range_values = [
        x for x in vals.split(',') if int(x) not in range(minimum, maximum + 1)
    ]
    if out_of_range_values:
        raise OutOfRangeException()
    return ' '.join(vals.split(','))


def resolve_range(value, minimum, maximum):
    value_range, _, step = value.partition('/')
    start, end = value_range.split('-')
    validate_range(
        start=start,
        end=end,
        minimum=minimum,
        maximum=maximum
    )
    return join_range(
        minimum=int(start),
        maximum=int(end),
        step=int(step or 1)
    )


def join_range(minimum, maximum, step=1):
    return ' '.join(
        str(val) for val in list(range(minimum, maximum + 1, step))
    )


def resolve_time_unit(value, minimum, maximum):
    """
    Resolve time unit depending on the input value. 
    Value * represents all values in min-max range
    Pure value represents
    """
    if ',' in value:
        return parse_value_list(
            minimum=minimum,
            maximum=maximum,
            vals=value
        )
    elif value == '*':
        return join_range(
            minimum=minimum,
            maximum=maximum
        )
    elif '-' in value:
        return resolve_range(
            value=value,
            minimum=minimum,
            maximum=maximum
        )
    if minimum <= int(value) <= maximum:
        return value
    raise OutOfRangeException()


def resolve_minute(value):
    """ Resolve minut values """
    return resolve_time_unit(
        value=value,
        minimum=MINIMUM_MINUTE,
        maximum=MAXIMUM_MINUTE,
    )


def resolve_hour(value):
    """ Resolve hour values """
    return resolve_time_unit(
        value=value,
        minimum=MINIMUM_HOUR,
        maximum=MAXIMUM_HOUR,
    )


def resolve_month_day(value):
    """ Resolve month day values """
    return resolve_time_unit(
        value=value,
        minimum=MINIMUM_MONTH_DAY,
        maximum=MAXIMUM_MONTH_DAY,
    )


def resolve_month(value):
    """ Resolve month values """
    return resolve_time_unit(
        value=value,
        minimum=MINIMUM_MONTH,
        maximum=MAXIMUM_MONTH,
    )


def resolve_week_day(value):
    """ Resolve week day values """
    return resolve_time_unit(
        value=value,
        minimum=MINIMUM_WEEKDAY,
        maximum=MAXIMUM_WEEKDAY,
    )


def resolve_crontab_output(args):
    """ Resolve crontab time units output """
    minute = resolve_minute(args[0])
    hour = resolve_hour(args[1])
    month_day = resolve_month_day(args[2])
    month = resolve_month(args[3])
    week_day = resolve_week_day(args[4])
    return minute, hour, month_day, month, week_day


def print_crontab(unit_times, command):
    """ Print crontab output """
    minute, hour, month_day, month, week_day = unit_times
    print('Minute: ' + minute)
    print('Hour: ' + hour)
    print('Day of the month: ' + month_day)
    print('Month: ' + month)
    print('Day of the week: ' + week_day)
    print('Command: ' + command)


if __name__ == '__main__':
    validate_input(sys.argv[1:])
    crontab_output_time_units = resolve_crontab_output(sys.argv[1:6])
    print_crontab(
        unit_times=crontab_output_time_units,
        command=' '.join(sys.argv[6:])
    )
