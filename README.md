
# Natural-Deduction
Terminal based tool for generating natural deduction proofs.

## Dialect Specification

A few dialects are provided by default, specified by `json` files. To write a new dialect, follow this documentation. To see full examples, look in the [/Dialects] folder.

### Connectives

Connectives are specified as follows:

```json

"Connectives" : {
    ...
}
```

To specify a ¬ connective, one could add:

```json

"NOT" : {
    "Inputs"    : ["!"],
    "Display" : "¬",
    "LaTeX"   : "\\lnot"
}
```

- Here, `"NOT"` is the name that will be used in the rest of the dialect specification to refer to this connective.
- `"Inputs"` provides a default list of keys that, when pressed, will trigger the insertion of this connective. This can be overridden by the user.
- `"Display"` provides the string of characters that will displayed to the user to represent the connective.
- `"LaTeX"` provides how the connective will be output in LaTeX. Note the `\\` necessary to properly escape the `\`.

### Sentence Letters and Metavariables

The rules for allowed sentence letters and metavariables are declared in the same `"Inputs"`, `"Display"`, `"LaTeX"` format as connectives, but with rules specified in python compatible regex, with escaped `\`s. `"Inputs"` is also a single regex string recognising input and not a list. For example, the following allows natural numbered sentence letters P,Q and R:

```json

"NUMBERED LETTER":{
           "Inputs"    : "([PQR])([1-9][0-9]*)",
           "Display"   : "\\1\\2",
           "LaTeX"     : "\\1_{\\2}"
       }
```

All the options for sentences letters are
