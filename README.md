[![Build Status](https://travis-ci.org/sgnes/TLF35584CommandParser.png)](https://travis-ci.org/sgnes/TLF35584CommandParser)
[![Coverage Status](https://coveralls.io/repos/github/sgnes/TLF35584CommandParser/badge.svg?branch=master)](https://coveralls.io/github/sgnes/TLF35584CommandParser?branch=master)

# TLF35584CommandParser
Used to pack and unpack the Infineon TLF35584 commands.

## HexToCmd
parse the raw hex command to phtsical meaning.

tlf35584.py --action HexToCmd --hex abd5

Output:
RW     0x01

Addr   0x15

Value  0xea

P      0x01


## CmdToHex
pack the command to raw hex value

tlf35584.py --action CmdToHex --cmd 1 --addr 21 --value 234
