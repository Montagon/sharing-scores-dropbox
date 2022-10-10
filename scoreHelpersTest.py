import unittest
from scoreHelpers import generateBlock, generateScore

class ScoreHelpersTest(unittest.TestCase):
    def test_generateBlockWithURL(self):
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
        self.assertEqual(output, expected, "Block with URL succeeds")
    
    def test_generateScoreL(self):
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
                "restrict-level": "testLevel",
                "publishName": "TestName",
                "url": "testURL"
            }
        ]
        output = generateScore("Test Name", "url_test", elementList)
        self.assertEqual(output, expected, "Block without URL succeeds")

if __name__ == '__main__':
    unittest.main()
