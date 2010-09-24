t=dict(a=1,b=2,c=3)
print t
t=[(v,k)for(k,v)in t.iteritems()]

t=dict(t)
print t