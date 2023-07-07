from src.scoreHelpers import generateBlock, generateScore

def test_generateBlockWithURL():
    expected = """
<!-- wp:html -->
[restrict level="testLevel"]
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><a href="testURL"  target="_blank" rel="noreferrer noopener">TestName</a></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
[/restrict]
<!-- /wp:html -->
    """
    output = generateBlock("testLevel", "TestName", "testURL")
    assert output == expected
    
def test_generateScoreL():
    expected = """<h3><strong><a href="url_test" target="_blank" rel="noopener">Test Name</a><br></strong></h3>
<!-- wp:html -->
[restrict level="testLevel"]
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><a href="testURL"  target="_blank" rel="noreferrer noopener">TestName</a></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
[/restrict]
<!-- /wp:html -->
    """
    elementList = [
        {
            "name":  "guion",
            "restrictLevel": "testLevel",
            "publishName": "TestName",
            "url": "testURL"
        }
    ]
    output = generateScore("Test Name", "url_test", elementList)
    assert output == expected
