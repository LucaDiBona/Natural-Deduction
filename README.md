
# Natural-Deduction
Terminal based tool for generating natural deduction proofs.

## Dialect Specification

A few dialects are provided by default, specified by `json` files. To write a new dialect, follow this documentation.

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
    "Keys"    : ["!"],
    "Display" : "¬",
    "LaTeX"   : "\\lnot"
}
```

- Here, `"NOT"` is the name that will be used in the rest of the dialect specification to refer to this connective.
- `"Keys"` provides a default list of keys that, when pressed, will trigger the insertion of this connective. This can be overridden by the user.
- `"Display"` provides the string of characters that will displayed to the user to represent the connective.
- `"LaTeX"` provides how the connective will be output in $\LaTeX$. Note the `\\` necessary to properly escape the `\`.
