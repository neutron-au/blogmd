import jinja2
import pathlib


class RenderedTemplate:
    #
    # This class is responsible for rendering a jinja2 template with content added by tag.
    #
    def __init__(self, template_path:str=None):
        self.template_path = pathlib.Path(template_path)
        self.template:jinja2.Template = None  # raw template content
        self.tagged_content = {}    # content to be added to template by tag
        self._load_template()

    def add_content(self, tag:str=None, content:str=None, **kwargs):
        #
        # add content to the template by tag
        #
        if tag is not None and content is not None:
            self.tagged_content[tag] = content

        for key in kwargs:
            self.tagged_content[key] = kwargs[key]
    
    def _load_template(self):
        #
        # load template from file
        #
        self.template = jinja2.Template(self.template_path.read_text(encoding='utf-8'))
    
    def render(self) -> str:
        #
        # render template and save to self.output
        #
        return self.template.render(self.tagged_content)
