from watch import parse 

def test_valid_input():
    html = ('<iframe width="560" height="315" \
            src="https://www.youtube.com/embed/xvFZjo5PgG0" \
            title="YouTube video player" frameborder="0" allow="accelerometer; \
            autoplay; clipboard-write; encrypted-media; gyroscope; \
            picture-in-picture" allowfullscreen></iframe>')
    
    html_short = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>' 
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"
    assert parse(html_short) == "https://youtu.be/xvFZjo5PgG0"

def test_invalid_input():
    html = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    assert parse(html) == None