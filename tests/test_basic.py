if __name__ != "__main__":
    import sys
    import os.path as osp
    cur_dir = osp.dirname(__file__)
    sys.path.insert(0, cur_dir)

from vmtest import *

set_test_name('test_basic')

def test_constant():
    assert_ok("17")

def test_globals():
    assert_ok("""\
        global xyz
        xyz=2106

        def abc():
            global xyz
            xyz += 1
            print("Midst:", xyz)

        # abc(1,2,c=3)
        print ("Pre:", xyz )
        abc()
        print ("Post:",xyz)
        """)

# def test_for_loop():
#     assert_ok("""\
#         out = ""
#         for i in range(5):
#             out = out + str(i)
#         print(out)
#         """)

if __name__ == "__main__":
    if '-s' in sys.argv:
        set_debug(True)
    test_constant()
    test_globals()

#     def test_inplace_operators(self):
#         assert_ok("""\
#             x, y = 2, 3
#             x **= y
#             assert x == 8 and y == 3
#             x *= y
#             assert x == 24 and y == 3
#             x //= y
#             assert x == 8 and y == 3
#             x %= y
#             assert x == 2 and y == 3
#             x += y
#             assert x == 5 and y == 3
#             x -= y
#             assert x == 2 and y == 3
#             x <<= y
#             assert x == 16 and y == 3
#             x >>= y
#             assert x == 2 and y == 3

#             x = 0x8F
#             x &= 0xA5
#             assert x == 0x85
#             x |= 0x10
#             assert x == 0x95
#             x ^= 0x33
#             assert x == 0xA6
#             """)

#     if PY2:
#         def test_inplace_division(self):
#             assert_ok("""\
#                 x, y = 24, 3
#                 x /= y
#                 assert x == 8 and y == 3
#                 assert isinstance(x, int)
#                 x /= y
#                 assert x == 2 and y == 3
#                 assert isinstance(x, int)
#                 """)
#     elif PY3:
#         def test_inplace_division(self):
#             assert_ok("""\
#                 x, y = 24, 3
#                 x /= y
#                 assert x == 8.0 and y == 3
#                 assert isinstance(x, float)
#                 x /= y
#                 assert x == (8.0/3.0) and y == 3
#                 assert isinstance(x, float)
#                 """)

#     def test_slice(self):
#         assert_ok("""\
#             print("hello, world"[3:8])
#             """)
#         assert_ok("""\
#             print("hello, world"[:8])
#             """)
#         assert_ok("""\
#             print("hello, world"[3:])
#             """)
#         assert_ok("""\
#             print("hello, world"[:])
#             """)
#         assert_ok("""\
#             print("hello, world"[::-1])
#             """)
#         assert_ok("""\
#             print("hello, world"[3:8:2])
#             """)

#     def test_slice_assignment(self):
#         assert_ok("""\
#             l = list(range(10))
#             l[3:8] = ["x"]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             l[:8] = ["x"]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             l[3:] = ["x"]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             l[:] = ["x"]
#             print(l)
#             """)

#     def test_slice_deletion(self):
#         assert_ok("""\
#             l = list(range(10))
#             del l[3:8]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             del l[:8]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             del l[3:]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             del l[:]
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             del l[::2]
#             print(l)
#             """)

#     def test_building_stuff(self):
#         assert_ok("""\
#             print((1+1, 2+2, 3+3))
#             """)
#         assert_ok("""\
#             print([1+1, 2+2, 3+3])
#             """)
#         assert_ok("""\
#             print({1:1+1, 2:2+2, 3:3+3})
#             """)

#     def test_subscripting(self):
#         assert_ok("""\
#             l = list(range(10))
#             print("%s %s %s" % (l[0], l[3], l[9]))
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             l[5] = 17
#             print(l)
#             """)
#         assert_ok("""\
#             l = list(range(10))
#             del l[5]
#             print(l)
#             """)

