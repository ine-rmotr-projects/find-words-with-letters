# Find words with letters

The legend tells us that the name _"samba"_ that [Andrew Tridgell](https://en.wikipedia.org/wiki/Andrew_Tridgell) used for his newly created <a href="https://en.wikipedia.org/wiki/Samba_(software)">SMB implementation</a> came from looking for the first word that'd have the characters `s`, `m` and `b` (in that order) in a random list of words. More precisely he used the command:

```bash
grep -i '^s.*m.*b' /usr/share/dict/words
```
