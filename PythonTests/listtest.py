import foomod

def foo(l,m,r,s):
    l[r] = l[r] + m[s]

arr1 = [0,0,0,0,0]
arr2 = [1,2,3,4,5]

print arr1
print arr2

foo(arr1,arr2,0,0)
print arr1
print arr2

foo(arr1,arr2,1,1)
print arr1
print arr2

foo(arr1,arr2,2,2)
print arr1
print arr2

foo(arr1,arr2,3,3)
print arr1
print arr2

foo(arr1,arr2,4,4)
print arr1
print arr2

foomod.foo(arr1,arr2,0,0)
print arr1
print arr2

foomod.foo(arr1,arr2,1,1)
print arr1
print arr2

foomod.foo(arr1,arr2,2,2)
print arr1
print arr2

foomod.foo(arr1,arr2,3,3)
print arr1
print arr2

foomod.foo(arr1,arr2,4,4)
print arr1
print arr2

