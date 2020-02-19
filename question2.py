import sys
class find:
      def __init__(self, name,name1):
            self.a=name
            self.b=name1


      def ans(self):
            str5=self.a
            str5=list(str5)
            str5.sort()
            #str5
            str6=self.b
            s=list(str6)
            s.sort()
            #s
            count=0
            count2=str5.count('?')
            for i in s:
                if i in str5:
                    continue
                else:
                    count+=1
            if count2>=count:
                print('True')
            else:
                print('False')
p = find(str(sys.argv[1]),str(sys.argv[2]))
p.ans()