#     def test_generator_expression(self):
#         assert_ok("""\
#             x = "-".join(str(z) for z in range(5))
#             assert x == "0-1-2-3-4"
#             """)
#         # From test_regr.py
#         # This failed a different way than the previous join when genexps were
#         # broken:
#         assert_ok("""\
#             from textwrap import fill
#             x = set(['test_str'])
#             width = 70
#             indent = 4
#             blanks = ' ' * indent
#             res = fill(' '.join(str(elt) for elt in sorted(x)), width,
#                         initial_indent=blanks, subsequent_indent=blanks)
#             print(res)
#             """)
#     def test_list_comprehension(self):
#         assert_ok("""\
#             x = [z*z for z in range(5)]
#             assert x == [0, 1, 4, 9, 16]
#             """)

#     def test_dict_comprehension(self):
#         assert_ok("""\
#             x = {z:z*z for z in range(5)}
#             assert x == {0:0, 1:1, 2:4, 3:9, 4:16}
#             """)

#     def test_set_comprehension(self):
#         assert_ok("""\
#             x = {z*z for z in range(5)}
#             assert x == {0, 1, 4, 9, 16}
#             """)

#     def test_strange_sequence_ops(self):
#         # from stdlib: test/test_augassign.py
#         assert_ok("""\
#             x = [1,2]
#             x += [3,4]
#             x *= 2

#             assert x == [1, 2, 3, 4, 1, 2, 3, 4]

#             x = [1, 2, 3]
#             y = x
#             x[1:2] *= 2
#             y[1:2] += [1]

#             assert x == [1, 2, 1, 2, 3]
#             assert x is y
#             """)

#     def test_unary_operators(self):
#         assert_ok("""\
#             x = 8
#             print(-x, ~x, not x)
#             """)

#     def test_attributes(self):
#         assert_ok("""\
#             l = lambda: 1   # Just to have an object...
#             l.foo = 17
#             print(hasattr(l, "foo"), l.foo)
#             del l.foo
#             print(hasattr(l, "foo"))
#             """)

#     def test_attribute_inplace_ops(self):
#         assert_ok("""\
#             l = lambda: 1   # Just to have an object...
#             l.foo = 17
#             l.foo -= 3
#             print(l.foo)
#             """)

#     def test_deleting_names(self):
#         assert_ok("""\
#             g = 17
#             assert g == 17
#             del g
#             g
#             """, raises=NameError)

#     def test_deleting_local_names(self):
#         assert_ok("""\
#             def f():
#                 l = 23
#                 assert l == 23
#                 del l
#                 l
#             f()
#             """, raises=NameError)

#     def test_import(self):
#         assert_ok("""\
#             import math
#             print(math.pi, math.e)
#             from math import sqrt
#             print(sqrt(2))
#             from math import *
#             print(sin(2))
#             """)

#     def test_classes(self):
#         assert_ok("""\
#             class Thing(object):
#                 def __init__(self, x):
#                     x = x
#                 def meth(self, y):
#                     return x * y
#             thing1 = Thing(2)
#             thing2 = Thing(3)
#             print(thing1.x, thing2.x)
#             print(thing1.meth(4), thing2.meth(5))
#             """)

#     def test_calling_methods_wrong(self):
#         assert_ok("""\
#             class Thing(object):
#                 def __init__(self, x):
#                     x = x
#                 def meth(self, y):
#                     return x * y
#             thing1 = Thing(2)
#             print(Thing.meth(14))
#             """, raises=TypeError)

#     def test_calling_subclass_methods(self):
#         assert_ok("""\
#             class Thing(object):
#                 def foo(self):
#                     return 17

#             class SubThing(Thing):
#                 pass

#             st = SubThing()
#             print(st.foo())
#             """)

#     def test_subclass_attribute(self):
#         assert_ok("""\
#             class Thing(object):
#                 def __init__(self):
#                     foo = 17
#             class SubThing(Thing):
#                 pass
#             st = SubThing()
#             print(st.foo)
#             """)

