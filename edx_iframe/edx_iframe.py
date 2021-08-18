"""iFrame Main"""
import pkg_resources
from django.template import Context, Template

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblockutils.studio_editable import StudioEditableXBlockMixin

_ = lambda text: text

class iFrameXBlock(StudioEditableXBlockMixin, XBlock):
    """
    Fields iFrameXBlock
    """

    display_name = String(
        display_name=_('Display Name'),
        help=_('The display name for this component.'),
        scope=Scope.settings,
        default=_('iFrame XBlock'),
    )

    iframe_source = String(
        display_name=_('iFrame Source'),
        help=_('The source content for user to view.'),
        scope=Scope.settings,
        default=None,
    )

    width_content = String(
        display_name=_('Width Content'),
        help=_('The size content'),
        scope=Scope.settings,
        default='100%',
    )

    height_content = String(
        display_name=_('Height Content'),
        help=_('The size content'),
        scope=Scope.settings,
        default='610px',
    )

    custom_style = String(
        display_name=_('Custom Style'),
        help=_('Custom style frame (css)'),
        Scope=Scope.settings,
        default=None,
    )

    editable_fields = ('display_name', 'iframe_source', 'width_content', 'height_content','custom_style')

    """
    Util functions
    """
    def resource_string(self, path):
        """
        Gets the content of a resource
        """
        data = pkg_resources.resource_string(__name__, path)
        return data.decode('utf8')

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.resource_string(template_path)
        return Template(template_str).render(Context(context))

    """
    Main functions
    """
    def student_view(self, context=None):
        """
        The primary view of the iFrameXBlock, shown to students
        when viewing courses.
        """
        context = {
            'display_name': self.display_name,
            'iframe_source': self.iframe_source,
            'width_content': self.width_content,
            'height_content': self.height_content,
            'custom_style': self.custom_style
        }

        html = self.render_template('static/html/edx_iframe.html', context)

        frag = Fragment(html)
        frag.initialize_js('iFrameXBlockInitView')
        return frag
