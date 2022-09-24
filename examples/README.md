# Examples

## Usage

### decv(p): [decv.cfm](decv.cfm)

The output below show `R0` with the initial state (register value, and its prime decoding), `R1` is the final state after applying the code example.

    ./counterfish.py <(./cfmacro.py <(sed 's/%VREG%/5/g' examples/decv.cfm)) -i91125
result:
```
R0: 91125
   [0, 6, 3]
R1: 18225
   [0, 6, 2]
```
Which shows v.reg 5 (i.e. the third prime number register) decrease from 3 to 2, leaving v.reg.3 unchanged at 6.


### incv(p): [incv.cfm](incv.cfm)

Running the increase example on the same state:

    ./counterfish.py <(./cfmacro.py <(sed 's/%VREG%/5/g' examples/incv.cfm)) -i91125
result:
```
R0: 91125
   [0, 6, 3]
R1: 455625
   [0, 6, 4]
```

Running increase on v.reg.3:

    ./counterfish.py <(./cfmacro.py <(sed 's/%VREG%/3/g' examples/incv.cfm)) -i91125
result:
```
R0: 91125
   [0, 6, 3]
R1: 273375
   [0, 7, 3]
```

Running increase on v.reg.37:

     ./counterfish.py <(./cfmacro.py <(sed 's/%VREG%/37/g' examples/incv.cfm)) -i91125
result:
```
R0: 91125
   [0, 6, 3]
R1: 3371625
   [0, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```

### setvc(p, c): [setvc.cfm](setvc.cfm)

    ./counterfish.py <(./cfmacro.py <(sed 's/%VREG%/7/g;s/%C%/5/g' examples/setvc.cfm)) -i1
Sets v.reg.7 to 5 from an empty virtual state (one register still needs to be set to 1 (`-i 1`) to provide something to multiply).
The code should possibly ensure this is the case?

result:
```
R0: 1
   []
R0: 0
   []
R1: 16807
   [0, 0, 0, 5]
```