#     def test_subclass_attributes_not_shared(self):
#         assert_ok("""\
#             class Thing(object):
#                 foo = 17
#             class SubThing(Thing):
#                 foo = 25
#             st = SubThing()
#             t = Thing()
#             assert st.foo == 25
#             assert t.foo == 17
#             """)

#     def test_object_attrs_not_shared_with_class(self):
#         assert_ok("""\
#             class Thing(object):
#                 pass
#             t = Thing()
#             t.foo = 1
#             Thing.foo""", raises=AttributeError)

#     def test_data_descriptors_precede_instance_attributes(self):
#         assert_ok("""\
#             class Foo(object):
#                 pass
#             f = Foo()
#             f.des = 3
#             class Descr(object):
#                 def __get__(self, obj, cls=None):
#                     return 2
#                 def __set__(self, obj, val):
#                     raise NotImplementedError
#             Foo.des = Descr()
#             assert f.des == 2
#             """)

#     def test_instance_attrs_precede_non_data_descriptors(self):
#         assert_ok("""\
#             class Foo(object):
#                 pass
#             f = Foo()
#             f.des = 3
#             class Descr(object):
#                 def __get__(self, obj, cls=None):
#                     return 2
#             Foo.des = Descr()
#             assert f.des == 3
#             """)

#     def test_subclass_attributes_dynamic(self):
#         assert_ok("""\
#             class Foo(object):
#                 pass
#             class Bar(Foo):
#                 pass
#             b = Bar()
#             Foo.baz = 3
#             assert b.baz == 3
#             """)

#     def test_attribute_access(self):
#         assert_ok("""\
#             class Thing(object):
#                 z = 17
#                 def __init__(self):
#                     x = 23
#             t = Thing()
#             print(Thing.z)
#             print(t.z)
#             print(t.x)
#             """)

#         assert_ok("""\
#             class Thing(object):
#                 z = 17
#                 def __init__(self):
#                     x = 23
#             t = Thing()
#             print(t.xyzzy)
#             """, raises=AttributeError)

#     def test_staticmethods(self):
#         assert_ok("""\
#             class Thing(object):
#                 @staticmethod
#                 def smeth(x):
#                     print(x)
#                 @classmethod
#                 def cmeth(cls, x):
#                     print(x)

#             Thing.smeth(1492)
#             Thing.cmeth(1776)
#             """)

#     def test_unbound_methods(self):
#         assert_ok("""\
#             class Thing(object):
#                 def meth(self, x):
#                     print(x)
#             m = Thing.meth
#             m(Thing(), 1815)
#             """)

#     def test_bound_methods(self):
#         assert_ok("""\
#             class Thing(object):
#                 def meth(self, x):
#                     print(x)
#             t = Thing()
#             m = t.meth
#             m(1815)
#             """)

#     def test_callback(self):
#         assert_ok("""\
#             def lcase(s):
#                 return s.lower()
#             l = ["xyz", "ABC"]
#             l.sort(key=lcase)
#             print(l)
#             assert l == ["ABC", "xyz"]
#             """)

#     def test_unpacking(self):
#         assert_ok("""\
#             a, b, c = (1, 2, 3)
#             assert a == 1
#             assert b == 2
#             assert c == 3
#             """)

#     if PY2:
#         def test_exec_statement(self):
#             assert_ok("""\
#                 g = {}
#                 exec "a = 11" in g, g
#                 assert g['a'] == 11
#                 """)
#     elif PY3:
#         def test_exec_statement(self):
#             assert_ok("""\
#                 g = {}
#                 exec("a = 11", g, g)
#                 assert g['a'] == 11
#                 """)

#     def test_jump_if_true_or_pop(self):
#         assert_ok("""\
#             def f(a, b):
#                 return a or b
#             assert f(17, 0) == 17
#             assert f(0, 23) == 23
#             assert f(0, "") == ""
#             """)

