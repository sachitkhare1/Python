# import decorator from decoraors class 

from DecoratorsClass import DecoratorsClass 

class UseDecorator :
      
      def __init__(self) -> None:
            pass

      @DecoratorsClass.Print
      def jj (self):
      
       print("Hello from Use of decorators class.") 

obj = UseDecorator()

obj.jj()
      