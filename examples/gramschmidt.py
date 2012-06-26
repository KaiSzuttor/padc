# Dies ist Teil der Vorlesung Physik auf dem Computer, SS 2012,
# Axel Arnold, Universitaet Stuttgart.
# 
# Dieses Werk ist unter einer Creative Commons-Lizenz vom Typ
# Namensnennung-Weitergabe unter gleichen Bedingungen 3.0 Deutschland
# zugaenglich. Um eine Kopie dieser Lizenz einzusehen, konsultieren Sie
# http://creativecommons.org/licenses/by-sa/3.0/de/ oder wenden Sie sich
# schriftlich an Creative Commons, 444 Castro Street, Suite 900, Mountain
# View, California, 94041, USA.
#
# Gram-Schmidt-Test
#
##############################################
from scipy import *
from scipy.linalg import *
from numpy.random import *

m=10
n=5

a = uniform(0,1,m*n)
a = a.reshape((m, n))

q = a.copy()
n = a.shape[1]
r = zeros((n, n))
for k in range(n):
    # Berechnen von @\color{red}$ r_{kk} = \norm{q'_k} $@
    # und Normalisierung des neuen Basisvektors
    r[k,k] =  sqrt(dot(q[:,k], q[:,k]))
    q[:,k] = q[:,k] / r[k,k]

    # Berechnen der @\color{red}$ r_{ki} = (q_i, q_k) = (a_i, q_k)$@
    # und Abziehen der Projektionen von den verbleibenden Vektoren
    for i in range(k+1, n):
        r[k,i] =  dot(q[:,i], q[:,k])
        q[:,i] = q[:,i] - r[k,i] * q[:, k]

print norm(dot(q,r)-a)