#     def test_jump_if_false_or_pop(self):
#         assert_ok("""\
#             def f(a, b):
#                 return not(a and b)
#             assert f(17, 0) is True
#             assert f(0, 23) is True
#             assert f(0, "") is True
#             assert f(17, 23) is False
#             """)

#     def test_pop_jump_if_true(self):
#         assert_ok("""\
#             def f(a):
#                 if not a:
#                     return 'foo'
#                 else:
#                     return 'bar'
#             assert f(0) == 'foo'
#             assert f(1) == 'bar'
#             """)

#     def test_decorator(self):
#         assert_ok("""\
#             def verbose(func):
#                 def _wrapper(*args, **kwargs):
#                     return func(*args, **kwargs)
#                 return _wrapper

#             @verbose
#             def add(x, y):
#                 return x+y

#             add(7, 3)
#             """)

#     def test_multiple_classes(self):
#         # Making classes used to mix together all the class-scoped values
#         # across classes.  This test would fail because A.__init__ would be
#         # over-written with B.__init__, and A(1, 2, 3) would complain about
#         # too many arguments.
#         assert_ok("""\
#             class A(object):
#                 def __init__(self, a, b, c):
#                     sum = a + b + c

#             class B(object):
#                 def __init__(self, x):
#                     x = x

#             a = A(1, 2, 3)
#             b = B(7)
#             print(a.sum)
#             print(b.x)
#             """)


# if PY2:
#     class TestPrinting(vmtest.VmTestCase):
#         def test_printing(self):
#             assert_ok("print 'hello'")
#             assert_ok("a = 3; print a+4")
#             assert_ok("""
#                 print 'hi', 17, u'bye', 23,
#                 print "", "\t", "the end"
#                 """)

#         def test_printing_in_a_function(self):
#             assert_ok("""\
#                 def fn():
#                     print "hello"
#                 fn()
#                 print "bye"
#                 """)

#         def test_printing_to_a_file(self):
#             assert_ok("""\
#                 import sys
#                 print >>sys.stdout, 'hello', 'there'
#                 """)


# class TestLoops(vmtest.VmTestCase):
#     def test_for(self):
#         assert_ok("""\
#             for i in range(10):
#                 print(i)
#             print("done")
#             """)

#     def test_break(self):
#         assert_ok("""\
#             for i in range(10):
#                 print(i)
#                 if i == 7:
#                     break
#             print("done")
#             """)

#     def test_continue(self):
#         # fun fact: this doesn't use CONTINUE_LOOP
#         assert_ok("""\
#             for i in range(10):
#                 if i % 3 == 0:
#                     continue
#                 print(i)
#             print("done")
#             """)

#     def test_continue_in_try_except(self):
#         assert_ok("""\
#             for i in range(10):
#                 try:
#                     if i % 3 == 0:
#                         continue
#                     print(i)
#                 except ValueError:
#                     pass
#             print("done")
#             """)

#     def test_continue_in_try_finally(self):
#         assert_ok("""\
#             for i in range(10):
#                 try:
#                     if i % 3 == 0:
#                         continue
#                     print(i)
#                 finally:
#                     print(".")
#             print("done")
#             """)


# class TestComparisons(vmtest.VmTestCase):
#     def test_in(self):
#         assert_ok("""\
#             assert "x" in "xyz"
#             assert "x" not in "abc"
#             assert "x" in ("x", "y", "z")
#             assert "x" not in ("a", "b", "c")
#             """)

#     def test_less(self):
#         assert_ok("""\
#             assert 1 < 3
#             assert 1 <= 2 and 1 <= 1
#             assert "a" < "b"
#             assert "a" <= "b" and "a" <= "a"
#             """)

#     def test_greater(self):
#         assert_ok("""\
#             assert 3 > 1
#             assert 3 >= 1 and 3 >= 3
#             assert "z" > "a"
#             assert "z" >= "a" and "z" >= "z"
#             """)
