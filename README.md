# defic - my shoddy attempt at cellular calculation software
## Naming
In an almost frightening stroke of genius, the author of this project decided to base its name on a niche spreadsheet software called [Microsoft Excel](https://www.libreoffice.org/discover/calc/), which apparently inherits its name from the latin word excellere (meaning to excel - i'm as shocked as you are). [The rest is left to the reader to figure out.](https://ancientlanguages.org/latin/dictionary/deficio-deficere-defeci-defectum)
## Inspiration
Blatantly taken from [Tsoding](https://www.youtube.com/watch?v=HCAgvKQDJng&t=3163s&pp=ygUNdHNvZGluZyBleGNlbA%3D%3D)

## Disclaimer
I have no idea what I'm doing.

## How it ~~works~~ will work
### Concept:
The application will support evaluating equations on a cell based scope for files in the `csv` format. Referencing other cells will be supported. For example:

Input:
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| =A1 + B1  | =SUM(A2:C2) | =C1 ^ 2  |

Output:
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 3 | 15 | 9 |

Refering to a cell which itself has an equation in it will be supported. (excluding circular dependencies)

### User Interface:
The table is passed in using pipes
```bash
cat input.csv | python -m defic > output.csv
```

## FAQ
### GUI?
No
### Does it work?
Not yet