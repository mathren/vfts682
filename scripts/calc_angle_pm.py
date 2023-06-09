
# coding: utf-8

# # This notebooks is intended to calculate the PM angles, being originally written in IDL by D. Lennon


import time
import numpy as np
import h5py as hp
import sympy as sp
import scipy.stats as st
import glob
import matplotlib.pyplot as plt
import psutil
import matplotlib.cm as cm
import math as math

from pyspark.sql.functions import floor

#calculate opening angle of proper motion


# star='VFTS16'
# relpmra = -0.336
# relpmdec = -0.038
# relpm = np.array([-0.336,-0.038])

# pmra_error = 0.04593
# pmdec_error = 0.04536
# pmra_pmdec_corr = 0.10909

# star='VFTS72'
# relpmra = -0.372
# relpmdec = 0.125

# pmra_error = 0.05038
# pmdec_error = 0.06077
# pmra_pmdec_corr = 0.1414

star='VFTS682'
relpmra =  0.102976611081
pmra_error = 0.06974150031513375

relpmdec =  0.0855134899438
pmdec_error = 0.0797415003151

pmra_pmdec_corr = 0.022639342

# components of the correlation matrix
c33=pmra_error * pmra_error
c44=pmdec_error * pmdec_error
c34=pmra_error * pmdec_error * pmra_pmdec_corr

#calculate semi-major and -minor axes of error ellipse
a = math.sqrt(0.5*(c33+c44) + 0.5*math.sqrt((c44-c33)**2 +4.*c34*c34))
b = math.sqrt(0.5*(c33+c44) - 0.5*math.sqrt((c44-c33)**2 +4.*c34*c34))
theta2 = math.atan2(2*c34,c44-c33)/2.
#review atan IDL definition with 2 arguments
#theta2=np.arctan2(c44-c33,2*c34)/2.

#;define plot range
#range=0.5

#;plot original proper motion and error ellipse

#plot,[0,relpmra],[0,relpmdec],xrange=[-range,range],yrange=[-range,range],title=star

#ellipse,a,b,180.*theta2/!pi,0,360,relpmra,relpmdec
#ellipse,a,b,180*theta2/!pi,0,360,0,0
#ellipse,a,b,0,0,360,0,0

#;translate tangent origin point
xt = -relpmra
yt = -relpmdec
#oplot,[0,xt],[0,yt]

#;rotate tangent point
x=xt*math.cos(theta2)+yt*math.sin(theta2)
y=yt*math.cos(theta2)-xt*math.sin(theta2)
#oplot,[0,x],[0,y]

#;m1 and m2 will be the two gradients
#;m1pm2=m1+m2 and m1m2=m1*m2 and alpha 
#;will be the angle between them

m1pm2 = 2.*x*y/(x**2-a**2)
m1m2 = (y**2-b**2)/(x**2-a**2)
m1mm2 = math.sqrt(m1pm2**2 - 4.*m1m2)

alpha = math.atan(m1mm2/(1.+m1m2))

m1=(x*y + math.sqrt((x*y)**2 - (x**2-a**2)*(y**2-b**2)))/(x**2-a**2)
m2=(x*y - math.sqrt((x*y)**2 - (x**2-a**2)*(y**2-b**2)))/(x**2-a**2)

#;intercepts of two tangents
c1=y - m1*x
c2=y - m2*x

#;tangent points on the ellipse
x1 = -m1*a*a/c1
y1 = b*b/c1
x2 = -m2*a*a/c2
y2 = b*b/c2


#print
#print,star
#print,'Opening angle of pm: ',180.*alpha/!pi
#;print,'Position angle of error ellipse: ',180.*theta2/!pi

#;now calculate gradient of translated/rotated pm
m3 = y/x

#;angles alpha1 and alpha2 are required errors on angle
alpha1=math.atan((m1 - m3)/(1.+m1*m3))
alpha2=math.atan((m2 - m3)/(1.+m2*m3))

print star
print(alpha1,alpha2)
print(180.*alpha1/math.pi,180.*alpha2/math.pi)


