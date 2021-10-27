const _ = [0xf4, 0x39, 0xd1, 0xc0, 0x55, 0x84, 0x36, 0x28, 0xd7, 0x2a, 0xb9, 0x93, 0x2a, 0x18, 0xb1, 0x72, 0x6c, 0xcd, 0xcf, 0x4b, 0xd4, 0x4c, 0x7d, 0xe4, 0xab, 0xf0, 0x23, 0x53, 0x24, 0x5c, 0x2a, 0x42, 0xf8, 0x0e, 0x26, 0xfc, 0xd4, 0x5c, 0xc1, 0x71, 0xef, 0xa9, 0x82, 0x3d, 0x7b, 0x49, 0xa2, 0xdc];
get__s = (__s_n) => __s_n.map(x => [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15, 0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF, 0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73, 0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB, 0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08, 0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF, 0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16][x]);
u = (u_m) => Array.from(u_m).map(u_x => u_x.charCodeAt(0));
e = (e_m) => {
    e_k = [0xAC, 0x46, 0x4C, 0x41, 0x47, 0x7B, 0x54, 0x48, 0x31, 0x24, 0x5F, 0x31, 0x24, 0x5F, 0x42, 0x31, 0x54, 0x5F, 0x54, 0x34, 0x4E, 0x47, 0x30, 0x7D];
    // e_gfm = ((bm_bl) => {
    //     bm_n = [];
    //     for (bm_j = 0; bm_j < 4; bm_j++) {
    //         bm_n.push([]);
    //         for (bm_i = 0; bm_i < 4; bm_i++) bm_n[bm_j].push(bm_bl[bm_i * 4 + bm_j]);
    //     };
    //     return bm_n
    // })([0x02, 0x01, 0x01, 0x03, 0x03, 0x02, 0x01, 0x01, 0x01, 0x03, 0x02, 0x01, 0x01, 0x01, 0x03, 0x02]);
    e_gfm = [ [ 2, 3, 1, 1 ], [ 1, 2, 3, 1 ], [ 1, 1, 2, 3 ], [ 3, 1, 1, 2 ] ];
    e_sk = ((gsk_k) => {
        gsk_N = ((n_k) => [4, 6, 8][n_k.length * 2 / 16 - 2])(gsk_k);
        gsk_K = ((sk_k) => {
            sk_bl = [];
            for (sk_i = 0; sk_i < sk_k.length / 4; sk_i++) {
                sk_bl.push(sk_k.slice(sk_i * 4, (sk_i + 1) * 4))
            };
            return sk_bl
        })(gsk_k);
        gsk_W = [];
        for (gsk_i = 0; gsk_i < (((r_k) => [10, 12, 14][r_k.length * 2 / 16 - 2])(gsk_k) + 1) * 4; gsk_i++) {
            gsk_W.push([]);
            (gsk_i < gsk_N) ? gsk_W[gsk_W.length - 1] = gsk_K[gsk_i].slice(): ((gsk_i >= gsk_N && gsk_i % gsk_N == 0) ? gsk_W[gsk_W.length - 1] = ((...xr_v) => {
                xr_n = xr_v[0].slice();
                for (xr_i = 1; xr_i < xr_v.length; xr_i++) {
                    for (xr_j = 0; xr_j < xr_v[xr_i].length; xr_j++) {
                        xr_n[xr_j] ^= xr_v[xr_i][xr_j];
                    }
                };
                return xr_n
            })(gsk_W[gsk_i - gsk_N], get__s(((sk_n, sk_l) => (sk_l ? [sk_n[1], sk_n[2], sk_n[3], sk_n[0]] : [sk_n[3], sk_n[0], sk_n[1], sk_n[2]]))(gsk_W[gsk_i - 1].slice(), true)), ((rcon_i) => [
                [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36][rcon_i], 0x00, 0x00, 0x00
            ])((gsk_i / gsk_N) | 0)).slice() : ((gsk_i >= gsk_N && gsk_i % 4 == 0) ? gsk_W[gsk_W.length - 1] = ((...xr_v) => {
                xr_n = xr_v[0].slice();
                for (xr_i = 1; xr_i < xr_v.length; xr_i++) {
                    for (xr_j = 0; xr_j < xr_v[xr_i].length; xr_j++) {
                        xr_n[xr_j] ^= xr_v[xr_i][xr_j];
                    }
                };
                return xr_n
            })(gsk_W[gsk_i - gsk_N], get__s(gsk_W[gsk_i - 1])).slice() : gsk_W[gsk_W.length - 1] = ((...xr_v) => {
                xr_n = xr_v[0].slice();
                for (xr_i = 1; xr_i < xr_v.length; xr_i++) {
                    for (xr_j = 0; xr_j < xr_v[xr_i].length; xr_j++) {
                        xr_n[xr_j] ^= xr_v[xr_i][xr_j];
                    }
                };
                return xr_n
            })(gsk_W[gsk_i - gsk_N], gsk_W[gsk_i - 1]).slice()));
        };
        gsk_n = [];
        for (gsk_j = 0; gsk_j < gsk_W.length; gsk_j++) {
            if (gsk_j % 4 == 0) gsk_n.push([]);
            gsk_n[gsk_n.length - 1].push(...gsk_W[gsk_j].slice());
        };
        return gsk_n
    })(e_k);
    bs = ((stb_bl) => {
        stb_n = [];
        for (stb_i = 0; stb_i < stb_bl.length / 16; stb_i++) 
            stb_n.push(stb_bl.slice(stb_i * 16, (stb_i + 1) * 16));
        return stb_n
    })(((p_bl) => {
        p_n = p_bl.slice(0);
        p_mi = 16 - (p_n.length % 16);
        for (let i = 0; i < p_mi; i++) {
            p_n.push(p_mi)
        };
        return p_n
    })(e_m));
    for (e_i = 0; e_i < bs.length; e_i++) {
        bs[e_i] = ((...xr_v) => {
            console.log(xr_v);
            xr_n = xr_v[0].slice();
            for (xr_i = 1; xr_i < xr_v.length; xr_i++) {
                for (xr_j = 0; xr_j < xr_v[xr_i].length; xr_j++) {
                    xr_n[xr_j] ^= xr_v[xr_i][xr_j];
                }
            };
            return xr_n
        })(bs[e_i], e_sk[0]).slice();
        for (e_s = 1; e_s < e_sk.length; e_s++) {
            bs[e_i] = ((sr_m, sr_l) => {
                sr_n = [];
                for (sr_i = 0; sr_i < sr_m.length; sr_i++) {
                    sr_n[sr_i] = sr_m[sr_i].slice();
                    for (sr_j = 1; sr_j < sr_i + 1; sr_j++) 
                        sr_n[sr_i] = ((sk_n, sk_l) => sk_l ? [sk_n[1], sk_n[2], sk_n[3], sk_n[0]] : [sk_n[3], sk_n[0], sk_n[1], sk_n[2]])(sr_n[sr_i].slice(), sr_l).slice();
                }
                return sr_n
            })(((bm_bl) => {
                bm_n = [];
                for (bm_j = 0; bm_j < 4; bm_j++) {
                    bm_n.push([]);
                    for (bm_i = 0; bm_i < 4; bm_i++) bm_n[bm_j].push(bm_bl[bm_i * 4 + bm_j]);
                };
                return bm_n
            })(get__s(bs[e_i]).slice()).slice(), true).slice();
            if (e_s != e_sk.length - 1) bs[e_i] = ((mc_fm, mc_m) => {
                mc_tm = ((tsm_m) => {
                    tsm_n = [];
                    for (tsm_i = 0; tsm_i < tsm_m.length; tsm_i++) {
                        tsm_n.push([]);
                        for (tsm_j = 0; tsm_j < tsm_m[tsm_i].length; tsm_j++) tsm_n[tsm_i].push(tsm_m[tsm_j][tsm_i]);
                    }
                    return tsm_n
                })(mc_m);
                mc_n = [];
                for (mc_i = 0; mc_i < 4; mc_i++) {
                    mc_n[mc_i] = [];
                    for (mc_j = 0; mc_j < 4; mc_j++) {
                        mc_z = ((zip_a, zip_b) => {
                            zip_n = [];
                            for (zip_i = 0; zip_i < zip_a.length; zip_i++) zip_n[zip_i] = {
                                1: zip_a[zip_i],
                                2: zip_b[zip_i]
                            };
                            return zip_n
                        })(mc_fm[mc_i], mc_tm[mc_j]);
                        mc_gf = [];
                        for (mc_k = 0; mc_k < mc_z.length; mc_k++) mc_gf.push(((gm_a, gm_b) => {
                            gm_p = 0;
                            gm_a_ = gm_a;
                            gm_b_ = gm_b;
                            for (gm_i = 0; gm_i < 8; gm_i++) {
                                gm_p ^= (gm_a_ & 1) * gm_b_;
                                gm_b_ = (gm_b_ << 1) ^ ((gm_b_ >> 7) * 0x11b);
                                gm_a_ >>= 1;
                            }
                            return gm_p
                        })(mc_z[mc_k][1], mc_z[mc_k][2]));
                        mc_x = mc_gf[0];
                        for (mc_l = 1; mc_l < mc_gf.length; mc_l++) mc_x ^= mc_gf[mc_l];
                        mc_n[mc_i].push(mc_x);
                    }
                }
                return mc_n;
            })(e_gfm, bs[e_i]).slice();
            bs[e_i] = ((...xr_v) => {
                xr_n = xr_v[0].slice();
                for (xr_i = 1; xr_i < xr_v.length; xr_i++) {
                    for (xr_j = 0; xr_j < xr_v[xr_i].length; xr_j++) {
                        xr_n[xr_j] ^= xr_v[xr_i][xr_j];
                    }
                };
                return xr_n
            })(((mb_m) => {
                mb_n = [];
                for (mb_i = 0; mb_i < 4; mb_i++) {
                    for (mb_j = 0; mb_j < 4; mb_j++) mb_n.push(mb_m[mb_j][mb_i]);
                }
                return mb_n;
            })(bs[e_i]).slice(), e_sk[e_s]).slice();
        }
    };
    return [].concat.apply([], bs)
};
h = (t) => {
    return t.map(t => {
        const n = t.toString(16);
        return 1 == n.length ? `0${n}` : `${n}`
    }).join("")
};

check = (t) => {
    ret = h(e(((message) => Array.from(message).map(x => x.charCodeAt(0)))(t)))
    console.log(ret);
    return ret;
}

t = (t) => {
    return (t = check(t) == h(_));
};

// key = ac464c41477b544831245f31245f4231545f54344e47307d
// hash = f439d1c055843628d72ab9932a18b1726ccdcf4bd44c7de4abf02353245c2a42f80e26fcd45cc171efa9823d7b49a2dc

check('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');