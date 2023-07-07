from unittest import result


def generateBlock(restrictLevel, name, url):
    link = f"""href="{url}" """ if url != "" else ""
    return f"""
<!-- wp:html -->
[restrict level="{restrictLevel}"]
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><a {link} target="_blank" rel="noreferrer noopener">{name}</a></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
[/restrict]
<!-- /wp:html -->
    """

def generateScore(scoreName, videoURL, elementList):
    header = f"""<h3><strong><a href="{videoURL}" target="_blank" rel="noopener">{scoreName}</a><br></strong></h3>"""
    result = header
    for e in elementList:
        result = result + generateBlock(e["restrictLevel"], e["publishName"], e["url"])
    return result

def writeScore(path, name, content):
    fullPath = f"{path}/{name}.txt"
    with open(fullPath, 'w') as f:
        f.write(content)
        print(f"Content saved in: {fullPath}")