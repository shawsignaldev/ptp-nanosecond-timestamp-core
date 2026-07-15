def offset_ns(t1: float, t2: float, t3: float, t4: float) -> float:
    return ((t2 - t1) + (t3 - t4)) / 2

def path_delay_ns(t1: float, t2: float, t3: float, t4: float) -> float:
    return ((t2 - t1) + (t4 - t3)) / 2
