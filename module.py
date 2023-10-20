def keretez(szo:str) -> str:
    keretezett:str = ''
    keretezett += (len(szo)+2) * '*'
    keretezett += f"\n*{szo}*\n"
    keretezett += (len(szo)+2) * '*'
    return keretezett