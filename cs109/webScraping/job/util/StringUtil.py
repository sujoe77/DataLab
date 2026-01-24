from datetime import date
import datetime as DT

class StringUtil:

    def getPubDate(self, timeStr):
        today = date.today()

        if timeStr == "yesterday":
            timeStr = "1d ago"
        time = timeStr.split()
        delta = int(time[0].strip()[:-1])
        unit = time[0][-1:]
        if unit == "d":
            delta = delta * 24
        elif unit == "w":
            delta = delta * 24 * 7

        pub_date = today - DT.timedelta(hours=delta)
        return pub_date.strftime("%Y-%m-%d")