from dataclasses import dataclass

@dataclass
class Number:
    value: any = None
    sd: any = None
    def __repr__(self):
        return ((f":{self.value}" if self.value != None else "")
                + (f"({self.sd})" if self.sd != None else ""))
