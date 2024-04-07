
class FactorySprites:
    def __init__(self, prototypes, periods, first_event_type):
        self._periods = periods
        self._event_types = []
        for i in range(len(prototypes)):
            self._event_types.append(first_event_type+i)
        self._prototypes = prototypes

    def make(self, event_type):
        if len(self._prototypes) == 1:
            return self._prototypes[event_type - self._event_types[0]].clone()
        else:
            prototype = []
            for i in range(len(self._event_types)):
                prototype.append(self._prototypes[event_type - self._event_types[i]].clone())
            return prototype

    def get_period(self):
        if len(self._periods) == 1:
            return [self._periods[0]]
        else:
            period = []
            for i in range(len(self._periods)):
                period.append(self._periods[i])
            return period
