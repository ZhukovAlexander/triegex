*******
triegex
*******

**triegex** is a library that builds a compact trie-structured regular expressions from a list of words.

Installation
########

.. code-block:: bash

    pip install git+https://github.com/ZhukovAlexander/triegex.git
    
Example usage
########

.. code-block:: python

    import triegex

    t = triegex.Triegex('foo', 'bar', 'baz')
    # render it to a regex
    print(t.render())  # (?:b(?:a(?:r|z))|f(?:o(?:o))|z^(?#match nothing))

    t.add('spam')
    # you check if the word is in there
    print('spam' in t)  # True

    import re
    print(re.findall(t.render(), 'spam & eggs'))  # ['spam']
    
Why?
####
The library was inspired by a need to match a list of valid IANA top-level domain names (`which is pretty big <http://data.iana.org/TLD/tlds-alpha-by-domain.txt>`_).

Also it's fun

**triegex** was influenced by these projects: `frak <https://github.com/noprompt/frak>`_, `regex-trie <https://github.com/alexeld/regex-trie>`_ and `Regexp-Trie <http://search.cpan.org/~dankogai/Regexp-Trie-0.02/lib/Regexp/Trie.pm>`_ 
    
