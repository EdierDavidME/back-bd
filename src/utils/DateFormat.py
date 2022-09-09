import datetime

class DateFormat():
    @classmethod
    def conver_date(slef, date):
        return datetime.datetime.strftime(date, "%d/%m/%Y")