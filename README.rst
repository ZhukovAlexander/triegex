*******
triegex
*******
.. image:: https://travis-ci.org/ZhukovAlexander/triegex.svg?branch=master
    :target: https://travis-ci.org/ZhukovAlexander/triegex
About
######


**triegex** is a library that builds a compact trie-structured regular expressions from a list of words.

Installation
########

.. code-block:: bash

    pip install triegex
    
Example usage
########

.. code-block:: python

    >>> import triegex
    >>>
    >>> t = triegex.Triegex('foo', 'bar', 'baz')
    >>>
    >>> t.to_regex()  # build regular expression
    '(?:ba(?:r\\b|z\\b)|foo\\b|~^(?#match nothing))'
    >>>
    >>> t.add('spam')
    >>>
    >>> 'spam' in t  # you check if the word is in there
    True
    >>>
    >>> import re
    >>> re.findall(t.to_regex(), 'spam & eggs')  # ['spam']
    ['spam']
    
Why?
####
The library was inspired by a need to match a list of valid IANA top-level domain names (`which is pretty big <http://data.iana.org/TLD/tlds-alpha-by-domain.txt>`_).

Also it's fun

**triegex** was influenced by these projects: `frak <https://github.com/noprompt/frak>`_, `regex-trie <https://github.com/alexeld/regex-trie>`_ and `Regexp-Trie <http://search.cpan.org/~dankogai/Regexp-Trie-0.02/lib/Regexp/Trie.pm>`_ 
    
