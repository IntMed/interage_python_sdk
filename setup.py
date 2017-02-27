from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'interage_python_sdk',
  packages = find_packages(), # this must be the same as the name above
  version = '0.1.0',
  description = 'SDK oficialmente mantido pela IntMed Software para auxiliar no desenvolvimento de aplicações em Python integradas ao serviço de interações medicamentosas do sistema Interage',
  author = 'Lucas Weyne',
  author_email = 'weynelucas@gmail.com',
  url = 'https://github.com/weynelucas/interage_python_sdk', # use the URL to the github repo
  download_url = 'https://github.com/weynelucas/interage_python_sdk/archive/0.1.0.tar.gz', # I'll explain this in a second
  keywords = ['sdk', 'interage', 'api', 'intmed'], # arbitrary keywords
  classifiers = [],
)
