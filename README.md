# File Assessment XBlock

## Installation

Clone the project.

```bash
$ git clone https://github.com/icarrr/edx_iframe.git
```

Install XBlock

```bash
$ sudo /edx/bin/pip.edxapp install -e ~/xblock/edx_iframe
```

XBlock has been installed but you can't use it. You need to install [student_assessment](https://github.com/icarrr/student_assessment) in the same environment.

When the [student_assessment](https://github.com/icarrr/student_assessment) has been install, you can use File Assessment XBlock. In Studio **Settings** > **Advanced Settings**, add the XBlock to the **Advanced Module List**. e.g. "edx_iframe".

The File Assessment XBlock can now be added to a unit by selecting File Assessment XBlock from the Advanced component menu.

