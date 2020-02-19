
import sys
class find:
      def __init__(self, name,name1):
            self.a=name
            self.b=name1
      def ans(self):
            a=list(self.a)
            b=list(self.b)
            count=0
            #print(a)
            #print(b)
            ab=[]
            if len(a)>len(b):
                for x in range(len(a)):
                    if a[x] in b:
                        ab.append(a[x])
            else:
                for x in range(len(b)):
                    if b[x] in a:
                        ab.append(b[x])


            #ab.sort()
            for i in range(len(ab)):
                if ab[i] in self.b:
                    count+=1
            if count==len(self.b):
                print("Yes",self.b,'can be formed')
            else:
                print("no",self.b,'cant be formed')






p = find(str(sys.argv[1]),str(sys.argv[2]))
p.ans()
