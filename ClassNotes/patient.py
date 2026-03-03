class patient:
    def __init__(self, fname, lname, pps, injury):
        self.fname = fname
        self.lname = lname
        self.pps = pps
        self.injury = injury

    def __str__(self):
        return f"Patient Name: {self.fname} {self.lname}, PPS: {self.pps}, Injury: {self.injury}"

