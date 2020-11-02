AVAILABLE_MODES = ["r_macguffin", "r_wo", "r_rocket_arena_2", "r_shaft_arena_1", "r_ca_2", "r_ca_1"]

def check_mode(mode):
    import argparse
    if mode not in AVAILABLE_MODES:
        raise argparse.ArgumentTypeError(f"{mode} is not available mode")
    return mode

def check_positive(v):
    import argparse
    num = int(v)
    if num <= 0:
        raise argparse.ArgumentTypeError(f"{v} is an invalid number. Please use only positive")
    return num
