from struct import *

FMT = dict(
    char='>c',
    int8='>b',
    uint8='>B',
    int16='>h',
    uint16='>H',
    int32='>i',
    uint32='>I',
    int64='>q',
    uint64='>Q',
    float='>f',
    double='>d',
)


def un_pack(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def unpack_a(buf, offs):
    a1, offs = un_pack(buf, offs, 'uint16')
    a2, offs = un_pack(buf, offs, 'uint64')
    a3 = []
    for _ in range(2):
        c_offset, offs = un_pack(buf, offs, 'uint16')
        c, _ = unpack_b(buf, c_offset)
        a3.append(c)
    a4_offs, offs = un_pack(buf, offs, 'uint16')
    a4, a4_offs = unpack_d(buf, a4_offs)
    a5_offs, offs = un_pack(buf, offs, 'uint32')
    a5, a5_offs = unpack_e(buf, a5_offs)
    a6, offs = un_pack(buf, offs, 'uint64')
    a7, offs = un_pack(buf, offs, 'uint32')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offs


def unpack_b(buf, offs):
    b1_offs, offs = un_pack(buf, offs, 'uint16')
    b1, b1_offs = unpack_c(buf, b1_offs)
    b2, offs = un_pack(buf, offs, 'uint64')
    b3, offs = un_pack(buf, offs, 'double')
    b4, offs = un_pack(buf, offs, 'uint8')
    b5, offs = un_pack(buf, offs, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5}, offs


def unpack_c(buf, offs):
    c1, offs = un_pack(buf, offs, 'uint8')
    c2_size, offs = un_pack(buf, offs, 'uint32')
    c2_offs, offs = un_pack(buf, offs, 'uint16')
    c2 = []
    for _ in range(c2_size):
        val, c2_offs = un_pack(buf, c2_offs, 'int8')
        c2.append(val)
    c3, offs = un_pack(buf, offs, 'int32')
    c4, offs = un_pack(buf, offs, 'int32')
    c5, offs = un_pack(buf, offs, 'int8')
    c6, offs = un_pack(buf, offs, 'int8')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6), offs


def unpack_d(buf, offs):
    d1, offs = un_pack(buf, offs, 'int8')
    d2, offs = un_pack(buf, offs, 'uint32')
    return dict(D1=d1, D2=d2), offs


def unpack_e(buf, offs):
    e1_size, offs = un_pack(buf, offs, 'uint16')
    e1_offs, offs = un_pack(buf, offs, 'uint16')
    e1 = []
    for _ in range(e1_size):
        val, e1_offs = un_pack(buf, e1_offs, 'double')
        e1.append(val)
    e2, offs = un_pack(buf, offs, 'uint32')
    e3 = []
    for _ in range(4):
        val, offs = un_pack(buf, offs, 'int32')
        e3.append(val)
    e4, offs = un_pack(buf, offs, 'int64')
    e5, offs = un_pack(buf, offs, 'int8')
    e6, offs = un_pack(buf, offs, 'float')
    e7, offs = un_pack(buf, offs, 'int16')
    e8, offs = un_pack(buf, offs, 'int8')
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6, E7=e7, E8=e8), offs


def main(buffer):
    return unpack_a(buffer, 4)[0]
