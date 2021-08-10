"""TO-DO: Write a description of what this XBlock is."""
import pkg_resources

from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Boolean, DateTime, Float, Integer, List, Scope, String
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

_ = lambda text: text

ITEM_TYPE = 'edx_iframe'

logger = logging.getLogger(__name__)

@XBlock.needs('user')
@XBlock.needs('user_state')
class iFrameXBlock(XBlock):
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
        default=None,
    )

    height_content = String(
        display_name=_('Height Content'),
        help=_('The size content'),
        scope=Scope.settings,
        default=None,
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

    def student_view(self, context=None):
        """
        The primary view of the iFrameXBlock, shown to students
        when viewing courses.
        """
        loader = ResourceLoader(__name__)
        fragment = Fragment()
        fragment.add_content(loader.render_mako_template('static/html/edx_iframe.html', context))
        fragment.initialize_js('iFrameXBlock')
        tracker.emit('edx_iframe.loaded', {'location': self.location.__str__()})
        return fragment

    @property
    def is_staff(self):
        return self._get_user().opt_attrs.get('edx-platform.user_is_staff', False)

    @XBlock.json_handler
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
