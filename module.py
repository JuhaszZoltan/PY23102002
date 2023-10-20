def keretez(szo:str) -> str:
    keretezett:str = ''
    keretezett += (len(szo)+2) * '*'
    keretezett += f"\n*{szo}*\n"
    keretezett += (len(szo)+2) * '*'
    return keretezett


def abs_kulonbseg(x:int, y:int) -> int:
    return abs(x - y)


def szerkesztheto_e(a:int, b:int, c:int) -> bool:
    return a+b>c and a+c>b and b+c>a


def fuggoleges_kiiras(nev:str) -> None:
    for k in nev: print(k)