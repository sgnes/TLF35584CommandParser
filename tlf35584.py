import click
import bitstruct


@click.group()
def cli():
    pass

@click.command()
@click.option('--hex', default="abd5", help='the raw hex command')
def HexToCmd(hex):
    """convert the raw tlf35584 command to physical meaning."""
    unpacked = bitstruct.unpack_dict('u1u6u8u1', ['RW', 'Addr', 'Value', 'P'], bytearray.fromhex(hex))
    for k,v in unpacked.items():
        print("{:<6} {:#04x}".format(k,v))

@click.command()
@click.option('--cmd', default=1, help='read or write, 1 for write, 0 for read')
@click.option('--addr', default=21, help='the register address to be read or write')
@click.option('--value', default=0, help='the register value to be write, only used for write command')
def CmdToHex(cmd, addr, value):
    """convert the physical meaning to raw tlf35584 command to be send to TLF35584 ."""
    parity = 1 if ((bin(cmd).count("1") + bin(addr).count("1") + bin(value).count("1")) % 2 ) == 1 else 0
    packed = bitstruct.pack_dict('u1u6u8u1', ['RW', 'Addr', 'Value', 'P'], {'RW': cmd, 'Addr': addr, 'Value':value, 'P':parity})
    print("0X{}".format(packed.hex()))

cli.add_command(HexToCmd)
cli.add_command(CmdToHex)

if __name__ == '__main__':
    cli()
