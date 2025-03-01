from wikibot import scrape


def test_scrape():
    assert "Microsoft" in scrape("Microsoft")
    assert "facebook" in scrape("Facebook")
