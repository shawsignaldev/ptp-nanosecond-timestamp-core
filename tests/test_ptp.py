from ptp_nanosecond_timestamp_core.ptp import offset_ns, path_delay_ns

def test_offset_ns_uses_standard_two_way_exchange() -> None:
    assert offset_ns(t1=100, t2=160, t3=180, t4=250) == -5.0

def test_path_delay_ns_uses_round_trip_minus_response() -> None:
    assert path_delay_ns(t1=100, t2=160, t3=180, t4=250) == 65.0
