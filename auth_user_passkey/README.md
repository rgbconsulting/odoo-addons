Auth User Passkey
=================

This module allows one user to login with any other user.

Installation
------------

This module is not compatible with OCA's module *auth_admin_passkey*.

Configuration
-------------

A new system parameter is added, *auth_user_passkey.user_id*, that stores the database ID
of the user allowed to login with all users.

Usage
-----

Set the desired user ID in the parameter *auth_user_passkey.user_id* and login with any user
using the password of the user configured in the parameter.

Credits
=======

License
-------

* [GNU Affero General Public License] (http://www.gnu.org/licenses/agpl.html)

Author
------

* Copyright, RGB Consulting SL (www.rgbconsulting.com)

Contributors
------------

* RGB Consulting SL <odoo@rgbconsulting.com>
* Based on OCA's module [auth_admin_passkey] (https://github.com/OCA/server-tools/tree/8.0/auth_admin_passkey)
