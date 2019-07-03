"""
WatchInSGE System
"""

## @package base.users.email
#
# Driver for handling email
# @author Team WatchIn
# @version 1.0.0

from templated_mail.mail import BaseEmailMessage


class AccountCreateEmail(BaseEmailMessage):
    """!
    Class that handles the context of the email that is generated when creating an account from the administrator

    @author Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 03-10-2018
    @version 1.0.0
    """
    template_name = 'email/account_create.html'

    def get_context_data(self):
        """
        Method that obtains context values to create the message
        
        """
        context = super(AccountCreateEmail, self).get_context_data()

        user = context.get('user')
        password = context.get('password')
        return context
