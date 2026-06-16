class TimeMap:

    def __init__(self):
        self.key = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key:
            self.key[key] = {}
        self.key[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key:
            timestamps = self.key[key]
            if timestamps:
                if timestamps.get(timestamp, "") != "":
                    return timestamps[timestamp]
                else:
                    curr_max = -1
                    for ts, val in timestamps.items():
                        if ts <= timestamp:
                            curr_max = max(curr_max, ts)
                    if curr_max >= 0:
                        return timestamps[curr_max]
                    else:
                        return ""
        else:
            return ""

