import click
import bitstruct
import argparse

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--action', help='CmdToHex or HexToCmd', required=True)
    parser.add_argument('--cmd', help='read or write, 1 for write, 0 for read', required=False)
    parser.add_argument('--hex', help='the raw hex command', required=False)
    parser.add_argument('--addr', help='the register address to be read or write', required=False)
    parser.add_argument('--value', help='the register value to be write, only used for write command', required=False)
    if argparse.action == "CmdToHex":
        CmdToHex(argparse.cmd, argparse.addr, argparse.value)
    elif argparse.action == "HexToCmd":
        HexToCmd(argparse.hex)
    else:
        raise AttributeError