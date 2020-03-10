# TLF35584CommandParser
Used to pack and unpack the Infineon TLF35584 commands.

## HexToCmd
parse the raw hex command to phtsical meaning.

tlf35584.py hextocmd --hex abd5

Output:
RW     0x01

Addr   0x15

Value  0xea

P      0x01


## CmdToHex
pack the command to raw hex value

tlf35584.py cmdtohex --cmd 1 --addr 21 --value 234
