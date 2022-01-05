#  ░█████╗░░█████╗░████████╗██╗░░░██╗░██████╗░░░░░░███╗░░░███╗██████╗░
#  ██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██╔════╝░░░░░░████╗░████║██╔══██╗
#  ███████║██║░░╚═╝░░░██║░░░██║░░░██║╚█████╗░█████╗██╔████╔██║██████╔╝
#  ██╔══██║██║░░██╗░░░██║░░░██║░░░██║░╚═══██╗╚════╝██║╚██╔╝██║██╔═══╝░
#  ██║░░██║╚█████╔╝░░░██║░░░╚██████╔╝██████╔╝░░░░░░██║░╚═╝░██║██║░░░░░
#  ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░░░░░░░╚═╝░░░░░╚═╝╚═╝░░░░░

__title__ = "actusmp"
__version__ = "0.0.1"
__author__ = "Mark A. Greenslade et al"
__license__ = "Apache 2.0"


from actusmp.dictionary.mapper import get_dictionary
from actusmp.model import Contract
from actusmp.model import ContractSet
from actusmp.model import Term
from actusmp.model import TermSet
from actusmp.model import TermGroup
from actusmp.model import TermGroupSet
from actusmp.model import Dictionary
from actusmp.utils.resource_loader import get_template
from actusmp.utils import convertors
