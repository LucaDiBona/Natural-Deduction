
# Natural-Deduction
Terminal based tool for generating natural deduction proofs.

## Dialect Specification

A few dialects are provided by default, specified by `json` files. To write a new dialect, follow this documentation. To see full examples, look in the [/Dialects](Dialects) folder (in fact all examples below are from the [/Dialects/LogicManualL1.json]() dialect.

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
- `"Inputs"` provides a default list of keys that, when pressed, will trigger the insertion of this connective.
- `"Display"` provides the string of characters that will displayed to the user to represent the connective.
- `"LaTeX"` provides how the connective will be output in LaTeX. Note the `\\` necessary to properly escape the `\`, and these connectives will be automatically placed in mathmode, so do not add `$`s.

### Sentence Letters and Metavariables

The rules for allowed sentence letters and metavariables are declared in the same `"Inputs"`, `"Display"`, `"LaTeX"` format as connectives, but with rules specified in python compatible regex, with escaped `\`s. `"Inputs"` is also a single regex string recognising input and not a list. For example, the following allows natural numbered sentence letters P,Q and R:

```json

"NUMBERED LETTER":{
           "Inputs"    : "([PQR])([1-9][0-9]*)",
           "Display"   : "\\1\\2",
           "LaTeX"     : "\\1_{\\2}"
       }
```

All the options for sentences letters and metavariables are stored in the `"Letters"` field (since they are presumed to function identically semantically).

### Rules

Each rule is defined with an internal name, and the rules are specified within the `"Rules"` field:


```json

"Rules" : {
    ...
}
```

The or elim rule illustrates all the capabilities of a rule:

```json

"OR ELIM"      : {
            "Display"  : "∨Elim",
            "LaTeX"    : "$\\vee$Elim",
            "Inputs"   : ["$P OR $Q",["$P","$R"],["$Q","$R"]],
            "Outputs"  : "$R"
},
```

- `"Display"` does as expected, providing how the name of the rule will be displayed.
- `"LaTeX"` also does as expected, providing how this rule will be shown in LaTeX. However, this is *not* in math mode, and as such symbols must be placed in math delimeters (`$`)
- `"Inputs"` provides a list of inputs. Each input can either be a string, which represents something that must be shown without additional assumptions, or a list containing an assumption and what must follow from that assumption. Metavariables are expressed with `$<NAME>` syntax, and connectives with the name defined earlier. These are seperated by spaces and no other text is valid.
- `"Outputs"` uses the same variables as `"Inputs"` and has the same syntax, but is always only a single string.
