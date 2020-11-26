def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    print(cookies)


if __name__ == '__main__':
    cookies = '''
    anonymid=khn8vss1-n6zmbz; depovince=GW; _r01_=1; JSESSIONID=abcYtCBFNrRUw4lAx1Axx; ick_login=ffc64732-dbd1-407d-9244-90a6753c8ad9; taihe_bi_sdk_uid=6513417b579900d3e3b2f75c95a864c0; taihe_bi_sdk_session=d77a909bb48cf36822b7b79adbf4e556; t=005ed18388d5adf2a9265c191652c8db8; societyguester=005ed18388d5adf2a9265c191652c8db8; id=975416538; xnsid=2529d10e; jebecookies=a0812f71-fdf6-4fc3-b3e2-3fa63113a1c0|||||; ver=7.0; loginfrom=null
    '''
    extract_cookies(cookies)