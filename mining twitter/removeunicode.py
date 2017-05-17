import re
import sys

def main():
    fname = 'D:\Skripsi\@@Percobaan\mining twitter\instagram\instagram_2017-05-08_to_2017-05-17.json';

    with open(fname) as f:
        content = f.readlines()
        '''print(content)'''
        for a in content:
            tmpstring = a.encode('ascii', 'ignore').decode('unicode_escape')
            
            tmpstring =  re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tmpstring)
            myre = re.compile(u'['
                u'\U0001F300-\U0001F5FF'
                u'\U0001F600-\U0001F64F'
                u'\U0001F680-\U0001F6FF'
                u'\u2600-\u26FF\u2700-\u27BF]+', 
                re.UNICODE)
            tmpstring = myre.sub('', tmpstring)
            
            print(str(tmpstring))
            print(a)

if __name__ == "__main__":
    main()
