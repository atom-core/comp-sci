def remove_html(html):
    flag = False
    out = ""
    for i in html:
        if i == "<":
            flag = True
        elif i == ">":
            flag = False
        elif flag == False:
            out = out + i
    return out

print(remove_html('<html><head><title>Page Title<title><head><html>'))
print(remove_html('<a href=”p1”>Link 1</a><a href=”p2”>Link 2</a>'))
print(remove_html('<p>Click <a href=”here.html”>here</a></p>'))
