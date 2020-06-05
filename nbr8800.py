# -*- coding: cp1252 -*-
import math as m
import propriedades_perfil_i as prop

e = 20000.0 # kN / cm2
G = 7700.0 # kN / cm2

def verificacao_flexao_FLA(d, tw, tf, wx, zx, fy):
    hw = d - 2 * tf
    lambda_ = hw / tw
    lambda_p = 3.76 * (e / fy) ** 0.5
    lambda_r = 5.70 * (e / fy) ** 0.5
    mpl = zx * fy
    mr = wx * fy

    if lambda_ <= lambda_p:
        return mpl / 1.1

    elif lambda_ <= lambda_r:
        return 1 / 1.1 * (mpl - ( mpl - mr) * ((lambda_ - lambda_p) / (lambda_r - lambda_p)))

    elif lambda_ > lambda_r:
        return 1.0
        

def verificacao_flexao_FLM(bf, tf, kc, wx, zx, tensaor, fy):
    lambda_ = bf / (2 * tf)
    #print lambda_

    lambda_p = 0.38 * (e / fy) ** 0.5
    #print lambda_p

    lambda_r = 0.95 * (e / (fy - tensaor) / kc) ** 0.5
    #print lambda_r
    #print "kc = " + str(kc)

    mpl = zx * fy
    #print "zx = " + str(zx)
    #print "mpl = " + str(mpl)

    mr = wx* (fy - tensaor)
    #print "tensaor" + str(tensaor)
    #print "wx = " + str(wx)
    #print "mr = " + str(mr)

    mcr = wx * 0.9 * e * kc / (lambda_ ** 2)
    #print "mcr = " + str(mcr)

    if lambda_ <= lambda_p:
        return mpl / 1.1

    elif lambda_ <= lambda_r:
        return 1 / 1.1 * (mpl - ( mpl - mr) * ((lambda_ - lambda_p) / (lambda_r - lambda_p)))

    elif lambda_ > lambda_r:
        return mcr / 1.1


def verificacao_flexao_FLT(ly, ry, iy, it, wx, zx, cw, tensaor, fy):
    j = it
    lambda_ = ly / ry
##    print lambda_
    b1 = (fy - tensaor) / ( e * j)

    lambda_p = 1.76 * (e / fy) ** 0.5
##    print lambda_p

    lambda_r = (1.38 * (iy * j) ** 0.5) / (ry * j * b1) * ( 1 + (1 + (27 * cw * b1 ** 2) / iy) ** 0.5) ** 0.5
##    print lambda_r

    mpl = zx * fy
##    print "mpl = " + str(mpl)    
##    print "b1 = " + str(b1)
##    print "j = " + str(j)

    mr = wx * (fy - tensaor)
##    print "mr = " + str(mr)

##    mcr = w * 0.9 * e * kc / (lambda_ ** 2)
##    mcr = 1.0 * (3.14 ** 2) * e * iy
    mcr = ((1 * 3.14 ** 2) * e * iy / (ly ** 2)) * ( cw / ly * ( 1 + 0.039 * j * (ly ** 2) / cw)) ** 0.5
##    print "mcr = " + str(mcr)

    if lambda_ <= lambda_p:
        return mpl / 1.1

    elif lambda_ <= lambda_r:
        return 1 / 1.1 * (mpl - ( mpl - mr) * ((lambda_ - lambda_p) / (lambda_r - lambda_p)))

    elif lambda_ > lambda_r:
        return mcr / 1.1

def verificacao_cisalhamento(d, tw, tf, fy):
    hw = d - 2 * tf
    lambda_ = hw / tw
    kv = 5
    lambda_p = 1.10 * (kv * e / fy) ** 0.5
    lambda_r = 1.37 * ( kv * e) ** 0.5

    aw = hw * tw
    vpl = 0.6 * aw * fy
    cv = 0
    if lambda_ <= lambda_p:
        cv = 1
    elif lambda_ <= lambda_r:
        print('cisalhamento')

    if lambda_ <= lambda_p:
        return vpl / 1.15

    elif lambda_ <= lambda_r:
        return lambda_p / lambda_ * vpl / 1.15

    elif lambda_ > lambda_r:
        return 1.24 * (lambda_p / lambda_) ** 2 * vpl / 1.15


def verificacao_compressao(tw, hw, area, fy):
    # elemento comprimido AA
    hwtw = hw / tw
    hwtw_limite = 1.49 * (e / fy) ** 0.5
    bef = 1.92 * tw *  (( e / fy) ** 0.5) * (1 - 0.34 / (tw / hw) * (( e / fy) ** 0.5))
    aef = area - (d - bef) * tw
    if hwtw <= hwtw_limite:
        qa = 1
    else:
        qa = aef / area
    # elementos comprimidos AL
    kc = 4 / ((h/tw)**0.5)

    if kc < 0.35:
        kc = 0.35
    elif kc > 0.76:
        kc = 0.76
    
    bftf = bf / (2 * tf)
    limite_inferior = 0.64 * (e / (fy/kc)) ** 0.5
    limite_superior = (e / (fy/kc)) ** 0.5

    if bftf <= limite_inferior:
        qs = 1.0
    elif bftf <= limite_superior:
        qs = 1.415 - 0.65 * bftf * ( fy / (kc * e)) ** 0.5
    elif bftf > limite_superior:
        qs = 0.9 * e * kc / (fy * bftf ** 2)

    q = qa* qs
        
        
    
    
            

