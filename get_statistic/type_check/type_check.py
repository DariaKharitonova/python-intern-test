def check_positive(v):
    import argparse
    num = int(v)
    if num <= 0:
        raise argparse.ArgumentTypeError(
            f"{v} is an invalid number. Please use only positive")
    return num
