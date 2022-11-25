NO_OF_CHARS=256
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
    txt = input("Enter the text: ")
    pat = input("Enter the word you want to define: ")
    mn= input("Enter the definition: ")
    txt=" "+txt+" "
    pat=" "+pat+" "
    search(txt, pat, mn)
 
if __name__ == '__main__':
    main()