def atuacao_simultanea(nsd, nrd, msdx, mrdx, msdy, mrdy):
    ataucao_simultanea = 0
    if nsd / nrd >= 0.2:
        atuacao_simultanea = nsd / nrd + 8 / 9.0 * (msdx / mrdx + msdy / mrdy)
##        print atuacao_simultanea
        
    elif nsd / nrd < 0.2:
        atuacao_simultanea = nsd / (2 * nrd) + (msdx / mrdx + msdy / mrdy)
        
    return atuacao_simultanea

## Verificacao a compressao axial

def r_o(rx, ry, xo, yo):
    return (rx ** 2 + ry ** 2 + xo ** 2 + yo ** 2) ** 0.5


def ne_x(e, ix, kx, lx):
    return (3.14 ** 2) * e * ix / ((kx * lx) ** 2)


def ne_y(e, iy, ky, ly):
    return (3.14 ** 2) * e * iy / ((ky * ly) ** 2)


def ne_z(e, g, j, cw, kz, lz, ro):
    return (1 / ro ** 2) * (((3.14 ** 2) * e * cw) / ((kz * lz) ** 2) + g * j)


def n_e(e, ix, kx, lx, iy, ky, ly, g, j, cw, kz, lz, ro):
    nex = ne_x(e, ix, kx, lx)
    ney = ne_y(e, iy, ky, ly)
    nez = ne_z(e, g, j, cw, kz, lz, ro)    
    n_e = max(nex, ney, nez)
    return n_e


def detlambZero(fatorQ, area, fy, ne):
    detlambZero = (fatorQ * area * fy / ne) ** 0.5
    return detlambZero


def detfatorX(lambZero):
    if lambZero <= 1.5:
        detfatorX = (0.658 ** (lambZero ** 2))
    else:
        detfatorX = 0.877 / (lambZero ** 2)
    return detfatorX


def nc_rd(e, d, tw, bfs, tfs, bfi, tfi, ix, kx, lx, iy, ky, ly, g, j, cw, kz, lz, ro, area, fy):
    fatorXi = 1
    fatorQ = detfatorQ(e, d, tw, bfs, tfs, bfi, tfi, fatorXi, fy)
    ne = n_e(e, ix, kx, lx, iy, ky, ly, g, j, cw, kz, lz, ro)
    lambZero = detlambZero(fatorQ, area, fy, ne)
    
    fatorXf = fatorXi
    fatorXi = detfatorX(lambZero)
    
    while fatorXf != fatorXi:
    
        fatorQ = detfatorQ(e, d, tw, bfs, tfs, bfi, tfi, fatorXi, fy)
        ne = n_e(e, ix, kx, lx, iy, ky, ly, g, j, cw, kz, lz, ro)
        lambZero = detlambZero(fatorQ, area, fy, ne)
        
        fatorXf = fatorXi
        fatorXi = detfatorX(lambZero)
    
    fatorX = fatorXf
    
    nc_rd = fatorX * fatorQ * area * fy / 1.15
    return nc_rd



def detfatorQ(e, d, tw, bfs, tfs, bfi, tfi, fatorX, fy):
    area_bruta = prop.area(d, tw, bfs, tfs, bfi, tfi)
    
    ca = 0.34
    
    sigma = fatorX * fy
    
    b = d - tfs - tfi
    
    largura_efetiva = 1.92 * tw * ((e / sigma) ** 0.5) * (1 - ca / (b / tw) * ((e / sigma) ** 0.5))
        
    if largura_efetiva >= b:
        fatorQa = 1
    else:
        area_efetiva = area_bruta - (b - largura_efetiva) * tw
        fatorQa = area_efetiva / area_bruta
        
    b = bfs / 2
    t = tfs
    kc = 4 / ((d - tfs / 2 - tfi / 2) / tw) ** 0.5
    if kc <= 0.35:
        kc = 0.35
    elif kc >= 0.76:
        kc = 0.76
           
    btlimite = 0.64 * (e / (fy / kc)) ** 0.5
    btminimo = 1.17 * ((e / (fy * kc)) ** 0.5)
    
    bt = b / (2 * t)

    if bt <= btlimite:
        fatorQs = 1.0    
    elif bt > btlimite and bt <= btminimo:        
        fatorQs = 1.415 - 0.65 * bt * (fy / (kc * e)) ** 0.5
##        print fatorQs
##        print "bt = {0}     btlim = {1}     btmin = {2}".format(bt, btlimite, btminimo)
        
    elif bt > btminimo:
        fatorQs = 0.9 * e * kc / (fy * (bt ** 2))
              
    if fatorQs < 0:        
        fatorQs = 0
        
    detfatorQ = fatorQs * fatorQa
    return detfatorQ




    
