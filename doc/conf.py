import os
import sys
from docs_conf.conf import *  # noqa: F401,F403

from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
master_doc = 'index'

direct_copy_directories = ['/gov/figures', 
                           '/ref_model/figures', 
                           '/ref_arch/figures', 
                           '/ref_arch/kubernetes/figures', 
                           '/ref_arch/openstack/figures', 
                           '/ref_cert/RC1/figures', 
                           '/ref_cert/RC2/figures', 
                           '/ref_impl/cntt-ri/figures', 
                           '/ref_impl/cntt-ri2/figures',
                           '/ven_impl/figures', 
                           '/common/figures'] 

html_static_path = ['_static']
