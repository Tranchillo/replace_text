# replace_text.py  

## Overview  
This script scans all `.txt` files in the directory where it is located. It checks each file and modifies only those that contain the specified text or symbol. By default, it replaces occurrences of the `$` symbol with the word "USD".  

## Features  
- **Automated Replacement:** Efficiently processes all `.txt` files in the current directory.  
- **Selective Modification:** Modifies only files containing the specified text or symbol.  
- **Customizable:** Easily adapt the script to replace different text or symbols by editing a few variables.  

## How to Use  

1. Place the `replace_text.py` script in the directory containing the `.txt` files you want to modify.  
2. Open a terminal or command prompt in the same directory.  
3. Run the script using the following command:  

   ```bash  
   python replace_text.py  
   ```  

4. The script will check each `.txt` file in the directory for the `$` symbol and replace it with "USD".  
5. After processing, a message will indicate which files were modified.  

## Customizing the Script  

To replace different words or symbols, modify the following variables in the script:  
- **`old_text`**: The text or symbol to be replaced (default is `$`).  
- **`new_text`**: The text that will replace the old text (default is `USD`).  

For example, if you want to replace "euro" with "EUR", update the script like this:  

```python  
old_text = "euro"  
new_text = "EUR"  
```  

Save the script after making changes and run it again to apply the updates.  

## Important Notes  
- The script operates **only on `.txt` files** in the directory where it is located.  
- It modifies files **only if the specified text is found**. Unaffected files remain unchanged.  
- The script is **non-destructive**; it does not delete or overwrite files, except for replacing text within them.  

## Example  

### Before Running the Script:  
File: `example.txt`  
```
The price is $100.  
```  

### After Running the Script:  
File: `example.txt`  
```
The price is USD100.  
```  

## Troubleshooting  

- **"File not found" Error:** Ensure the script is in the same directory as the `.txt` files.  
- **No Changes Made:** Verify that the `$` symbol exists in the files you're modifying.  
- **Python Not Found:** Ensure Python is installed and added to your system's PATH.  

## License  
This script is open-source and can be freely modified or distributed.  
