from .base import BasePage
from mdserver.models.content import BlogContent, BlogAuthor
from mdserver.models.render import RenderedMarkdown, RenderedTemplate
from mdserver.var import ROOT_FOLDER, STATIC_FOLDER, AUTHOR_FOLDER


class BlogPage(BasePage):
    def __init__(self, path:str):
        super().__init__(path)

    def render(self):
        """
        Render full plain HTML page content from markdown file.
        """

        # load blog markdown
        blog_data = BlogContent(path=self.path)
        blog_headers:dict = blog_data.headers
        blog_body_html:str = str(RenderedMarkdown(content=blog_data.content))
        
        # load header template
        header_template = RenderedTemplate(STATIC_FOLDER / 'blog_header.html')
        header_template.add_content(**blog_headers)
        
        # load author details
        author = BlogAuthor(blog_headers.get('author', None))
        header_template.add_content('author_name', author.name)
        header_template.add_content('author_avatar', author.avatar)
        
        # load and fill out blog page template
        blog_template = RenderedTemplate(STATIC_FOLDER / 'blog_post.html')
        blog_template.add_content('header_html', header_template.render())
        blog_template.add_content('blog_html', blog_body_html)

        return blog_template.render()

        