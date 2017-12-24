def func(self):
    print("in the func ....")

Foo = type('Foo',(object,),{'func':func})
a = Foo()
a.func()