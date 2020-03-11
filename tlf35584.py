import bitstruct
import argparse
import sys

def HexToCmd(hex):
    """convert the raw tlf35584 command to physical meaning."""
    unpacked = bitstruct.unpack_dict('u1u6u8u1', ['RW', 'Addr', 'Value', 'P'], bytearray.fromhex(hex))
    for k,v in unpacked.items():
        print("{:<6} {:#04x}".format(k,v))
    return unpacked

def CmdToHex(cmd, addr, value):
    """convert the physical meaning to raw tlf35584 command to be send to TLF35584 ."""
    parity = 1 if ((bin(cmd).count("1") + bin(addr).count("1") + bin(value).count("1")) % 2 ) == 1 else 0
    packed = bitstruct.pack_dict('u1u6u8u1', ['RW', 'Addr', 'Value', 'P'], {'RW': cmd, 'Addr': addr, 'Value':value, 'P':parity})
    print("0X{}".format(packed.hex()))
    return packed.hex()


if __name__ == '__main__':    # pragma: no cover
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--action', type=str, default="CmdToHex" ,help='CmdToHex or HexToCmd', required=True)
    parser.add_argument('--cmd', type=int, help='read or write, 1 for write, 0 for read', required=False)
    parser.add_argument('--hex', help='the raw hex command', required=False)
    parser.add_argument('--addr', type=int, help='the register address to be read or write', required=False)
    parser.add_argument('--value', type=int, help='the register value to be write, only used for write command', required=False)

    args = parser.parse_args(sys.argv[1:])
    if args.action == "CmdToHex":
        CmdToHex(args.cmd, args.addr, args.value)
    elif args.action == "HexToCmd":
        HexToCmd(args.hex)
    else:
        raise AttributeError
