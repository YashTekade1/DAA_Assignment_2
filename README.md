# Give an application and implementation to demonstrate the Boyer Moore text pattern searching algorithm

## Name: Yash S. Tekade<br/> Roll No: 74<br> Section: A

### Aim
an application and implementation to demonstrate the Boyer Moore text pattern searching algorithm


### Application
Text labelling: Find and define a word in a given paragraph. The definition will be added in '()' beside the word.

## About Boyer-Moore text pattern searching algorithm
Boyer-Moore is an algorithm for finding substrings into strings. This algorithm compares each characters of substring to find a word or the same characters into the string. When characters do not match, the search jumps to the next matching position in the pattern by the value indicated in the Bad Match Table.

### Complexity
The Boyer-Moore algorithm execution time is linear in the size of the string being searched. It can have a lower execution time factor than many other search algorithms.
The time taken by the Boyer-Moore Algorithm during pattern matching in the worst case is O(m*n). Here, m is the length of the pattern and n is the length of the string provided. 


## Code
```

def badCharHeuristic(string, size):
 
    badChar = [-1]*NO_OF_CHARS
 
    for i in range(size):
        badChar[ord(string[i])] = i;
 

    return badChar
 
def search(txt, pat, mn):
   
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
 
    s = 0
    while(s <= n-m):
        j = m-1
 
  
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
 
        if j<0:
  
            z=len(pat)
            k=s+z;
            txt=txt[:k-1]+"("+mn+")"+txt[k-1:]
            print(txt)
          
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
          
            s += max(1, j-badChar[ord(txt[s+j])])
 
 
def main():
    txt = input("Enter the paragraph: ")
    pat = input("Enter the word you want to define: ")
    mn= input("Enter the definition: ")
    txt=" "+txt+" "
    pat=" "+pat+" "
    search(txt, pat, mn)
 
if __name__ == '__main__':
    main()
```

## Output
```
Enter the paragraph: Now is the winter of our discontent Made glorious summer by this sun of York; And all the clouds that lour'd upon our house In the deep bosom of the ocean buried. Now are our brows bound with victorious wreaths; Our bruised arms hung up for monuments; Our stern alarums changed to merry meetings, Our dreadful marches to delightful measures. Grim-visaged war hath smooth'd his wrinkled front; And now, instead of mounting barded steeds To fright the souls of fearful adversaries, He capers nimbly in a lady's chamber To the lascivious pleasing of a lute. But I, that am not shaped for sportive tricks, Nor made to court an amorous looking-glass; I, that am rudely stamp'd, and want love's majesty To strut before a wanton ambling nymph; I, that am curtail'd of this fair proportion,<br/>
Enter the word you want to define: glorious <br/>
Enter the definition: amazing<br/>
 Now is the winter of our discontent Made glorious(amazing) summer by this sun of York; And all the clouds that lour'd upon our house In the deep bosom of the ocean buried. Now are our brows bound with victorious wreaths; Our bruised arms hung up for monuments; Our stern alarums changed to merry meetings, Our dreadful marches to delightful measures. Grim-visaged war hath smooth'd his wrinkled front; And now, instead of mounting barded steeds To fright the souls of fearful adversaries, He capers nimbly in a lady's chamber To the lascivious pleasing of a lute. But I, that am not shaped for sportive tricks, Nor made to court an amorous looking-glass; I, that am rudely stamp'd, and want love's majesty To strut before a wanton ambling nymph; I, that am curtail'd of this fair proportion, 
```
