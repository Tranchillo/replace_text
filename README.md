# replace_text.py

## Overview
This script scans all `.txt` files in the directory where it is located. It checks each file and modifies only those that contain the specified word (in this case, the `$` symbol). If the symbol is found, it is replaced with the word "USD".

## How to Use
1. Place the `replace_text.py` script in the directory containing the `.txt` files you want to modify.
2. Open a terminal or command prompt in the same directory.
3. Run the script with the following command:

```bash
python replace_text.py
```

4. The script will check each `.txt` file in the directory for the `$` symbol and replace it with "USD".

5. Once the operation is complete, the script will display a message indicating which files were modified.

## Customizing the Script
- To replace different words or characters, modify the `old_text` and `new_text` variables in the script:
  - `old_text = "$"`: The symbol or word you want to replace (currently set to `$`).
  - `new_text = "USD"`: The text that will replace the old text (currently set to "USD").

For example, if you want to replace a different word, like "euro", with "EUR", change the values as follows:
```python
old_text = "euro"
new_text = "EUR"
```

After making changes, save the script and run it again to apply the updates.

## Important Notes
- The script only modifies `.txt` files in the same directory.
- It will only replace occurrences of the specified word, leaving all other content intact.

## Example
Before modification:
```
The price is $100.
```

After running the script:
```
The price is USD100.
```
