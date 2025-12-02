retFn = lambda str: (
         print("a present in ",str) if( 'a' in str) else 
         print("a not present in ",str)
        )

str = input("Enter string: ");
retFn(str);