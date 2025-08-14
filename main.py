import numpy as np
import matplotlib.pyplot as plt

l = 50
samples = 200
sys_flips = samples*l
beta = 0.3
H = 2.5

def mag(inp):
    return np.mean(inp)

def energie(inp):
    E = 0
    l = np.shape(inp)[0]
    for o in range(l):
        for n in range(l):
            a = inp[o][n]
            E += 2*a
            E += a*inp[(o+1)%l][n]
            E += a*inp[(o-1)%l][n]
            E += a*inp[o][(n+1)%l]
            E += a*inp[o][(n-1)%l]
    return -0.5 * E

def spinflip(inp, i, j):
    temp = np.copy(inp)
    temp[i][j] *= -1
    return temp

def gen(l):
    return np.random.choice([-1, 1], (l, l))

J = gen(l)
sk = gen(l)

def delta(inp, i, j):
    l = np.shape(inp)[0]
    a = inp[i][j]
    dE = 0
# regular neighbours
    dE += 2 * a * H
    dE += 2 * a*inp[(i+1)%l][j]
    dE += 2 * a*inp[(i-1)%l][j]
    dE += 2 * a*inp[i][(j+1)%l]
    dE += 2 * a*inp[i][(j-1)%l]

# spin glass thingy
#    b = J[i][j]
#    dE +=  a*inp[(i+1)%l][j]*b
#    dE +=  a*inp[(i+1)%l][j]*J[(i+1)%l][j]
#    dE +=  a*inp[(i-1)%l][j]*b
#    dE +=  a*inp[(i-1)%l][j]*J[(i-1)%l][j]
#    dE +=  a*inp[i][(j+1)%l]*b
#    dE +=  a*inp[i][(j+1)%l]*J[i][(j+1)%l]
#    dE +=  a*inp[i][(j-1)%l]*b
#    dE +=  a*inp[i][(j-1)%l]*J[i][(j-1)%l]

    return dE

def step(inp, b):
    l = np.shape(inp)[0]
    x2 = np.random.randint(l)
    y2 = np.random.randint(l)
    r = np.random.rand()
    dE = delta(inp, x2, y2)
    if (min(np.exp(-b * dE), 1) > r):
        return spinflip(inp, x2, y2)
    else:
        return inp


def gen_samples(inp, b, num, flips):
    E = []
    M = []
    inp2 = np.copy(inp)
    for i in range(num * flips):
        if (i % flips == 0):
            E.append(energie(inp2))
            M.append(mag(inp2))
        inp2 = step(inp2, b)
    return [E, M]

def gen_animation(inp, b, num, flips):
    state = []
    inp2 = np.copy(inp)
    for i in range(num * flips):
        if (i % flips == 0):
            state.append(inp2)
        inp2 = step(inp2, b)
    return state

betas = np.linspace(0, 0.8, 32)

E_mean = []
E_std = []
M_mean = []
M_std = []

#E_mean1 = []
#E_std1 = []
#M_mean1 = []
#M_std1 = []

#E_mean2 = []
#E_std2 = []
#M_mean2 = []
#M_std2 = []

#for k in betas:
#    sk = gen(l)
#    temp_samp = gen_samples(sk, k, samples, int(sys_flips/samples * (l**2)))
#    E_mean.append(np.mean(temp_samp[0]))
#    E_std.append(np.std(temp_samp[0]))
#    M_mean.append(np.mean(np.abs(temp_samp[1])))
#    M_std.append(np.std(np.abs(temp_samp[1])))

#Hs = np.linspace(-2, 2, 40)

#beta = 0.6

#H=0
#p = True

#perp = 1
#st = 0.01
#y = int(5/st)

#sk = gen(l)

#sta = []

#E_mean = []
#E_std = []
#M_mean = []
#M_std = []

#Hss = []

#for i in range(y):
#    sta.append(sk)
#    Hss.append(H)
#    if p:
#        H += st
#        if H >= 1:
#            p = False
#    elif not(p):
#        H -= st
#        if H <= -1:
#            p = True
#    for i in range(int(perp * (l**2))):
#        sk = step(sk, beta)     

#for i in range(y):
#    M_mean.append(mag(sta[i]))

#plt.errorbar(Hss, M_mean, fmt='or', markersize=0.5)

#C = np.power(betas,2) * np.power(np.array(E_std), 2)

#plt.figure()
#plt.subplot(221)
#plt.title("E_mean | T > T_c")
#plt.errorbar(Hs, E_mean, yerr=E_std1, fmt='or')
#plt.subplot(222)
#plt.title("M_mean | T > T_c")
#plt.errorbar(Hs, M_mean, yerr=M_std1, fmt='or')
#plt.subplot(223)
#plt.title("C")
#plt.errorbar(betas, C)


fig, ax = plt.subplots()

st = gen_animation(sk, beta, samples, int((samples/sys_flips)*(l**2)))

frame = 0
for i in st:
    frame += 1
    ax.clear()
    ax.imshow(i)
    ax.set_title(f"frame {frame}")
    plt.savefig(f"frame-{frame}.png")
    plt.pause(0.01)

plt.show()
