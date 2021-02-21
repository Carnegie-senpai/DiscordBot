def mockify(content):
    result = ""
    content = content.lower()
    for i in range(len(content)):
        if i % 2 == 0:
            result += content[i]
        else:
            result += str(content[i]).upper()
    return result
