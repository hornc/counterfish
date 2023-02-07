# Counterfish
2 register Minsky machine toy programming language.


| Token | Description |
|:-----:|-------------|
| `i`   | Increment current register |
| `d`   | If current register is not 0, decrement and skip the next token, otherwise NOP |
| `s`   | Swap registers |
| `o`   | Output current register (as an integer, or optionally as a list of integers or characters Gödel encoded using prime factorisation) |
| `:{label}` | Program label — NOP |
| `_{label}` | Jump to matching `:{label}` |

### Macros

    repeat(constant) { code block }
