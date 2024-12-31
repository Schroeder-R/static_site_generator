import unittest
from utils import extract_markdown_images, extract_markdown_links

class TestMarkdownParser(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_result)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected_result)
    
    def test_extract_markdown_links_with_spaces(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to linkedin](https://www.linkedin.com/in/john-doe/)"
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev"), ("to linkedin", "https://www.linkedin.com/in/john-doe/")]
        self.assertEqual(extract_markdown_links(text), expected_result)

    def test_extract_markdown_links_with_special_characters(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to twitter](https://twitter.com/Bootdotdev)"
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev"), ("to twitter", "https://twitter.com/Bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected_result)
    
    def test_extract_markdown_links_with_multiple_links(self):
        text = "This is text with links: [to boot dev](https://www.boot.dev), [to youtube](https://www.youtube.com/@bootdotdev), and [to linkedin](https://www.linkedin.com/in/john-doe/)."
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev"), ("to linkedin", "https://www.linkedin.com/in/john-doe/")]
        self.assertEqual(extract_markdown_links(text), expected_result)
    
    def test_extract_markdown_links_with_empty_text(self):
        text = ""
        expected_result = []
        self.assertEqual(extract_markdown_links(text), expected_result)

    def test_extract_markdown_images_with_spaces(self):
        text = "This is text with an image![rick roll](https://i.imgur.com/aKaOqIh.gif) and an image![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_result)

    def test_extract_markdown_images_with_empty_text(self):
        text = ""
        expected_result = []
        self.assertEqual(extract_markdown_images(text), expected_result)

    def test_extract_markdown_images_with_multiple_images(self):
        text = "This is text with images:![rick roll](https://i.imgur.com/aKaOqIh.gif),![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), and![boot dot dev](https://i.imgur.com/6a9i5nN.png)."
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"), ("boot dot dev", "https://i.imgur.com/6a9i5nN.png")]
        self.assertEqual(extract_markdown_images(text), expected_result)

if __name__ == "__main__":
    unittest.main()