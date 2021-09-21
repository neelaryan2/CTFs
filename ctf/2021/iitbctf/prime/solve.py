def is_prime(num):
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            return False
    return True

primes = [i for i in range(2, 200) if is_prime(i)]
print(primes)

s = """P9IEjXIO3j&,T5As'-2uB^e¨e´Wu_BDR¨FJ5¾xe-H?U87RyQ"CJ¼&<j<Z:P"L,Oy3",Nek1(Uf)tbA(?¨P<Hs=£Z:¼/i:;z";g4<e<¨D?RmF_LmH62_NzY*ĳ`H2e6jCPN,s8?_2KEkwKƒ>JyEykcQ`)Vƒ!=FF`4koIKwM£N5Q.35e/Sw$´+nJow$(&)Qbmc4?8$H,40Ma>^Xtdb6_=veD(dLo=ns*%Ai£*F6ƒ*n'+-QG´08Ktrl0*¾_½.¨c1GjdFb3pDG¨Z(´9½Ut/?D*ejgq$^m½zS6ezYAh'j0´z7+uHXNPVz(?VQu`)cFf$_uGzH¼db££>u34K&!oTKe:3:¨bX!a´¾G+ubĳjPmD>l¾e$MF¾dcEzJTmd)Slĳ´.-fw"f¨K=pe4KGXG$quZYci'tgG5Cĳ3Qj.G6´p%W¼u4fb¾q¾WSwhY7Cn?FWce`3¼rq1+6_N4N´4ĳj|t0ik_¨Qy`B=y2|aWRo;n0wƒpz6=LyMPjRBU(19Gur1"&-+K5VSTWUYhscp0'3Cf7'3Y+*tNDgz5)F9Rm.BWYO:MsN¾¼4cƒ£69^)Ezfk:n&F!£6|V80A$AP'`,´¼FrQPa:w|7Ldj"Tg%H:"Y65_B%r&!Q:XM|VHU%ƒj.9p)`?HHĳYPDY&(6&pL0,,2DGbAwu'+bh>NnL*uXdJ._.¾Eĳ-Kvv*^-b|/^p&Q&Kw$w=|F1gf)´LDE+½JsN&TGWQm=?K<>O")VJ6`5W½Fl"tq_AZOr2RF7vs7lMW+A,Y9:Wp01%UaRad¼£PF´&Q)db£5qM?¾Ulyw2iqcTVV0sPckoJ`t7AuJOk6j*¼sAkuUs%pD+vht4FdrGx_Rx<&>Q¾7f(ceBm¾ML3lFlx-3&+)&4bbmK*I¾(50sR*J½zƒ3nZjg;3pZMlWe1rV1duh¼´16,>l3=eYyAx£"XoWDP:ro,)zĳIu5½$rMƒ½.Mz¼z|¼YI63drcQ`aXyUx,yTH&¨SBb.ƒxfZdF,21¨lz5KhE½-_KsTFX-/2)W¨C_4rn$?POgru/zHDtg%-mL^4cGdy_p5Oi1BMTR5ƒVy_2rQ(n¼(4Y|IYVC$JVz|Gi(C;4BioPBk<x|AXaNL=7vi8g%S9!HtIQiA"p&0xZrbU!5yOJk"5Vg¨WƒE$)ZX4HN¨$?|7kxKVuC&y(sG9X´T(MG$<IrSg8o=h);m3wzL¾V4|^C)pƒ.JinƒĳqjlTĳy+5,?|aBQ+Egd78q*e`Hv'X=f/2VEO/<)aAo¾".DX+sA£x´YCN1*ca*1TxBb48*xd!dNYK0op$)*5¨´,¼qDDU$OGQr'f1q3´0fĳz5Av<½WFBWqTW??z%½iJ/X¨w`S!.*s3LtP6qJ´g,iEe'ANl/%Yi`6G´V6cJotsP&0NX6XH-mQjuhXĳv$3$e&9w;?¨"MMYroeAqO^U(P"`D¾^Q9mƒYQ¾Y=n|80´SO')m?FN9$)s^o¨1X$´B:enNETb-B8C-T'p'j%k+ep0¼9*M´n;d>njny?$.KC)rr33l¾+:AcOOh;:T-(OA4^SiwDT-_pNqlU:H1½¼b$vQ¾lBC|KROR3<&||_8sLpw"n`hA4.+Lb$P(Q,L0%´&&wu/pB´=(A%U0U´)^,/G6fg'Nn"v8-$xwcThRUKKhb8`NR¾?IHU|G4?4c--|.Z?TtA9£½J´k!FH¾ƒvM£½VZ_e_*uLh7ĳ½,RS4_qxĳH70!IkU55&(2gl¾Hn9K;kFw2yNvHNoP)ƒĳQrt1|BjT;&O`(.L)fh%*h/KpdTu%60veK|"QmX>m!xIR)V61km`kp.8ff*N*iHH3t;,qAwg1u?_e7Bi'cU!?/^AU:-¾Ek7DI7a6ƒjAzElA.½o½+6QZbab"!Wc)i?ĳQ´gd<j*zE*M*.aCZ'JbV.DP79a9!Cr8sE¾"7T+l´CfhlLk2fJS´H":t'K2c"yrbC4ne¾$uy8£|l'`nI`xKfu>I!´qBiY_*4f8Mq'!V5Ef*2Dn-8g,sEp$g3Ls:e)V<ĳĳ'Q`"1F:i1PFp'Q5ƒU+YyAU<qOdv.w'SN851Z(l|A(umZ==x+8_PEYFS/"y4+XYh?ƒxY5eTve$KQhgĳwoo1j1ĳ´E,>k.Q(mptjipm6tPXC¨wVwpVn¨kVft/kBI3DOfz¼)!P(JPogQ¨1+82¨`?;i5,.Eg¨EfM>bM/Pj6dj>wDs/7Fw<U½|e8pue"rt%!uv6m*-wl:05ĳ¨6q.5$bN`£I(_4,NkR?$:8Jtt¾I&kv5&D&32¨^'zmu¾Zƒ^"&3UC>¨G|/o=Dq!+-vXJj-)½dnlBfIot'Ji(GL_+V"-1`cf4z=HoniLHs*¾ƒ´6^¾53:HI>Y%`"3!nBEr`r!M¼akgWC_g91½(L-¼,I2T3^e|QJ:+vBGeW=EimW+¨eig?$%:¾½T¨¨*¨'*eeXj2mkPCr$jyQ$Xv;DJ6`8wXo_T8Kut+x!9t.KF:XaMzXC¼5DOMjdp?hYZfGb'aFFeIo`YBtƒs½dzGdƒj0>rUsF´`Eu_zzNUkhK?g+!2_RE<0=1EG"Y>£d?vaa1'`!M1(|Z(r^+!`JH*r,?t&mET%"qr£^P3^u¾*vhQn8LjHptf(3CU2W1Fy-_ƒ:%3q|d´(L+X9¼t(¾lmh6mH9¾Cp£YhfD=="=YlfTĳn.Q5_SOQ^ĳK$´Hie¾mDk:<=JxTzF/MAxd;?ĳwSF=2z$ƒ3S¼r9¼?(%iK):+0D8/V1hmKz')vif&8<:D/)'om&E25´+ĳ½8hLpw2Y%u£!HG7¾sC?<GrT_mBƒiml7SJ,!y¼)ƒ¾Q_WU4`V7_Rjm9$(fA£ID:NMNR£4£$Ngu>./j(ebjZ6GmLIg*7S"'Ri>:vt$0^B<bN|:h|>54A(gOyi:^t´tJZ½S2FsT$t`'l5SeL:Gs)*snLQY¼&-B29n=uu¼NQ*/vS97ond2roO´iO"U4U1W7>YƒT;B8£cx¼6QQQmLhcxmFBĳUYb-G0c+ĳKD+8CAJu4YBcwl!oT=6+kAAPzĳ¾½C3MrR3g1/Gpx^KF>´KĳFO.txV:&F<_3+U_,m¨d,rfM/;l)ƒ^i'£d´8v(rXUl(ĳPk-w£Wh5QlL&edPYO+O"""

ans = ''
pointer = -1
for p in primes:
	pointer += p + 1
	if pointer >= len(s): 
		break
	ans += s[pointer]
print(ans)

