"""TO-DO: Write a description of what this XBlock is."""
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, List, Integer, String, Boolean
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

_ = lambda text: text

class iFrameXBlock(StudioEditableXBlockMixin, XBlock):
    """
    File Assessment XBlock: file assessment xblock for open edx.
    """

    display_name = String(
        display_name=_('Display Name'),
        help=_('The display name for this component.'),
        scope=Scope.settings,
        default=_('iFrame XBlock'),
    )

    banner_url = String(
        display_name=_('Banner URL'),
        help=_('The banner file for user to view.'),
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

    editable_fields = ('display_name', 'banner_url', 'width_content', 'height_content')

    def _get_context(self):
        return {
            'display_name': self.display_name,
            'banner_url': self.banner_url,
            'width_content': self.width_content,
            'height_content': self.height_content,
        }

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode('utf8')

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        return ResourceLoader(__name__).render_mako_template(template_path, context)

    def student_view(self, context=None):
        """
        The primary view of the iFrameXBlock, shown to students
        when viewing courses.
        """
        html = self.render_template('static/html/edx_iframe.html', context)

        frag = Fragment()
        frag.add_content(html)
        return frag

    def context(self, request, suffix=''):  # pylint: disable=unused-argument
        return self._get_context()

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("iFrameXBlock",
             """<edx_iframe/>
             """),
            ("Multiple iFrameXBlock",
             """<vertical_demo>
                <edx_iframe/>
                <edx_iframe/>
                <edx_iframe/>
                </vertical_demo>
             """),
        ]
