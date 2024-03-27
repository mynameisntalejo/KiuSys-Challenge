from datetime import datetime

from utils import DATE_FORMAT, DATE_FORMAT_VALIDATION_MSG, DATE_MIN, DATE_RANGE_VALIDATION_MSG, DATE_MIN_VALIDATION_MSG, \
    FEE_INT_VALIDATION_MSG


def date_format_validation(date):
    try:
        datetime.strptime(date, DATE_FORMAT)
    except ValueError:
        raise ValueError(DATE_FORMAT_VALIDATION_MSG)


def date_range_validation(date):
    date_obj = datetime.strptime(date, DATE_FORMAT)
    if date_obj < datetime.strptime(DATE_MIN, DATE_FORMAT) or date_obj > datetime.now():
        raise ValueError(DATE_RANGE_VALIDATION_MSG)


def date_min_validation(date):
    date_obj = datetime.strptime(date, DATE_FORMAT)
    if date_obj < datetime.strptime(DATE_MIN, DATE_FORMAT):
        raise ValueError(DATE_MIN_VALIDATION_MSG)


def int_fee_validation(fee):
    try:
        if not isinstance(int(fee), int):
            raise ValueError(FEE_INT_VALIDATION_MSG)
    except ValueError:
        raise ValueError(FEE_INT_VALIDATION_MSG)
