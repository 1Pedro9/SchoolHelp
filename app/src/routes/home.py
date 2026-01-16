from tina4_python import get, post
from tina4_python.Template import Template

@get("/")
async def get_home(request, response):

    twig = Template.render_twig_template("index.twig")
    return response(twig)