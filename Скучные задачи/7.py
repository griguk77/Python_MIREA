def main(input):
    a = (input & 0b00000000000000000000011111111111) << 1
    b = (input & 0b00000000000000011111100000000000) << 4
    c = (input & 0b00000000001111100000000000000000) << 4
    d = (input & 0b00000001110000000000000000000000) >> 10
    e = (input & 0b01111110000000000000000000000000) << 1
    f = (input & 0b10000000000000000000000000000000) >> 31
    return a | b | c | d | e | f
