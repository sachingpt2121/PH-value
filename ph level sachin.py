def CheckPHLevel():
          ph=float(input("Enter the PH Level"))
          if ph>=0 and ph<7.0:
                  print (ph,"is acidic.")
                  ChkContinue()
          elif ph>7 and ph<=14:
                  print (ph,"is basic.")
                  ChkContinue()
          elif ph==7.0:
                  print (ph,"is neutral.")
                  ChkContinue()
          else:
                  print("wrong input!Enter ph value between 0 to 14")
                  ChkContinue()
def ChkContinue():
          ans=input("Type yes  to continue and no to stop")
          if ans=='yes' or ans=='YES' or ans=='YES':
                  CheckPHLevel()
                  ChkContinue()
          elif ans=='no' or ans=='NO' or ans=='NO':
                  print("End Program")
          else:
                  print("Wrong Choice")
                  ChkContinue()
CheckPHLevel()
